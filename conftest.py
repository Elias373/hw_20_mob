import pytest
from selene import browser
from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.config import config
import allure
import requests


def get_browserstack_video(session_id):
    try:
        url = f"https://api.browserstack.com/app-automate/sessions/{session_id}.json"
        response = requests.get(url, auth=(config.bstack_username, config.bstack_access_key))
        return response.json().get('automation_session', {}).get('video_url') if response.status_code == 200 else None
    except:
        return None


@pytest.fixture(scope='function')
def mobile_management():
    options = UiAutomator2Options()

    if config.context == 'bstack':
        options.set_capability('platformName', config.platform_name)
        options.set_capability('platformVersion', config.platform_version)
        options.set_capability('deviceName', config.device_name)
        options.set_capability('app', config.app)
        options.set_capability('appPackage', config.app_package)
        options.set_capability('appActivity', config.app_activity)
        options.set_capability('bstack:options', {
            "userName": config.bstack_username,
            "accessKey": config.bstack_access_key,
            "video": True
        })
    else:
        options.platform_name = config.platform_name
        options.device_name = config.device_name
        options.app_package = config.app_package
        options.app_activity = config.app_activity

    browser.config.driver = webdriver.Remote(config.remote_url, options=options)
    browser.config.timeout = 10

    yield

    if config.context == 'bstack':
        video_url = get_browserstack_video(browser.driver.session_id)
        if video_url:
            allure.attach(
                f'<video controls><source src="{video_url}"></video>',
                name="Video",
                attachment_type=allure.attachment_type.HTML
            )

    browser.quit()