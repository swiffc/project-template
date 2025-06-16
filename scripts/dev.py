#!/usr/bin/env python3
"""Development environment setup and management script."""

import os
import subprocess
import sys
from pathlib import Path

from src.core.env_manager import EnvManager


def setup_environment() -> None:
    """Set up development environment."""
    print("Setting up development environment...")

    # Initialize environment manager
    env_manager = EnvManager()
    env_manager.load_global_env()

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


def run_consistency_check() -> None:
    """Run codebase consistency validation."""
    print("Running consistency validation...")
    result = subprocess.run([sys.executable, "scripts/validate_consistency.py"])
    if result.returncode != 0:
        print("Consistency validation failed!")
        sys.exit(1)


def run_security_check() -> None:
    """Run security checks."""
    print("Running security checks...")
    subprocess.run(["bandit", "-r", "src"])


def run_performance_check() -> None:
    """Run performance checks."""
    print("Running performance checks...")
    subprocess.run(["pytest", "--durations=0"])


def run_accessibility_check() -> None:
    """Run accessibility checks."""
    print("Running accessibility checks...")
    subprocess.run(["pa11y", "http://localhost:3000"])


def run_all_checks() -> None:
    """Run all checks."""
    run_tests()
    run_linting()
    run_consistency_check()
    run_security_check()
    run_performance_check()
    run_accessibility_check()


def run_dev_server() -> None:
    """Run development server."""
    print("Starting development server...")
    # Load environment variables
    env_manager = EnvManager()
    env_manager.load_global_env()

    # Start the server
    subprocess.run(["python", "src/main.py", "run-dev"])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/dev.py [setup|test|lint|consistency|all|run-dev]")
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
    elif command == "run-dev":
        run_dev_server()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
