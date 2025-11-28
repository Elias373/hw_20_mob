import os
from pydantic import Field
from pydantic_settings import BaseSettings
from typing import Optional


class BaseConfig(BaseSettings):



    remote_url: str = Field(default="http://localhost:4723", env='REMOTE_URL')


    platform_name: str = Field(default="Android", env='PLATFORM_NAME')
    device_name: str = Field(default="emulator-5554", env='DEVICE_NAME')
    automation_name: str = Field(default='UiAutomator2', env='AUTOMATION_NAME')


    app: Optional[str] = Field(None, env='APP')
    app_package: Optional[str] = Field(default="org.wikipedia.alpha", env='APP_PACKAGE')
    app_activity: Optional[str] = Field(default="org.wikipedia.main.MainActivity", env='APP_ACTIVITY')


    bstack_userName: Optional[str] = Field(None, env='BSTACK_USERNAME')
    bstack_accessKey: Optional[str] = Field(None, env='BSTACK_ACCESS_KEY')

    class Config:
        case_sensitive = False


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