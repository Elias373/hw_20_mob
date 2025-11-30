import pytest
from selene import browser
from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.config import config
import allure
import time
import requests
import os


@pytest.fixture(scope='function')
def mobile_management(request):
    print(f"🚀 Запускаем тест на {config.context}")
    print(f"📱 Подключаемся к: {config.remote_url}")
    print(f"📟 Устройство: {config.device_name}")

    options = UiAutomator2Options()
    session_id = None

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
            "sessionName": "Wikipedia Onboarding Test",
            "video": True,  # Включаем запись видео
            "networkLogs": True
        })
    else:
        # Local capabilities
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
        session_id = browser.driver.session_id
        print(f"✅ WebDriver создан успешно! Session ID: {session_id}")
    except Exception as e:
        print(f"❌ Ошибка создания WebDriver: {e}")
        raise

    browser.config.timeout = 10
    time.sleep(5)

    yield


    if config.context == 'bstack' and session_id:
        try:
            video_url = get_browserstack_video(session_id)
            if video_url:

                allure.attach(
                    f'<video width="100%" controls><source src="{video_url}" type="video/mp4"></video>',
                    name=f"Video_{session_id}",
                    attachment_type=allure.attachment_type.HTML
                )
                print(f"🎥 Видео прикреплено к отчету: {video_url}")
        except Exception as e:
            print(f"⚠️ Не удалось прикрепить видео: {e}")

    if browser.driver:
        try:
            browser.quit()
            print("✅ Браузер закрыт")
        except:
            print("⚠️ Ошибка при закрытии браузера")


def get_browserstack_video(session_id):

    try:
        url = f"https://api.browserstack.com/app-automate/sessions/{session_id}.json"
        auth = (config.bstack_username, config.bstack_access_key)

        response = requests.get(url, auth=auth)
        if response.status_code == 200:
            data = response.json()
            return data.get('automation_session', {}).get('video_url')
        else:
            print(f"❌ Ошибка получения видео: {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ Ошибка при запросе видео: {e}")
        return None