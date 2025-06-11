#!/usr/bin/env python3
"""Project structure and code consistency validation script.

Enforces the rules defined in .cursor/rules/codebase_consistency.mdc and .cursor/rules/development_standards.mdc
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Pattern


class ConsistencyValidator:
    """Validates project structure and code consistency."""

    def __init__(self) -> None:
        """Initialize the validator."""
        self.project_root = Path.cwd()
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def validate_structure(self) -> bool:
        """Validate project structure."""
        print("Validating project structure...")

        # Check required directories
        required_dirs = ["src", "tests", "docs", "config", ".cursor"]

        for dir_name in required_dirs:
            if not (self.project_root / dir_name).exists():
                self.errors.append(f"Required directory '{dir_name}' is missing")
                return False

        # Check required files
        required_files = ["README.md", ".gitignore", ".env.example", "requirements.txt"]

        for file_name in required_files:
            if not (self.project_root / file_name).exists():
                self.errors.append(f"Required file '{file_name}' is missing")
                return False

        print("Project structure validation complete!")
        return True

    def validate_naming_conventions(self) -> bool:
        """Validate file and directory naming conventions."""
        print("Validating naming conventions...")

        # Define patterns for different file types
        component_patterns: Dict[Pattern[str], str] = {
            re.compile(
                r"^[A-Z][a-zA-Z0-9]*\.(tsx|jsx)$"
            ): "React components should be PascalCase",
            re.compile(
                r"^[a-z][a-zA-Z0-9]*\.(ts|js)$"
            ): "Utility files should be camelCase",
            re.compile(
                r"^[a-z][a-zA-Z0-9_]*\.py$"
            ): "Python files should be snake_case",
        }

        utility_patterns: Dict[Pattern[str], str] = {
            re.compile(
                r"^[a-z][a-zA-Z0-9]*\.(ts|js)$"
            ): "Utility files should be camelCase",
            re.compile(
                r"^[a-z][a-zA-Z0-9_]*\.py$"
            ): "Python files should be snake_case",
        }

        api_patterns: Dict[Pattern[str], str] = {
            re.compile(
                r"^[a-z][a-zA-Z0-9_]*\.(ts|js)$"
            ): "API files should be camelCase",
            re.compile(r"^[a-z][a-zA-Z0-9_]*\.py$"): "API files should be snake_case",
        }

        # Check source files
        source_files: List[Path] = list(self.project_root.rglob("*.py"))
        source_files.extend(self.project_root.rglob("*.ts"))
        source_files.extend(self.project_root.rglob("*.tsx"))
        source_files.extend(self.project_root.rglob("*.js"))
        source_files.extend(self.project_root.rglob("*.jsx"))

        for file_path in source_files:
            relative_path = file_path.relative_to(self.project_root)
            file_name = file_path.name

            # Skip files in certain directories
            if any(part.startswith(".") for part in relative_path.parts):
                continue

            # Check component files
            if "components" in str(relative_path):
                for pattern, message in component_patterns.items():
                    if not pattern.match(file_name):
                        self.errors.append(f"{relative_path}: {message}")

            # Check utility files
            elif "utils" in str(relative_path):
                for pattern, message in utility_patterns.items():
                    if not pattern.match(file_name):
                        self.errors.append(f"{relative_path}: {message}")

            # Check API files
            elif "api" in str(relative_path):
                for pattern, message in api_patterns.items():
                    if not pattern.match(file_name):
                        self.errors.append(f"{relative_path}: {message}")

        return len(self.errors) == 0

    def validate_imports(self) -> bool:
        """Validate import statements."""
        print("Validating imports...")

        # Define import patterns
        patterns = {
            r"^from \.\. import": "Use absolute imports instead of relative",
            r"^from \. import": "Use absolute imports instead of relative",
        }

        # Check Python files
        for file_path in self.project_root.rglob("*.py"):
            if any(
                part.startswith(".")
                for part in file_path.relative_to(self.project_root).parts
            ):
                continue

            with open(file_path, "r", encoding="utf-8") as f:
                for i, line in enumerate(f, 1):
                    for pattern, message in patterns.items():
                        if re.match(pattern, line.strip()):
                            self.errors.append(f"{file_path}:{i}: {message}")

        return len(self.errors) == 0

    def validate_docstrings(self) -> bool:
        """Validate docstring formatting."""
        print("Validating docstrings...")

        # Define docstring patterns
        patterns = {
            r'"""[^"]*\.$': "Docstring should end with a period",
            r'"""[^"]*[A-Z][^"]*$': "Docstring should not end with a capital letter",
        }

        # Check Python files
        for file_path in self.project_root.rglob("*.py"):
            if any(
                part.startswith(".")
                for part in file_path.relative_to(self.project_root).parts
            ):
                continue

            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                for pattern, message in patterns.items():
                    if re.search(pattern, content):
                        self.errors.append(f"{file_path}: {message}")

        return len(self.errors) == 0

    def validate_type_hints(self) -> bool:
        """Validate type hints."""
        print("Validating type hints...")

        # Check Python files
        for file_path in self.project_root.rglob("*.py"):
            if any(
                part.startswith(".")
                for part in file_path.relative_to(self.project_root).parts
            ):
                continue

            with open(file_path, "r", encoding="utf-8") as f:
                for i, line in enumerate(f, 1):
                    if line.strip().startswith("def "):
                        if "->" not in line:
                            self.errors.append(
                                f"{file_path}:{i}: Function missing return type annotation"
                            )

        return len(self.errors) == 0

    def validate_error_handling(self) -> bool:
        """Validate error handling."""
        print("Validating error handling...")

        # Check Python files
        for file_path in self.project_root.rglob("*.py"):
            if any(
                part.startswith(".")
                for part in file_path.relative_to(self.project_root).parts
            ):
                continue

            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                if "try:" in content and "except:" in content:
                    self.warnings.append(f"{file_path}: Bare except clause detected")

        return len(self.errors) == 0

    def validate_comments(self) -> bool:
        """Validate comment formatting."""
        print("Validating comments...")

        # Check Python files
        for file_path in self.project_root.rglob("*.py"):
            if any(
                part.startswith(".")
                for part in file_path.relative_to(self.project_root).parts
            ):
                continue

            with open(file_path, "r", encoding="utf-8") as f:
                for i, line in enumerate(f, 1):
                    if line.strip().startswith("#"):
                        if not line.strip().startswith("# "):
                            self.warnings.append(
                                f"{file_path}:{i}: Comment should start with '# '"
                            )

        return len(self.errors) == 0

    def validate_line_length(self) -> bool:
        """Validate line length."""
        print("Validating line length...")

        # Check Python files
        for file_path in self.project_root.rglob("*.py"):
            if any(
                part.startswith(".")
                for part in file_path.relative_to(self.project_root).parts
            ):
                continue

            with open(file_path, "r", encoding="utf-8") as f:
                for i, line in enumerate(f, 1):
                    if len(line.rstrip()) > 88:
                        self.warnings.append(
                            f"{file_path}:{i}: Line too long ({len(line.rstrip())} > 88)"
                        )

        return len(self.errors) == 0

    def validate_whitespace(self) -> bool:
        """Validate whitespace usage."""
        print("Validating whitespace...")

        # Check Python files
        for file_path in self.project_root.rglob("*.py"):
            if any(
                part.startswith(".")
                for part in file_path.relative_to(self.project_root).parts
            ):
                continue

            with open(file_path, "r", encoding="utf-8") as f:
                for i, line in enumerate(f, 1):
                    if line.rstrip().endswith(" "):
                        self.warnings.append(f"{file_path}:{i}: Trailing whitespace")

        return len(self.errors) == 0

    def validate_newlines(self) -> bool:
        """Validate newline usage."""
        print("Validating newlines...")

        # Check Python files
        for file_path in self.project_root.rglob("*.py"):
            if any(
                part.startswith(".")
                for part in file_path.relative_to(self.project_root).parts
            ):
                continue

            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                if not content.endswith("\n"):
                    self.warnings.append(f"{file_path}: File should end with a newline")

        return len(self.errors) == 0

    def validate_all(self) -> bool:
        """Run all validation checks."""
        checks = [
            self.validate_structure,
            self.validate_naming_conventions,
            self.validate_imports,
            self.validate_docstrings,
            self.validate_type_hints,
            self.validate_error_handling,
            self.validate_comments,
            self.validate_line_length,
            self.validate_whitespace,
            self.validate_newlines,
        ]

        for check in checks:
            if not check():
                return False

        return True

    def print_results(self) -> None:
        """Print validation results."""
        if self.errors:
            print("\nErrors:")
            for error in self.errors:
                print(f"  - {error}")

        if self.warnings:
            print("\nWarnings:")
            for warning in self.warnings:
                print(f"  - {warning}")

        if not self.errors and not self.warnings:
            print("\nAll checks passed!")


def main() -> None:
    """Run the main validation process."""
    validator = ConsistencyValidator()
    if validator.validate_all():
        validator.print_results()
        sys.exit(0)
    else:
        validator.print_results()
        sys.exit(1)


if __name__ == "__main__":
    main()
