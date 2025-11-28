import os
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class BaseConfig(BaseSettings):
    """Базовая конфигурация с Pydantic"""

    # Remote configuration
    remote_url: str = Field(default="http://localhost:4723")

    # Device configuration
    platform_name: str = Field(default="Android")
    device_name: str = Field(default="emulator-5554")
    automation_name: str = Field(default='UiAutomator2')

    # App configuration
    app: Optional[str] = Field(None)
    app_package: Optional[str] = Field(default="org.wikipedia.alpha")
    app_activity: Optional[str] = Field(default="org.wikipedia.main.MainActivity")

    # BrowserStack credentials (из .env.credentials)
    bstack_userName: Optional[str] = Field(None)
    bstack_accessKey: Optional[str] = Field(None)

    model_config = SettingsConfigDict(
        env_file='.env.credentials',  # Загружаем из .env.credentials
        case_sensitive=False,
        extra='ignore'
    )


class Config:
    def __init__(self, context: str = "local_emulator"):
        self.context = context
        self._load_config()

    def _load_config(self):
        # Сначала загружаем credentials
        if os.path.exists('.env.credentials'):
            credentials_config = BaseConfig()
        else:
            credentials_config = BaseConfig()

        # Затем загружаем контекстный конфиг
        context_env_file = f".env.{self.context}"
        if os.path.exists(context_env_file):
            context_config = BaseConfig(_env_file=context_env_file)
        else:
            context_config = BaseConfig()

        # Объединяем конфигурации (приоритет у контекстных значений)
        for field in BaseConfig.model_fields:
            context_value = getattr(context_config, field)
            creds_value = getattr(credentials_config, field)
            base_value = getattr(BaseConfig(), field)

            final_value = context_value if context_value is not None else (
                creds_value if creds_value is not None else base_value
            )
            setattr(self, field, final_value)