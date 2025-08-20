#!/usr/bin/env python3
"""
Script to generate GenerateBodyAssets classes for all CreateBodyAssets classes found in types/params directory.

WHAT IT DOES:
- Finds all *_create_body_assets.py files in magic_hour/types/params/
- For each CreateBodyAssets class, creates a new separate file with GenerateBodyAssets class
- The Generate classes are identical to Create classes except:
  1. Class name changes from "Create" to "Generate"
  2. File path docstrings change from API upload URLs to local file paths
- Creates new files: *_create_body_assets.py -> *_generate_body_assets.py

SPECIAL CASES:
- FaceMappingsItem classes: Only converts `new_face` field docs, leaves `original_face` unchanged
  (because original_face comes from API response, not user upload)
- Import handling: For face swap classes that reference FaceMappingsItem, imports are updated to use
  generate versions automatically (avoiding mixed Create/Generate imports)

WHEN TO RUN:
- After adding new CreateBodyAssets classes
- After modifying existing CreateBodyAssets classes
- When file path documentation needs updates

USAGE:
    python codemod/generate_asset_types.py                    # Dry run - shows what would be changed
    python codemod/generate_asset_types.py --apply            # Apply changes to all files
    python codemod/generate_asset_types.py --file <path>      # Process specific file only
    python codemod/generate_asset_types.py --check            # Check if any files need updates
    python codemod/generate_asset_types.py --quiet            # Minimal output

SAFETY:
- Always runs in dry-run mode by default
- Use --apply to actually create new files
- Original CreateBodyAssets classes are never modified
- Creates separate files so no existing code is affected
- Existing GenerateBodyAssets files are overwritten if they exist
"""

import os
import re
import glob
import sys
import argparse
from typing import List, Tuple


def extract_create_body_assets_class(file_content: str, class_name: str) -> str:
    """Extract the CreateBodyAssets class from file content."""

    # Find the start of the specific CreateBodyAssets class
    class_start = file_content.find(f"class {class_name}(typing_extensions.TypedDict):")
    if class_start == -1:
        raise ValueError(f"{class_name} class not found")

    # Find the end of the class (next class definition or end of file)
    class_end = file_content.find("\nclass _Serializer", class_start)
    if class_end == -1:
        class_end = len(file_content)

    return file_content[class_start:class_end].strip()


def generate_generate_body_assets_class(
    create_class_content: str, file_path: str = ""
) -> str:
    """
    Convert a CreateBodyAssets class to a GenerateBodyAssets class.

    The main differences:
    1. Class name changes from Create to Generate
    2. File path docstrings change from API upload URLs to local file paths

    Special handling for FaceMappingsItem classes:
    - Only converts new_face field documentation
    - Leaves original_face field unchanged (it's from API response)
    """

    # Replace CreateBodyAssets with GenerateBodyAssets in class name
    content = re.sub(r"CreateBodyAssets", "GenerateBodyAssets", create_class_content)

    # Check if this is a FaceMappingsItem class (special case)
    is_face_mappings_item = (
        "FaceMappingsItem" in create_class_content and "face_mappings_item" in file_path
    )

    # Pattern to find file path documentation that needs to be replaced
    if is_face_mappings_item:
        # For FaceMappingsItem, only replace new_face field documentation
        file_path_pattern = r'(new_face: typing_extensions\.Required\[str\]\s*"""[\s\S]*?This value is either[\s\S]*?- a direct URL to the .*? file[\s\S]*?- `file_path` field from the response of the \[upload urls API\][\s\S]*?""")'
    else:
        # For regular classes, replace all file path documentation
        file_path_pattern = r'("""[\s\S]*?This value is either[\s\S]*?- a direct URL to the .*? file[\s\S]*?- `file_path` field from the response of the \[upload urls API\][\s\S]*?""")'

    def replace_file_path_doc(match):
        original_text = match.group(1)

        if is_face_mappings_item:
            # For FaceMappingsItem, we need to handle the field declaration + docstring
            # The match includes "new_face: typing_extensions.Required[str]" + docstring
            return '''new_face: typing_extensions.Required[str]
    """
    The face image that will be used to replace the face in the `original_face`. This value is either
    - a direct URL to the image file
    - a path to a local file

    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour's storage, and will not be uploaded again.
    """'''
        else:
            # Regular handling for other classes
            # Extract the description before "This value is either"
            description_match = re.search(
                r'"""(.*?)This value is either', original_text, re.DOTALL
            )
            if description_match:
                description = description_match.group(1).strip()
            else:
                description = "The file path."

            # Determine if it's image or video based on service context
            # Extract the file path from the file name to understand the service
            import os

            filename = os.path.basename(file_path) if file_path else ""

            # Services that work with videos
            video_services = [
                "video_to_video",
                "image_to_video",
                "text_to_video",
                "lip_sync",
                "ai_talking_photo",
                "animation",
                "auto_subtitle_generator",
            ]

            # Check if this is a video service
            is_video_service = any(service in filename for service in video_services)

            # For video services, determine based on field name
            if is_video_service:
                # Check field name - some video services take image inputs
                field_name = re.search(r"(\w+_file_path):", original_text)
                if field_name:
                    field = field_name.group(1)
                    if "image" in field or "photo" in field:
                        file_type = "image"
                    else:
                        file_type = "video"
                else:
                    file_type = "video"  # default for video services
            else:
                # For image services, always use image
                file_type = "image"

            return f'"""\n    {description} This value is either\n    - a direct URL to the {file_type} file\n    - a path to a local file\n\n    Note: if the path begins with `api-assets`, it will be assumed to already be uploaded to Magic Hour\'s storage, and will not be uploaded again.\n    """'

    # Apply the replacement
    content = re.sub(file_path_pattern, replace_file_path_doc, content, flags=re.DOTALL)

    # Note: Import fixing is handled in the process_file function, not here
    # since imports are at the file level, not class level

    return content


def find_create_body_assets_classes(file_path: str) -> List[str]:
    """Find all CreateBodyAssets class names in a file."""
    with open(file_path, "r") as f:
        content = f.read()

    # Find all class names that end with CreateBodyAssets (including FaceMappingsItem)
    pattern = r"class (\w+CreateBodyAssets\w*)\(typing_extensions\.TypedDict\):"
    matches = re.findall(pattern, content)
    return matches


def get_generate_file_path(create_file_path: str) -> str:
    """Convert a create_body_assets file path to a generate_body_assets file path."""
    # Always create separate generate files, including for face mapping items
    return create_file_path.replace("_create_body_assets", "_generate_body_assets")


def file_needs_update(file_path: str) -> bool:
    """Check if a file needs GenerateBodyAssets files created or updated."""
    create_classes = find_create_body_assets_classes(file_path)
    if not create_classes:
        return False

    # Check if the corresponding generate file exists or needs updating
    generate_file_path = get_generate_file_path(file_path)

    # If generate file doesn't exist, we need to create it
    if not os.path.exists(generate_file_path):
        return True

    # If generate file exists, check if it's older than the create file
    create_mtime = os.path.getmtime(file_path)
    generate_mtime = os.path.getmtime(generate_file_path)

    # Return True if create file is newer (needs update)
    return create_mtime > generate_mtime


def create_generate_file_content(create_file_path: str) -> str:
    """Create the content for a new generate_body_assets file."""
    with open(create_file_path, "r") as f:
        content = f.read()

    # Start with the imports from the original file
    imports_end = content.find("\nclass ")
    if imports_end == -1:
        imports_end = content.find("class ")

    imports_section = content[:imports_end].strip()

    # Check for face mapping imports before any replacements
    has_face_mappings = "FaceMappingsItem" in content
    is_not_face_mapping_file = "face_mappings_item" not in create_file_path
    has_face_mapping_import = (
        "_create_body_assets_face_mappings_item import" in imports_section
    )

    # For regular face swap files, update imports to reference generate versions
    if has_face_mappings and is_not_face_mapping_file and has_face_mapping_import:
        # Add generate imports alongside create imports
        face_mapping_import_pattern = r"(from \.v1_\w+_create_body_assets_face_mappings_item import \(\s*)([\s\S]*?)(\s*\))"

        def update_import(match):
            prefix = match.group(1)
            import_content = match.group(2)
            suffix = match.group(3)

            # Change import path to generate version
            prefix = prefix.replace(
                "_create_body_assets_face_mappings_item",
                "_generate_body_assets_face_mappings_item",
            )

            # Update class names to Generate versions
            lines = [
                line.strip() for line in import_content.split("\n") if line.strip()
            ]
            new_lines = []
            for line in lines:
                # Only update the main class, not the serializer
                if not line.startswith("_Serializer"):
                    new_line = line.replace(
                        "CreateBodyAssetsFaceMappingsItem",
                        "GenerateBodyAssetsFaceMappingsItem",
                    )
                else:
                    # For serializer, we don't need it in generate files since it's for API calls
                    continue
                new_lines.append(new_line)

            new_import_content = "\n    ".join(new_lines)
            return prefix + new_import_content + suffix

        imports_section = re.sub(
            face_mapping_import_pattern, update_import, imports_section, flags=re.DOTALL
        )

    # Find all CreateBodyAssets classes and convert them
    create_classes = find_create_body_assets_classes(create_file_path)
    generate_classes = []

    for class_name in create_classes:
        try:
            # Extract the CreateBodyAssets class
            create_class = extract_create_body_assets_class(content, class_name)

            # Generate the GenerateBodyAssets class
            generate_class = generate_generate_body_assets_class(
                create_class, create_file_path
            )
            generate_classes.append(generate_class)

        except Exception as e:
            print(f"    Error processing {class_name}: {e}")
            continue

    # Construct the new file content
    new_content = imports_section + "\n\n\n"
    for i, generate_class in enumerate(generate_classes):
        if i > 0:
            new_content += "\n\n\n"
        new_content += generate_class

    new_content += "\n"

    return new_content


def process_file(file_path: str, dry_run: bool = True, verbose: bool = True) -> bool:
    """Process a single file to create GenerateBodyAssets files."""

    if verbose:
        print(f"\nProcessing file: {file_path}")

    # Find all CreateBodyAssets classes in this file
    create_classes = find_create_body_assets_classes(file_path)

    if not create_classes:
        if verbose:
            print("  No CreateBodyAssets classes found")
        return False

    if verbose:
        print(f"  Found CreateBodyAssets classes: {create_classes}")

    # Get the generate file path
    generate_file_path = get_generate_file_path(file_path)

    # All files are processed the same way - create separate generate files
    return process_regular_file(file_path, generate_file_path, dry_run, verbose)


# Removed process_face_mapping_file function since all files are now processed the same way


def process_regular_file(
    file_path: str, generate_file_path: str, dry_run: bool = True, verbose: bool = True
) -> bool:
    """Process a regular file by creating a new generate file."""

    if verbose:
        print(f"  Will create new file: {os.path.basename(generate_file_path)}")

    try:
        # Create the content for the new generate file
        new_content = create_generate_file_content(file_path)

        if not dry_run:
            # Write the new file
            with open(generate_file_path, "w") as f:
                f.write(new_content)
            if verbose:
                print(f"  ✅ Created new file: {os.path.basename(generate_file_path)}")
        elif verbose:
            print(
                f"  📋 Ready to create: {os.path.basename(generate_file_path)} (dry run mode)"
            )

        return True

    except Exception as e:
        if verbose:
            print(f"  ❌ Error creating generate file: {e}")
        return False


def find_all_create_body_assets_files(params_dir: str) -> List[str]:
    """Find all files that contain CreateBodyAssets classes."""
    # Include both regular create_body_assets files and face_mappings_item files
    pattern1 = os.path.join(params_dir, "*create_body_assets.py")
    pattern2 = os.path.join(params_dir, "*create_body_assets_face_mappings_item.py")

    files = glob.glob(pattern1) + glob.glob(pattern2)
    return sorted(list(set(files)))  # Remove duplicates and sort


def main():
    """Main function to process files."""
    parser = argparse.ArgumentParser(
        description="Generate GenerateBodyAssets classes from CreateBodyAssets classes"
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply changes to files (default is dry run)",
    )
    parser.add_argument("--file", type=str, help="Process specific file only")
    parser.add_argument(
        "--check", action="store_true", help="Only check which files need updates"
    )
    parser.add_argument("--quiet", action="store_true", help="Minimal output")

    args = parser.parse_args()

    dry_run = not args.apply
    verbose = not args.quiet

    if args.check:
        dry_run = True
        if verbose:
            print("CHECKING which files need updates...")
    elif dry_run and verbose:
        print("DRY RUN MODE - No files will be modified")
        print("Use --apply to actually modify files")
    elif verbose:
        print("APPLYING CHANGES TO FILES")

    # Determine which files to process
    params_dir = "/Users/dhu/Desktop/coding/sdks/python/magic_hour/types/params"

    if args.file:
        if not os.path.exists(args.file):
            print(f"Error: File {args.file} does not exist")
            return 1
        files_to_process = [args.file]
    else:
        files_to_process = find_all_create_body_assets_files(params_dir)

    if verbose:
        print(f"\nFound {len(files_to_process)} potential files to process:")
        for file_path in files_to_process:
            print(f"  {os.path.basename(file_path)}")

    # Process each file
    total_files_changed = 0
    files_needing_update = []

    for file_path in files_to_process:
        if args.check:
            if file_needs_update(file_path):
                files_needing_update.append(file_path)
                if verbose:
                    print(f"  {os.path.basename(file_path)} needs updates")
        else:
            if process_file(file_path, dry_run, verbose):
                total_files_changed += 1

    if verbose:
        print(f"\n{'=' * 60}")

    if args.check:
        if files_needing_update:
            print(f"Files needing updates: {len(files_needing_update)}")
            if not verbose:
                for file_path in files_needing_update:
                    print(f"  {os.path.basename(file_path)}")
            return 1  # Exit code 1 indicates updates needed
        else:
            print("All files are up to date!")
            return 0
    else:
        print(
            f"Summary: {total_files_changed} files {'would be' if dry_run else 'were'} processed"
        )

        if dry_run and total_files_changed > 0 and verbose:
            print("\nTo create all generate files, run:")
            print("python codemod/generate_asset_types.py --apply")

    return 0


if __name__ == "__main__":
    sys.exit(main())
