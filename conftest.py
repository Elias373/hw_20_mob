import pytest
from selene import browser
from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.config import config
import allure
import time


@pytest.fixture(scope='function')
def mobile_management():
    print(f"🚀 Запускаем тест на {config.context}")
    print(f"📱 Подключаемся к: {config.remote_url}")
    print(f"📟 Устройство: {config.device_name}")

    options = UiAutomator2Options()

    if config.context == 'bstack':
        # BrowserStack capabilities
        options.set_capability('platformName', config.platform_name)
        options.set_capability('platformVersion', config.platform_version)
        options.set_capability('deviceName', config.device_name)
        options.set_capability('app', config.app)
        options.set_capability('appPackage', config.app_package)
        options.set_capability('appActivity', config.app_activity)
        options.set_capability('automationName', config.automation_name)
        options.set_capability('bstack:options', {
            "userName": config.bstack_username,
            "accessKey": config.bstack_access_key,
            "projectName": "Wikipedia Android Tests",
            "buildName": "Wikipedia Build",
            "sessionName": "Wikipedia Onboarding Test"
        })
    else:
        # Local capabilities - БЕЗ APP!
        options.platform_name = config.platform_name
        options.device_name = config.device_name
        options.app_package = config.app_package
        options.app_activity = config.app_activity
        options.automation_name = config.automation_name

    print("🔗 Создаем WebDriver...")

    try:
        browser.config.driver = webdriver.Remote(
            command_executor=config.remote_url,
            options=options
        )
        print("✅ WebDriver создан успешно!")
    except Exception as e:
        print(f"❌ Ошибка создания WebDriver: {e}")
        raise

    browser.config.timeout = 10
    time.sleep(5)

    yield

    if browser.driver:
        try:
            browser.quit()
            print("✅ Браузер закрыт")
        except:
            print("⚠️ Ошибка при закрытии браузера")