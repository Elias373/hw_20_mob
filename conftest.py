import pytest
from selene import browser
from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.config import config
import allure
import time


@pytest.fixture(scope='function')
def mobile_management(request):
    print(f"🚀 Запускаем тест на {config.context}")

    options = UiAutomator2Options()
    session_id = None

    if config.context == 'bstack':
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
            "sessionName": "Wikipedia Onboarding Test",
            "video": True,
            "networkLogs": True
        })

    print("🔗 Создаем WebDriver...")

    try:
        browser.config.driver = webdriver.Remote(
            command_executor=config.remote_url,
            options=options
        )
        session_id = browser.driver.session_id
        print(f"✅ WebDriver создан! Session ID: {session_id}")


        if config.context == 'bstack' and session_id:
            bs_url = f"https://app-automate.browserstack.com/dashboard/v2/builds/sessions/{session_id}"
            allure.dynamic.link(bs_url, name="🎥 BrowserStack Session")


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