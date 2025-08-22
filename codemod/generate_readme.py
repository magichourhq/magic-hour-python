import re
from pathlib import Path
from typing import Callable, List

# -------------------------------
# Transformation functions
# -------------------------------


def update_file_path(section: str) -> str:
    """Append note that file_path can be local or URL."""
    return re.sub(
        r"(_file_path.*?)(\n\s+The image.*?)",
        r"\1\n    This can be either a local file path or a URL.\2",
        section,
        flags=re.DOTALL,
    )


def replace_create_with_generate(section: str) -> str:
    """Replace any `.create(` calls with `.generate(`"""
    return section.replace(".create(", ".generate(")


def add_extra_params(section: str) -> str:
    """Add wait_for_completion, download_outputs, download_directory to client examples."""

    def add_params(match: re.Match) -> str:
        code_block = match.group(0)
        insertion = (
            "    wait_for_completion=True,\n"
            "    download_outputs=True,\n"
            "    download_directory=None,\n"
        )
        return code_block.replace(")", f"{insertion})")

    return re.sub(r"client\.v1\.[a-z_]+\.[a-z_]+\([^)]*\)", add_params, section)


# -------------------------------
# Core functions
# -------------------------------


def extract_section(text: str) -> str:
    """Extract the first ### <Resource> section."""
    pattern = r"(### [^\n]+[\s\S]*?)(?=\n### |\Z)"
    match = re.search(pattern, text)
    return match.group(1) if match else None


def apply_transformations(section: str, transforms: List[Callable[[str], str]]) -> str:
    for transform in transforms:
        section = transform(section)
    return section


def replace_custom_docs(text: str, new_content: str) -> str:
    """Replace the CUSTOM_DOCS section in README."""
    pattern = r"<!-- CUSTOM DOCS START -->[\s\S]*?<!-- CUSTOM DOCS END -->"
    replacement = f"<!-- CUSTOM DOCS START -->\n{new_content}\n<!-- CUSTOM DOCS END -->"
    return re.sub(pattern, replacement, text, count=1)


def process_readme(path: Path, transforms: List[Callable[[str], str]]) -> None:
    text = path.read_text()
    section = extract_section(text)
    if not section:
        print(f"⚠️ No section found in {path}")
        return
    updated = apply_transformations(section, transforms)
    final_text = replace_custom_docs(text, updated)

    print(final_text)
    path.write_text(final_text)
    print(f"✅ Updated custom docs in {path}")


# -------------------------------
# Automation across all v1 READMEs
# -------------------------------

README_DIR = Path("magic_hour/resources/v1")
DEFAULT_TRANSFORMS = [
    update_file_path,
    replace_create_with_generate,
    add_extra_params,
]


def main():
    for readme_path in README_DIR.glob("*/README.md"):
        process_readme(readme_path, DEFAULT_TRANSFORMS)


if __name__ == "__main__":
    main()
