"""Configuration system for AI Brain — Australia.

Priority: env vars > config file (~/.ailawfirm-australia/config.json) > defaults.
"""

import json
import os
from pathlib import Path

DEFAULT_CONFIG_DIR = os.path.expanduser("~/.ailawfirm-australia")
DEFAULT_CALENDAR_DIR = os.path.join(DEFAULT_CONFIG_DIR, "calendars")
DEFAULT_AI_PROVIDER = "ollama"
DEFAULT_OLLAMA_HOST = "http://localhost:11434"
DEFAULT_OLLAMA_MODEL = "qwen3:14b"
DEFAULT_TIMEZONE = "Australia/Sydney"


class AILawFirmAustraliaConfig:
    """Configuration manager for AI Brain — Australia."""

    def __init__(self, config_dir=None):
        self._config_dir = Path(config_dir) if config_dir else Path(DEFAULT_CONFIG_DIR)
        self._config_file = self._config_dir / "config.json"
        self._file_config = {}

        if self._config_file.exists():
            try:
                with open(self._config_file, "r") as f:
                    self._file_config = json.load(f)
            except (json.JSONDecodeError, OSError):
                self._file_config = {}

    @property
    def config_dir(self):
        return str(self._config_dir)

    @property
    def calendar_dir(self):
        env_val = os.environ.get("AILAWFIRM_AUS_CALENDAR_DIR")
        if env_val:
            return env_val
        return self._file_config.get("calendar_dir", DEFAULT_CALENDAR_DIR)

    @property
    def ai_provider(self):
        env_val = os.environ.get("AILAWFIRM_AUS_AI_PROVIDER")
        if env_val:
            return env_val
        return self._file_config.get("ai_provider", DEFAULT_AI_PROVIDER)

    @property
    def ollama_host(self):
        return self._file_config.get("ollama_host", DEFAULT_OLLAMA_HOST)

    @property
    def ollama_model(self):
        return self._file_config.get("ollama_model", DEFAULT_OLLAMA_MODEL)

    @property
    def timezone(self):
        env_val = os.environ.get("AILAWFIRM_AUS_TIMEZONE")
        if env_val:
            return env_val
        return self._file_config.get("timezone", DEFAULT_TIMEZONE)

    @property
    def cloud_warning_acknowledged(self):
        return self._file_config.get("cloud_warning_acknowledged", False)

    def init(self):
        """Create config directory and write default config.json."""
        self._config_dir.mkdir(parents=True, exist_ok=True)
        default_config = {
            "ai_provider": DEFAULT_AI_PROVIDER,
            "ollama_host": DEFAULT_OLLAMA_HOST,
            "ollama_model": DEFAULT_OLLAMA_MODEL,
            "timezone": DEFAULT_TIMEZONE,
            "calendar_dir": DEFAULT_CALENDAR_DIR,
            "cloud_warning_acknowledged": False,
        }
        if not self._config_file.exists():
            with open(self._config_file, "w") as f:
                json.dump(default_config, f, indent=2)
        return self._config_file
