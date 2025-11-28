import os
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class BaseConfig(BaseSettings):
    remote_url: str = Field(default="http://localhost:4723")
    platform_name: str = Field(default="Android")
    device_name: str = Field(default="emulator-5554")
    automation_name: str = Field(default='UiAutomator2')
    app: Optional[str] = Field(None)
    app_package: Optional[str] = Field(default="org.wikipedia.alpha")
    app_activity: Optional[str] = Field(default="org.wikipedia.main.MainActivity")
    bstack_userName: Optional[str] = Field(None)
    bstack_accessKey: Optional[str] = Field(None)

    model_config = SettingsConfigDict(
        env_file='.env.credentials',
        case_sensitive=False,
        extra='ignore'
    )


class Config:
    def __init__(self, context: str = "local_emulator"):
        self.context = context
        self._load_config()

    def _load_config(self):
        context_env_file = f".env.{self.context}"
        if os.path.exists(context_env_file):
            config = BaseConfig(_env_file=context_env_file)
        else:
            config = BaseConfig()

        for field in BaseConfig.model_fields:
            setattr(self, field, getattr(config, field))