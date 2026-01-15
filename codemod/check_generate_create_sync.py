#!/usr/bin/env python3
"""
Script to check that generate() and create() methods have matching parameters.

WHAT IT DOES:
- Finds all client files with both generate() and create() methods
- Compares parameters between the two methods
- Reports any parameters in create() that are missing from generate()
- Ignores parameters specific to generate() (wait_for_completion, download_outputs, etc.)
- Ignores 'assets' parameter (handled differently in generate vs create)

WHEN TO RUN:
- After SDK regeneration to catch new parameters
- In CI/CD pipeline to prevent parameter drift

USAGE:
    python codemod/check_generate_create_sync.py           # Check all files
    python codemod/check_generate_create_sync.py --fix     # Show what needs to be added

EXIT CODES:
    0 - All generate methods are in sync with create methods
    1 - Some generate methods are missing parameters from create
"""

import os
import re
import glob
import sys
import argparse
from typing import List, Set, Tuple, Optional


# Parameters that are specific to generate() and should not be in create()
GENERATE_ONLY_PARAMS = {
    "wait_for_completion",
    "download_outputs",
    "download_directory",
}

# Parameters to ignore when comparing (handled differently)
IGNORED_PARAMS = {
    "assets",  # Different types between generate and create
    "request_options",  # Should be in both, but handled separately
}


def extract_method_params(content: str, method_name: str) -> Optional[Set[str]]:
    """
    Extract parameter names from a method definition.

    Returns:
        Set of parameter names, or None if method not found
    """
    # Pattern to find the method definition and its parameters
    # Handles both sync and async methods
    pattern = rf"(?:async\s+)?def\s+{method_name}\s*\(\s*self\s*,\s*\*\s*,([^)]+)\)"

    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return None

    params_block = match.group(1)

    # Extract parameter names (before the colon)
    param_pattern = r"(\w+)\s*:"
    params = set(re.findall(param_pattern, params_block))

    return params


def find_client_files_with_generate(base_dir: str) -> List[str]:
    """Find all client.py files that have a generate method."""
    pattern = os.path.join(base_dir, "magic_hour/resources/v1/*/client.py")
    files = glob.glob(pattern)

    result = []
    for file_path in files:
        with open(file_path, "r") as f:
            content = f.read()
        if "def generate(" in content:
            result.append(file_path)

    return sorted(result)


def check_file(file_path: str, verbose: bool = True) -> Tuple[bool, List[str]]:
    """
    Check a single client file for parameter mismatches.

    Returns:
        Tuple of (is_in_sync, list_of_missing_params)
    """
    with open(file_path, "r") as f:
        content = f.read()

    # Extract parameters from both methods
    generate_params = extract_method_params(content, "generate")
    create_params = extract_method_params(content, "create")

    if generate_params is None:
        if verbose:
            print(f"  Warning: No generate() method found in {file_path}")
        return True, []

    if create_params is None:
        if verbose:
            print(f"  Warning: No create() method found in {file_path}")
        return True, []

    # Find params in create that should also be in generate
    # Exclude generate-only params and ignored params
    create_params_to_check = create_params - GENERATE_ONLY_PARAMS - IGNORED_PARAMS
    generate_params_to_check = generate_params - GENERATE_ONLY_PARAMS - IGNORED_PARAMS

    missing_in_generate = create_params_to_check - generate_params_to_check

    return len(missing_in_generate) == 0, sorted(missing_in_generate)


def get_resource_name(file_path: str) -> str:
    """Extract the resource name from a file path."""
    # e.g., .../v1/ai_talking_photo/client.py -> ai_talking_photo
    parts = file_path.split("/")
    for i, part in enumerate(parts):
        if part == "v1" and i + 1 < len(parts):
            return parts[i + 1]
    return os.path.basename(os.path.dirname(file_path))


def main():
    parser = argparse.ArgumentParser(
        description="Check that generate() and create() methods have matching parameters"
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Show detailed information about what needs to be fixed",
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
        is_in_sync, missing_params = check_file(file_path, verbose=False)

        if not is_in_sync:
            all_in_sync = False
            issues.append((resource_name, file_path, missing_params))
            if verbose:
                print(f"MISMATCH: {resource_name}")
                print(f"  File: {file_path}")
                print(f"  Missing in generate(): {', '.join(missing_params)}")
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
        for resource_name, file_path, missing_params in issues:
            print(f"  {resource_name}:")
            print(f"    Missing: {', '.join(missing_params)}")
            if args.fix:
                print(f"    File: {file_path}")
                print(
                    f"    Action: Add these parameters to the generate() method signature"
                )
                print(f"            and forward them to self.create(...)")
            print()

        if not args.fix:
            print("Run with --fix for more details on how to resolve.")

        return 1


if __name__ == "__main__":
    sys.exit(main())
