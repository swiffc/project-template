#!/usr/bin/env python3
"""Development environment setup and management script."""

import os
import subprocess
import sys
from pathlib import Path


def setup_environment() -> None:
    """Set up development environment."""
    print("Setting up development environment...")

    # Create virtual environment if it doesn't exist
    if not Path(".venv").exists():
        print("Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", ".venv"])

    # Activate virtual environment and install dependencies
    if os.name == "nt":  # Windows
        pip_path = ".venv/Scripts/pip"
    else:  # Unix/Linux/MacOS
        pip_path = ".venv/bin/pip"

    # Install dependencies
    print("Installing dependencies...")
    subprocess.run([pip_path, "install", "-r", "requirements.txt"])

    # Set up pre-commit hooks
    print("Setting up pre-commit hooks...")
    subprocess.run([pip_path, "install", "pre-commit"])
    subprocess.run(["pre-commit", "install"])

    print("Development environment setup complete!")


def run_tests() -> None:
    """Run test suite."""
    print("Running tests...")
    subprocess.run(["pytest", "-v"])


def run_linting() -> None:
    """Run code linting."""
    print("Running linting...")
    subprocess.run(["flake8", "src"])
    subprocess.run(["mypy", "src"])
    subprocess.run(["black", "--check", "src"])
    subprocess.run(["isort", "--check-only", "src"])


def run_consistency_check() -> None:
    """Run codebase consistency validation."""
    print("Running consistency validation...")
    result = subprocess.run([sys.executable, "scripts/validate_consistency.py"])
    if result.returncode != 0:
        print("\nConsistency validation failed!")
        print("Please fix the issues before continuing.")
        sys.exit(1)
    print("Consistency validation passed!")


def run_security_check() -> None:
    """Run security checks."""
    print("Running security checks...")
    subprocess.run(["bandit", "-r", "src"])
    subprocess.run(["safety", "check"])


def run_performance_check() -> None:
    """Run performance checks."""
    print("Running performance checks...")
    # Add performance testing commands here
    pass


def run_accessibility_check() -> None:
    """Run accessibility checks."""
    print("Running accessibility checks...")
    # Add accessibility testing commands here
    pass


def run_all_checks() -> None:
    """Run all development checks."""
    print("Running all development checks...")

    # Run checks in order of importance
    run_consistency_check()
    run_security_check()
    run_linting()
    run_tests()
    run_performance_check()
    run_accessibility_check()

    print("\nAll checks completed successfully!")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/dev.py [setup|test|lint|consistency|all]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "setup":
        setup_environment()
    elif command == "test":
        run_tests()
    elif command == "lint":
        run_linting()
    elif command == "consistency":
        run_consistency_check()
    elif command == "security":
        run_security_check()
    elif command == "performance":
        run_performance_check()
    elif command == "accessibility":
        run_accessibility_check()
    elif command == "all":
        run_all_checks()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
