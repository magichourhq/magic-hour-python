#!/usr/bin/env python3
"""
Script to check that generate() and create() methods have matching parameters.

WHAT IT DOES:
- Finds all client files with both generate() and create() methods
- Checks both sync and async client classes within each file
- Compares parameters between the two methods for each client type
- Reports any parameters in create() that are missing from generate()
- Ignores parameters specific to generate() (wait_for_completion, download_outputs, etc.)
- Ignores 'assets' parameter (handled differently in generate vs create)
- Ensures trailing params are always last in correct order

WHEN TO RUN:
- After SDK regeneration to catch new parameters
- In CI/CD pipeline to prevent parameter drift

USAGE:
    python codemod/check_generate_create_sync.py           # Check all files
    python codemod/check_generate_create_sync.py --fix     # Automatically fix all issues

EXIT CODES:
    0 - All generate methods are in sync with create methods
    1 - Some generate methods are missing parameters from create

IMPLEMENTATION OVERVIEW:
1. extract_method_params: Extracts parameter names from a method
2. extract_param_definitions: Extracts full parameter definitions (with types)
3. extract_all_generate_params: Categorizes params as regular vs trailing
4. check_file: Checks for parameter mismatches
5. fix_generate_method: Adds missing params to generate() and forwards to create()
   - _update_generate_signature: Updates method signature with correct param order
   - _update_create_call: Updates self.create() call to include new params
"""

import os
import re
import glob
import sys
import argparse
from typing import List, Set, Tuple, Optional


# Parameters that are specific to generate() and should not be in create()
# These should always be at the end of generate() method signatures, in this order
GENERATE_ONLY_PARAMS = {
    "wait_for_completion",
    "download_outputs",
    "download_directory",
}

# The order these params should appear at the end of generate()
GENERATE_PARAMS_ORDER = [
    "wait_for_completion",
    "download_outputs",
    "download_directory",
    "request_options",
]

# Parameters to ignore when comparing (handled differently)
IGNORED_PARAMS = {
    "assets",  # Different types between generate and create
    "request_options",  # Should be in both, but handled separately
}


def extract_method_params(
    content: str, method_name: str, class_name: Optional[str] = None
) -> Optional[Set[str]]:
    """
    Extract parameter names from a method definition.

    Args:
        content: File content to search
        method_name: Name of the method to find
        class_name: Optional class name to search within

    Returns:
        Set of parameter names, or None if method not found
    """
    # If class_name is provided, extract just that class's content
    if class_name:
        class_pattern = rf"class\s+{class_name}\s*[:\(].*?(?=\nclass\s|\Z)"
        class_match = re.search(class_pattern, content, re.DOTALL)
        if not class_match:
            return None
        content = class_match.group(0)

    # Pattern to find the method definition and its parameters
    # Handles both sync and async methods
    pattern = rf"(?:async\s+)?def\s+{method_name}\s*\(\s*self\s*,\s*\*\s*,([^)]+)\)"

    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return None

    params_block = match.group(1)

    # Extract parameter names (before the colon)
    # Match word followed by colon, but only at the start of a line or after comma/whitespace
    # This avoids matching literal strings like "16:9"
    param_pattern = r"(?:^|,)\s*(\w+)\s*:"
    params = set(re.findall(param_pattern, params_block, re.MULTILINE))

    return params


def extract_param_definitions(
    content: str, method_name: str, class_name: Optional[str], param_names: Set[str]
) -> dict[str, str]:
    """
    Extract full parameter definitions (with type hints and defaults) from a method.

    Args:
        content: File content to search
        method_name: Name of the method to find
        class_name: Optional class name to search within
        param_names: Set of parameter names to extract

    Returns:
        Dictionary mapping parameter name to its full definition
        Example: {"model": "model: typing.Union[...] = type_utils.NOT_GIVEN"}
    """
    if class_name:
        class_pattern = rf"class\s+{class_name}\s*[:\(].*?(?=\nclass\s|\Z)"
        class_match = re.search(class_pattern, content, re.DOTALL)
        if not class_match:
            return {}
        content = class_match.group(0)

    # Find method - handle both with and without return type annotations
    pattern = (
        rf"(?:async\s+)?def\s+{method_name}\s*\(\s*self\s*,\s*\*\s*,(.+?)\)\s*(?:->|:)"
    )
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return {}

    params_block = match.group(1)
    definitions = {}

    for param_name in param_names:
        param_start = re.search(rf"\b{param_name}\s*:", params_block)
        if not param_start:
            continue

        # Scan forward to find the end of this parameter
        # We need to track bracket/paren depth to handle nested types
        start_pos = param_start.start()
        pos = param_start.end()
        bracket_depth = 0
        paren_depth = 0

        while pos < len(params_block):
            char = params_block[pos]

            if char == "[":
                bracket_depth += 1
            elif char == "]":
                bracket_depth -= 1
            elif char == "(":
                paren_depth += 1
            elif char == ")":
                paren_depth -= 1
            elif char == "," and bracket_depth == 0 and paren_depth == 0:
                break

            pos += 1

        param_def = params_block[start_pos:pos].strip()
        definitions[param_name] = param_def

    return definitions


def extract_class_names(content: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Extract sync and async client class names from file content.

    Returns:
        Tuple of (sync_class_name, async_class_name)
    """
    # Find class names - typically like "AiClothesChangerClient" and "AsyncAiClothesChangerClient"
    class_pattern = r"class\s+(\w*Client)\s*[:\(]"
    class_matches = re.findall(class_pattern, content)

    sync_class = None
    async_class = None

    for class_name in class_matches:
        if class_name.startswith("Async"):
            async_class = class_name
        else:
            sync_class = class_name

    return sync_class, async_class


def find_client_files_with_generate(base_dir: str) -> List[str]:
    """Find all client.py files that have a generate method."""
    pattern = os.path.join(base_dir, "magic_hour/resources/v1/*/client.py")
    files = glob.glob(pattern)

    result = []
    for file_path in files:
        with open(file_path, "r") as f:
            content = f.read()
        # Check for both sync and async generate methods
        if "def generate(" in content or "async def generate(" in content:
            result.append(file_path)

    return sorted(result)


def check_file(
    file_path: str, verbose: bool = True
) -> Tuple[bool, List[Tuple[str, List[str]]]]:
    """
    Check a single client file for parameter mismatches in both sync and async clients.

    Args:
        file_path: Path to the client file to check
        verbose: Whether to print verbose output (unused currently)

    Returns:
        Tuple of (is_in_sync, list_of_issues)
        where each issue is (client_type, missing_params)
    """
    with open(file_path, "r") as f:
        content = f.read()

    sync_class, async_class = extract_class_names(content)
    issues = []

    # Check both sync and async clients
    for client_type, class_name in [("sync", sync_class), ("async", async_class)]:
        if not class_name:
            continue

        generate_params = extract_method_params(content, "generate", class_name)
        create_params = extract_method_params(content, "create", class_name)

        if generate_params and create_params:
            create_params_to_check = (
                create_params - GENERATE_ONLY_PARAMS - IGNORED_PARAMS
            )
            generate_params_to_check = (
                generate_params - GENERATE_ONLY_PARAMS - IGNORED_PARAMS
            )
            missing_in_generate = create_params_to_check - generate_params_to_check

            if missing_in_generate:
                issues.append((client_type, sorted(missing_in_generate)))

    return len(issues) == 0, issues


def get_resource_name(file_path: str) -> str:
    """Extract the resource name from a file path."""
    # e.g., .../v1/ai_talking_photo/client.py -> ai_talking_photo
    parts = file_path.split("/")
    for i, part in enumerate(parts):
        if part == "v1" and i + 1 < len(parts):
            return parts[i + 1]
    return os.path.basename(os.path.dirname(file_path))


def extract_all_generate_params(content: str, class_name: str) -> dict:
    """
    Extract all parameters from generate() method, categorized by type.

    Args:
        content: File content
        class_name: Name of the client class

    Returns:
        Dictionary with keys:
        - 'regular': List of regular parameter names
        - 'trailing': List of trailing parameter names (wait_for_completion, etc.)
        - 'definitions': Dict mapping parameter name to full definition
    """
    class_pattern = rf"class\s+{class_name}\s*[:\(].*?(?=\nclass\s|\Z)"
    class_match = re.search(class_pattern, content, re.DOTALL)
    if not class_match:
        return {}

    class_content = class_match.group(0)
    is_async = "Async" in class_name
    async_keyword = "async " if is_async else ""

    pattern = rf"{async_keyword}def\s+generate\s*\(\s*self\s*,\s*\*\s*,(.+?)\)\s*:"
    match = re.search(pattern, class_content, re.DOTALL)
    if not match:
        return {}

    params_block = match.group(1)

    result = {
        "regular": [],
        "trailing": [],
        "definitions": {},
    }

    # Parse parameters by tracking bracket/paren depth
    pos = 0
    current_param_start = 0
    bracket_depth = 0
    paren_depth = 0

    while pos < len(params_block):
        char = params_block[pos]

        if char == "[":
            bracket_depth += 1
        elif char == "]":
            bracket_depth -= 1
        elif char == "(":
            paren_depth += 1
        elif char == ")":
            paren_depth -= 1
        elif char == "," and bracket_depth == 0 and paren_depth == 0:
            param_text = params_block[current_param_start:pos].strip()
            _categorize_param(param_text, result)
            current_param_start = pos + 1

        pos += 1

    # Handle last parameter
    param_text = params_block[current_param_start:].strip()
    _categorize_param(param_text, result)

    return result


def _categorize_param(param_text: str, result: dict) -> None:
    """Helper to categorize a parameter as regular or trailing."""
    if not param_text:
        return

    param_match = re.match(r"(\w+)\s*:", param_text)
    if param_match:
        param_name = param_match.group(1)
        result["definitions"][param_name] = param_text

        if param_name in GENERATE_PARAMS_ORDER:
            result["trailing"].append(param_name)
        else:
            result["regular"].append(param_name)


def fix_generate_method(
    content: str, class_name: str, missing_params: List[str]
) -> str:
    """
    Add missing parameters to generate() method and forward them to create() call.

    Ensures trailing params are always last in correct order:
    1. wait_for_completion
    2. download_outputs
    3. download_directory
    4. request_options

    Args:
        content: File content
        class_name: Name of the client class (e.g., "AsyncAiGifGeneratorClient")
        missing_params: List of parameter names to add

    Returns:
        Updated file content with fixed generate() method
    """
    # Extract the class content
    class_pattern = rf"class\s+{class_name}\s*[:\(].*?(?=\nclass\s|\Z)"
    class_match = re.search(class_pattern, content, re.DOTALL)
    if not class_match:
        return content

    class_content = class_match.group(0)
    class_start = class_match.start()

    # Get full parameter definitions from create method
    param_defs = extract_param_definitions(
        class_content, "create", None, set(missing_params)
    )
    if not param_defs:
        return content

    # Extract current generate parameters and categorize them
    current_params = extract_all_generate_params(content, class_name)
    if not current_params:
        return content

    # Update the generate() method signature
    updated_class_content = _update_generate_signature(
        class_content, class_name, current_params, param_defs, missing_params
    )

    # Update the self.create() call to include new parameters
    updated_class_content = _update_create_call(updated_class_content, missing_params)

    # Replace in full content
    return (
        content[:class_start]
        + updated_class_content
        + content[class_start + len(class_content) :]
    )


def _update_generate_signature(
    class_content: str,
    class_name: str,
    current_params: dict,
    param_defs: dict,
    missing_params: List[str],
) -> str:
    """Update the generate() method signature with missing parameters."""
    is_async = "Async" in class_name
    async_keyword = "async " if is_async else ""

    generate_pattern = (
        rf"({async_keyword}def\s+generate\s*\(\s*self\s*,\s*\*\s*,)(.+?)(\):)"
    )
    generate_match = re.search(generate_pattern, class_content, re.DOTALL)
    if not generate_match:
        return class_content

    # Build complete list of regular params (excluding trailing params)
    all_regular_params = current_params["regular"] + [
        p for p in missing_params if p not in GENERATE_PARAMS_ORDER
    ]
    # Remove duplicates while preserving order
    all_regular_params = list(dict.fromkeys(all_regular_params))

    # Merge all parameter definitions
    all_definitions = {**current_params["definitions"], **param_defs}

    # Build trailing params in correct order
    trailing_params = [
        p
        for p in GENERATE_PARAMS_ORDER
        if p in current_params["trailing"] or p in all_definitions
    ]

    # Build new params section
    new_params_lines = []
    for param in all_regular_params:
        if param in all_definitions:
            new_params_lines.append(f"        {all_definitions[param]},")

    for param in trailing_params:
        if param in all_definitions:
            new_params_lines.append(f"        {all_definitions[param]},")

    new_params_section = "\n".join(new_params_lines)
    if new_params_section:
        new_params_section = "\n" + new_params_section + "\n    "
    else:
        new_params_section = "\n    "

    # Build and return updated signature
    new_signature = (
        f"{generate_match.group(1)}{new_params_section}{generate_match.group(3)}"
    )
    return (
        class_content[: generate_match.start()]
        + new_signature
        + class_content[generate_match.end() :]
    )


def _update_create_call(class_content: str, missing_params: List[str]) -> str:
    """Update the self.create() call to include missing parameters."""
    create_call_pattern = r"((?:await\s+)?self\.create\s*\(\s*)(.*?)(\s*\))"
    create_call_match = re.search(create_call_pattern, class_content, re.DOTALL)

    if not create_call_match:
        return class_content

    existing_args = create_call_match.group(2).strip()

    # Parse existing arguments - split by comma while tracking bracket/paren depth
    arg_parts = []
    current_part = ""
    paren_depth = 0
    bracket_depth = 0

    for char in existing_args:
        if char == "(":
            paren_depth += 1
        elif char == ")":
            paren_depth -= 1
        elif char == "[":
            bracket_depth += 1
        elif char == "]":
            bracket_depth -= 1
        elif char == "," and paren_depth == 0 and bracket_depth == 0:
            arg_parts.append(current_part.strip())
            current_part = ""
            continue
        current_part += char

    if current_part.strip():
        arg_parts.append(current_part.strip())

    # Extract arg names and preserve the full argument text
    existing_args_dict = {}
    for part in arg_parts:
        arg_match = re.match(r"(\w+)\s*=", part)
        if arg_match:
            arg_name = arg_match.group(1)
            existing_args_dict[arg_name] = part

    # Build new args list - insert missing params before request_options
    new_args_list = []
    for arg_name, arg_text in existing_args_dict.items():
        if arg_name == "request_options":
            # Insert missing params before request_options
            for param in sorted(missing_params):
                if param not in existing_args_dict:
                    new_args_list.append(f"{param}={param}")
        new_args_list.append(arg_text)

    # If request_options not found, add missing params at the end
    if "request_options" not in existing_args_dict:
        for param in sorted(missing_params):
            if param not in existing_args_dict:
                new_args_list.append(f"{param}={param}")

    # Format the arguments
    if new_args_list:
        # group(1) already includes '\n            ' after '('
        # group(3) already includes '\n        ' before ')'
        updated_args = ",\n            ".join(new_args_list) + ","
    else:
        updated_args = ""

    new_create_call = (
        f"{create_call_match.group(1)}{updated_args}{create_call_match.group(3)}"
    )
    return (
        class_content[: create_call_match.start()]
        + new_create_call
        + class_content[create_call_match.end() :]
    )


def fix_file(file_path: str, issues: List[Tuple[str, List[str]]]) -> bool:
    """
    Fix parameter mismatches in a client file.

    Args:
        file_path: Path to the client file
        issues: List of (client_type, missing_params) tuples

    Returns:
        True if file was modified, False otherwise
    """
    with open(file_path, "r") as f:
        content = f.read()

    original_content = content
    sync_class, async_class = extract_class_names(content)

    for client_type, missing_params in issues:
        if client_type == "sync" and sync_class:
            content = fix_generate_method(content, sync_class, missing_params)
        elif client_type == "async" and async_class:
            content = fix_generate_method(content, async_class, missing_params)

    if content != original_content:
        with open(file_path, "w") as f:
            f.write(content)
        return True

    return False


def main():
    parser = argparse.ArgumentParser(
        description="Check that generate() and create() methods have matching parameters"
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Automatically fix parameter mismatches by updating generate() methods",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Only output errors",
    )

    args = parser.parse_args()
    verbose = not args.quiet

    base_dir = "."
    if not os.path.exists(os.path.join(base_dir, "magic_hour")):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    client_files = find_client_files_with_generate(base_dir)

    if verbose:
        print(f"Checking {len(client_files)} client files with generate() methods...\n")

    all_in_sync = True
    issues = []

    for file_path in client_files:
        resource_name = get_resource_name(file_path)
        is_in_sync, client_issues = check_file(file_path, verbose=False)

        if not is_in_sync:
            all_in_sync = False
            issues.append((resource_name, file_path, client_issues))
            if verbose:
                print(f"MISMATCH: {resource_name}")
                print(f"  File: {file_path}")
                for client_type, missing_params in client_issues:
                    print(
                        f"  {client_type} client - Missing in generate(): {', '.join(missing_params)}"
                    )
                print()
        elif verbose and not args.quiet:
            print(f"OK: {resource_name}")

    if verbose:
        print()
        print("=" * 60)

    if all_in_sync:
        if verbose:
            print("All generate() methods are in sync with create() methods!")
        return 0
    else:
        print(f"\nFound {len(issues)} file(s) with parameter mismatches:\n")

        if args.fix:
            print("Applying fixes...\n")
            fixed_count = 0
            for resource_name, file_path, client_issues in issues:
                print(f"  Fixing {resource_name}...")
                for client_type, missing_params in client_issues:
                    print(
                        f"    {client_type} client - Adding: {', '.join(missing_params)}"
                    )

                if fix_file(file_path, client_issues):
                    fixed_count += 1
                    print(f"    ✓ Fixed {file_path}")
                else:
                    print(f"    ✗ Failed to fix {file_path}")
                print()

            print(f"Fixed {fixed_count} of {len(issues)} file(s)")

            # Re-check to verify fixes
            print("\nRe-checking files...")
            all_fixed = True
            for resource_name, file_path, _ in issues:
                is_in_sync, remaining_issues = check_file(file_path, verbose=False)
                if not is_in_sync:
                    all_fixed = False
                    print(f"  {resource_name}: Still has issues")
                    for client_type, missing_params in remaining_issues:
                        print(
                            f"    {client_type} client - Still missing: {', '.join(missing_params)}"
                        )
                else:
                    print(f"  {resource_name}: ✓ All fixed")

            if all_fixed:
                print("\n✓ All issues resolved!")
                return 0
            else:
                print("\n✗ Some issues remain")
                return 1
        else:
            for resource_name, file_path, client_issues in issues:
                print(f"  {resource_name}:")
                for client_type, missing_params in client_issues:
                    print(
                        f"    {client_type} client - Missing: {', '.join(missing_params)}"
                    )
                print(f"    File: {file_path}")
                print()

            print("Run with --fix to automatically apply fixes.")
            return 1


if __name__ == "__main__":
    sys.exit(main())
