"""Environment manager module for centralized environment configuration."""

import os
import shutil
from pathlib import Path
from typing import Dict, Optional

from dotenv import load_dotenv


class EnvManager:
    """Manages environment configuration across projects."""

    def __init__(self, base_dir: Optional[Path] = None) -> None:
        """Initialize environment manager.

        Args:
            base_dir: Base directory for environment files (defaults to user home)
        """
        self.base_dir = base_dir or Path.home() / ".cursor" / "env"
        self.env_file = self.base_dir / ".env"
        self._ensure_base_dir()

    def _ensure_base_dir(self) -> None:
        """Ensure base directory exists."""
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def load_global_env(self) -> None:
        """Load global environment variables."""
        if self.env_file.exists():
            load_dotenv(self.env_file)

    def save_global_env(self, env_vars: Dict[str, str]) -> None:
        """Save environment variables to global .env file.

        Args:
            env_vars: Dictionary of environment variables to save
        """
        # Read existing variables
        existing_vars = {}
        if self.env_file.exists():
            with open(self.env_file, "r", encoding="utf-8") as f:
                for line in f:
                    if "=" in line and not line.startswith("#"):
                        key, value = line.strip().split("=", 1)
                        existing_vars[key] = value

        # Update with new variables
        existing_vars.update(env_vars)

        # Write back to file
        with open(self.env_file, "w", encoding="utf-8") as f:
            for key, value in existing_vars.items():
                f.write(f"{key}={value}\n")

    def copy_to_project(self, project_dir: Path) -> None:
        """Copy global environment to project directory.

        Args:
            project_dir: Project directory to copy environment to
        """
        if not self.env_file.exists():
            return

        # Create .env.example in project
        example_file = project_dir / ".env.example"
        with open(self.env_file, "r", encoding="utf-8") as src, open(
            example_file, "w", encoding="utf-8"
        ) as dst:
            for line in src:
                if "=" in line and not line.startswith("#"):
                    key, _ = line.strip().split("=", 1)
                    dst.write(f"{key}=your_{key.lower()}_here\n")
                else:
                    dst.write(line)

        # Copy actual .env if it doesn't exist
        project_env = project_dir / ".env"
        if not project_env.exists():
            shutil.copy2(self.env_file, project_env)

    def get_env_value(self, key: str, default: Optional[str] = None) -> Optional[str]:
        """Get environment variable value.

        Args:
            key: Environment variable key
            default: Default value if not found

        Returns:
            Environment variable value or default
        """
        return os.environ.get(key, default)

    def set_env_value(self, key: str, value: str) -> None:
        """Set environment variable value.

        Args:
            key: Environment variable key
            value: Environment variable value
        """
        os.environ[key] = value
        self.save_global_env({key: value})
