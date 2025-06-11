"""Core system types and enums for the cursor development system."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Dict, Optional


class ProjectType(str, Enum):
    """Project types supported by the system."""

    REACT_SPA = "react-spa"
    NEXTJS_FULLSTACK = "nextjs-fullstack"
    VUE_NUXT = "vue-nuxt"
    EXPRESS_API = "express-api"
    FASTAPI_BACKEND = "fastapi-backend"
    ELECTRON_DESKTOP = "electron-desktop"
    REACT_NATIVE = "react-native"
    FLUTTER_MOBILE = "flutter-mobile"
    PYTHON_AUTOMATION = "python-automation"
    WINDOWS_AUTOMATION = "windows-automation"
    CAD_AUTOMATION = "cad-automation"
    AI_ML_PROJECT = "ai-ml-project"
    STATIC_WEBSITE = "static-website"


class ExecutionPhase(Enum):
    """Development execution phases."""

    ANALYSIS = "analysis"
    INFRASTRUCTURE = "infrastructure"
    TEMPLATES = "templates"
    VALIDATION = "validation"
    INTEGRATION = "integration"
    DEPLOYMENT = "deployment"


class LogLevel(Enum):
    """Logging levels."""

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


@dataclass
class SystemConfig:
    """System configuration."""

    version: str = "2.0.0"
    name: str = "Cursor Development System"
    base_dir: Path = field(default_factory=lambda: Path(__file__).parent)

    # Directory structure
    core_dir: Path = field(init=False)
    modules_dir: Path = field(init=False)
    templates_dir: Path = field(init=False)
    validators_dir: Path = field(init=False)
    integrations_dir: Path = field(init=False)
    utilities_dir: Path = field(init=False)
    config_dir: Path = field(init=False)
    logs_dir: Path = field(init=False)

    # Execution settings
    timeout_seconds: int = 300
    retry_attempts: int = 3
    fail_fast: bool = True

    def __post_init__(self) -> None:
        """Initialize directory paths."""
        self.core_dir = self.base_dir / "core"
        self.modules_dir = self.base_dir / "modules"
        self.templates_dir = self.base_dir / "templates"
        self.validators_dir = self.base_dir / "validators"
        self.integrations_dir = self.base_dir / "integrations"
        self.utilities_dir = self.base_dir / "utilities"
        self.config_dir = self.base_dir / "config"
        self.logs_dir = self.base_dir / "logs"


@dataclass
class ExecutionContext:
    """Context for project execution."""

    project_name: str
    project_type: ProjectType
    output_path: Optional[Path] = None
    execution_id: str = field(
        default_factory=lambda: datetime.now().strftime("%Y%m%d_%H%M%S")
    )
    advanced_mode: bool = False
    github_integration: bool = False
    skip_install: bool = False
    template_variant: str = "default"
    config_override: Optional[Path] = None

    # Runtime state
    current_phase: Optional[ExecutionPhase] = None

    @property
    def project_root(self) -> Path:
        """Get project root directory."""
        if self.output_path:
            return self.output_path / self.project_name
        return Path(self.project_name)


@dataclass
class ModuleResult:
    """Result of module execution."""

    module_name: str
    success: bool
    message: str
    data: Optional[Dict[str, Any]] = None
    execution_time: float = 0.0
    error: Optional[Exception] = None
