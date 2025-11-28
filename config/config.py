from pydantic import BaseModel
import os
from typing import Optional


class Config(BaseModel):
    context: str = "local_emulator"
    platform_name: str = "Android"
    device_name: str = "emulator-5554"
    app_package: str = "org.wikipedia.alpha"
    app_activity: str = "org.wikipedia.main.MainActivity"
    automation_name: str = "UiAutomator2"
    remote_url: str = "http://localhost:4723"
    bstack_username: Optional[str] = None
    bstack_access_key: Optional[str] = None
    platform_version: Optional[str] = None
    app: Optional[str] = None


def load_config():
    # Сначала пробуем загрузить из .env.credentials (для локальной работы)
    try:
        from dotenv import load_dotenv
        load_dotenv('.env.credentials')
    except:
        pass

    # Берем credentials из переменных окружения ИЛИ из файла
    bstack_username = os.getenv('BSTACK_USERNAME')
    bstack_access_key = os.getenv('BSTACK_ACCESS_KEY')

    # Определяем контекст
    context = os.getenv('CONTEXT', 'local_emulator')

    # Загружаем конфиг для контекста
    try:
        from dotenv import load_dotenv
        env_file = f'.env.{context}'
        if os.path.exists(env_file):
            load_dotenv(env_file)
    except:
        pass

    return Config(
        context=context,  # Важно: используем вычисленный context!
        platform_name=os.getenv('PLATFORM_NAME', 'Android'),
        device_name=os.getenv('DEVICE_NAME', 'emulator-5554'),
        app_package=os.getenv('APP_PACKAGE', 'org.wikipedia.alpha'),
        app_activity=os.getenv('APP_ACTIVITY', 'org.wikipedia.main.MainActivity'),
        automation_name=os.getenv('AUTOMATION_NAME', 'UiAutomator2'),
        remote_url=os.getenv('REMOTE_URL', 'http://localhost:4723'),
        bstack_username=bstack_username,
        bstack_access_key=bstack_access_key,
        platform_version=os.getenv('PLATFORM_VERSION'),
        app=os.getenv('APP')
    )


config = load_config()