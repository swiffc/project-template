"""Script to fix trailing whitespace and newline issues."""

import os


def fix_file(file_path: str) -> None:
    """Fix trailing whitespace and newline issues in a file.

    Args:
        file_path: Path to the file to fix
    """
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Remove trailing whitespace from each line
    lines = [line.rstrip() for line in lines]

    # Remove blank lines at the end
    while lines and lines[-1] == "":
        lines.pop()

    # Ensure file ends with exactly one newline
    lines.append("")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main() -> None:
    """Run the script."""
    files = [
        "src/__init__.py",
        "src/core/__init__.py",
        "src/core/module.py",
        "src/modules/__init__.py",
    ]

    for file_path in files:
        if os.path.exists(file_path):
            fix_file(file_path)
            print(f"Fixed {file_path}")


if __name__ == "__main__":
    main()
