"""Module interface and base classes for the cursor development system."""

import logging
from abc import ABC, abstractmethod

from .core_types import ExecutionContext, ModuleResult


class ModuleInterface(ABC):
    """Standard interface contract for all modules."""

    @abstractmethod
    def validate(self, context: ExecutionContext) -> bool:
        """Validate module can execute with given context."""
        pass

    @abstractmethod
    def execute(self, context: ExecutionContext) -> ModuleResult:
        """Execute module functionality."""
        pass

    @abstractmethod
    def cleanup(self, context: ExecutionContext) -> None:
        """Clean up resources after execution."""
        pass


class BaseModule(ABC):
    """Base class for all modules."""

    def __init__(self, name: str, description: str) -> None:
        """Initialize base module.

        Args:
            name: Module name
            description: Module description
        """
        self.name = name
        self.description = description
        self.logger = logging.getLogger(name)

    def log_info(self, message: str) -> None:
        """Log info message.

        Args:
            message: Message to log
        """
        self.logger.info(message)

    def log_error(self, message: str) -> None:
        """Log error message.

        Args:
            message: Message to log
        """
        self.logger.error(message)

    def log_warning(self, message: str) -> None:
        """Log warning message.

        Args:
            message: Message to log
        """
        self.logger.warning(message)

    def log_debug(self, message: str) -> None:
        """Log debug message.

        Args:
            message: Message to log
        """
        self.logger.debug(message)

    def validate(self, context: ExecutionContext) -> bool:
        """Validate module can execute.

        Args:
            context: Execution context

        Returns:
            True if validation passes, False otherwise
        """
        return True

    @abstractmethod
    def execute(self, context: ExecutionContext) -> ModuleResult:
        """Execute module.

        Args:
            context: Execution context

        Returns:
            Module execution result
        """
        pass

    def cleanup(self, context: ExecutionContext) -> None:
        """Clean up module resources."""
        pass
