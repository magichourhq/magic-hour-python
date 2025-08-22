#!/usr/bin/env python3
"""
Script to automatically populate custom docs sections in README files.

This script extracts the generate workflow documentation from ai_clothes_changer/README.md
and populates it into other README files that have generate methods but empty custom docs sections.
"""

import re
from pathlib import Path
from typing import List


class CustomDocsPopulator:
    def __init__(self, v1_resources_dir: Path):
        self.v1_resources_dir = v1_resources_dir
        self.source_readme = v1_resources_dir / "ai_clothes_changer" / "README.md"
        self.custom_docs_content = self._extract_custom_docs()

    def _extract_custom_docs(self) -> str:
        """Extract the custom docs section from ai_clothes_changer README."""
        with open(self.source_readme, "r") as f:
            content = f.read()

        # Find the custom docs section
        start_pattern = r"<!-- CUSTOM DOCS START -->"
        end_pattern = r"<!-- CUSTOM DOCS END -->"

        start_match = re.search(start_pattern, content)
        end_match = re.search(end_pattern, content)

        if not start_match or not end_match:
            raise ValueError("Could not find custom docs section in source README")

        # Extract content between the markers
        start_pos = start_match.end()
        end_pos = end_match.start()

        return content[start_pos:end_pos].strip()

    def _get_resource_name_from_path(self, readme_path: Path) -> str:
        """Extract resource name from README path."""
        return readme_path.parent.name

    def _customize_docs_for_resource(self, content: str, resource_name: str) -> str:
        """Customize the docs content for a specific resource."""
        # Find the create function code samples
        lines = content.split("\n")

        print(f"🔍 Processing {resource_name}, total lines: {len(lines)}")

        # Find the sync create function
        create_sync_start = -1
        create_sync_end = -1
        create_async_start = -1
        create_async_end = -1

        for i, line in enumerate(lines):
            # Look for create function calls
            if f"client.v1.{resource_name}.create(" in line:
                print(f"📍 Found create function at line {i}: '{line.strip()}'")
                if create_sync_start == -1:
                    create_sync_start = i
                    print("   -> Set as sync start")
                elif create_async_start == -1:
                    create_async_start = i
                    print("   -> Set as async start")
            # Look for closing parenthesis at the end of function calls
            elif (
                create_sync_start != -1
                and line.strip() == ")"
                and create_sync_end == -1
            ):
                create_sync_end = i
                print(f"📍 Found sync end at line {i}: '{line.strip()}'")
            elif (
                create_async_start != -1
                and line.strip() == ")"
                and create_async_end == -1
            ):
                create_async_end = i
                print(f"📍 Found async end at line {i}: '{line.strip()}'")

        if create_sync_start == -1 or create_async_start == -1:
            # Fallback to the original approach if we can't find the create samples
            print(f"❌ Could not find create function samples for {resource_name}")
            return self._fallback_customization(content, resource_name)

        # Extract the create function parameter sections
        create_sync_params = "\n".join(lines[create_sync_start:create_sync_end])
        create_async_params = "\n".join(lines[create_async_start:create_async_end])

        print(f"📋 Extracted sync params for {resource_name}:")
        print(repr(create_sync_params))
        print(f"📋 Extracted async params for {resource_name}:")
        print(repr(create_async_params))

        # Add generate-specific parameters
        generate_params = ''' wait_for_completion=True,
    download_outputs=True,
    download_directory="outputs"'''

        # Create the new generate function calls
        sync_generate_call = create_sync_params.replace(
            f"client.v1.{resource_name}.create(", f"client.v1.{resource_name}.generate("
        )
        sync_generate_call = sync_generate_call + f"\n    {generate_params}\n)"

        async_generate_call = create_async_params.replace(
            f"client.v1.{resource_name}.create(", f"client.v1.{resource_name}.generate("
        )
        async_generate_call = async_generate_call + f"\n    {generate_params}\n)"

        # Create the full custom docs content manually with proper formatting
        resource_title = resource_name.replace("_", " ").title()
        custom_docs_content = f"""### {resource_title} Generate Workflow <a name="generate"></a>

The workflow performs the following action

1. upload local assets to Magic Hour storage. So you can pass in a local path instead of having to upload files yourself
2. trigger a generation
3. poll for a completion status. This is configurable
4. if success, download the output to local directory

> [!TIP]
> This is the recommended way to use the SDK unless you have specific needs where it is necessary to split up the actions.

#### Parameters

In Additional to the parameters listed in the `.create` section below, `.generate` introduces 3 new parameters:

- `wait_for_completion` (bool, default True): Whether to wait for the project to complete.
- `download_outputs` (bool, default True): Whether to download the generated files
- `download_directory` (str, optional): Directory to save downloaded files (defaults to current directory)

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
{sync_generate_call}
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
{async_generate_call}
```"""

        # Return the customized content - replacement will be handled by the caller
        return custom_docs_content

    def _fallback_customization(self, content: str, resource_name: str) -> str:
        """Fallback customization when create samples aren't found."""
        # This is the original approach as a fallback
        config = {
            "assets": {"file_path": "/path/to/input_file.png"},
            "name": f"{resource_name.replace('_', ' ').title()} result",
        }

        # Simple parameter list
        params: List[str] = []
        params.append('    assets={"file_path": "/path/to/input_file.png"},')
        params.append(f'    name="{config.get("name", "Generated content")}",')
        params.append("    wait_for_completion=True,")
        params.append("    download_outputs=True,")
        params.append('    download_directory="outputs",')

        params_str = "\n".join(params)

        # Replace method names
        content = content.replace(
            "client.v1.ai_clothes_changer.generate(",
            f"client.v1.{resource_name}.generate(",
        )
        content = content.replace(
            "client.v1.AsyncClient.ai_clothes_changer.generate(",
            f"client.v1.{resource_name}.generate(",
        )

        # Replace parameter blocks
        sync_pattern = r"client\.v1\." + resource_name + r"\.generate\(\s*\n.*?\n\)"
        sync_replacement = f"client.v1.{resource_name}.generate(\n{params_str}\n)"

        matches = list(re.finditer(sync_pattern, content, re.DOTALL))
        for i, match in enumerate(matches):
            if i == 0:  # First occurrence is sync
                content = (
                    content[: match.start()] + sync_replacement + content[match.end() :]
                )
            elif i == 1:  # Second occurrence is async
                content = (
                    content[: match.start()] + sync_replacement + content[match.end() :]
                )
                break

        # Customize the title
        resource_title = resource_name.replace("_", " ").title()
        content = content.replace(
            "AI Clothes Changer Generate Workflow",
            f"{resource_title} Generate Workflow",
        )
        content = content.replace(
            "Clothes Changer image", str(config.get("name", f"{resource_title} result"))
        )

        return content

    def _has_generate_method(self, resource_name: str) -> bool:
        """Check if a resource has a generate method by looking for client.py."""
        client_file = self.v1_resources_dir / resource_name / "client.py"
        if not client_file.exists():
            return False

        with open(client_file, "r") as f:
            content = f.read()

        return "def generate(" in content

    def _has_custom_docs_section(self, readme_path: Path) -> bool:
        """Check if README has a custom docs section."""
        with open(readme_path, "r") as f:
            content = f.read()

        return (
            "<!-- CUSTOM DOCS START -->" in content
            and "<!-- CUSTOM DOCS END -->" in content
        )

    def _is_custom_docs_empty(self, readme_path: Path) -> bool:
        """Check if the custom docs section is empty."""
        with open(readme_path, "r") as f:
            content = f.read()

        start_pattern = r"<!-- CUSTOM DOCS START -->"
        end_pattern = r"<!-- CUSTOM DOCS END -->"

        start_match = re.search(start_pattern, content)
        end_match = re.search(end_pattern, content)

        if not start_match or not end_match:
            return False

        start_pos = start_match.end()
        end_pos = end_match.start()

        section_content = content[start_pos:end_pos].strip()
        return len(section_content) == 0

    def populate_custom_docs(self, dry_run: bool = True) -> List[str]:
        """Populate custom docs sections for all eligible README files."""
        updated_files: List[str] = []

        # Find all README files in v1 resources
        for readme_path in self.v1_resources_dir.glob("*/README.md"):
            resource_name = self._get_resource_name_from_path(readme_path)

            # Skip if it's the source file
            if resource_name == "ai_clothes_changer":
                continue

            # Skip if it doesn't have a generate method
            if not self._has_generate_method(resource_name):
                continue

            # Skip if it doesn't have custom docs section or if it's not empty
            if not self._has_custom_docs_section(
                readme_path
            ) or not self._is_custom_docs_empty(readme_path):
                continue

            print(f"📝 Processing {resource_name}...")

            # Read the target file content to extract create function samples
            with open(readme_path, "r") as f:
                target_content = f.read()

            # Customize the docs for this resource
            customized_content = self._customize_docs_for_resource(
                target_content, resource_name
            )

            if not dry_run:
                # Replace the empty custom docs section
                with open(readme_path, "r") as f:
                    original_content = f.read()

                # Only replace empty custom docs sections (sections with only whitespace between markers)
                pattern = r"<!-- CUSTOM DOCS START -->\s*<!-- CUSTOM DOCS END -->"
                replacement = f"<!-- CUSTOM DOCS START -->\n\n{customized_content}\n\n<!-- CUSTOM DOCS END -->"

                updated_content = re.sub(
                    pattern, replacement, original_content, count=1
                )

                with open(readme_path, "w") as f:
                    f.write(updated_content)

                updated_files.append(str(readme_path))
                print(f"✅ Updated {readme_path}")
            else:
                updated_files.append(str(readme_path))
                print(f"🔍 Would update {readme_path}")

        return updated_files


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Populate custom docs sections in README files"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be updated without making changes",
    )
    parser.add_argument(
        "--apply", action="store_true", help="Actually apply the changes"
    )

    args = parser.parse_args()

    if not args.dry_run and not args.apply:
        print("Please specify either --dry-run or --apply")
        return

    v1_resources_dir = Path("magic_hour/resources/v1")

    if not v1_resources_dir.exists():
        print(f"Error: {v1_resources_dir} does not exist")
        return

    populator = CustomDocsPopulator(v1_resources_dir)

    print("🔍 Extracting custom docs template from ai_clothes_changer...")
    print(f"📄 Template length: {len(populator.custom_docs_content)} characters")

    updated_files = populator.populate_custom_docs(dry_run=args.dry_run)

    if args.dry_run:
        print(f"\n📋 Dry run complete. Would update {len(updated_files)} files:")
        for file in updated_files:
            print(f"  - {file}")
    else:
        print(f"\n✅ Updated {len(updated_files)} files:")
        for file in updated_files:
            print(f"  - {file}")


if __name__ == "__main__":
    main()
