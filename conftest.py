import pytest
from selene import browser
from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.config import config
import allure
import urllib.request
import base64
import json
import time


def attach_bstack_video(session_id):
    time.sleep(5)
    url = f"https://api.browserstack.com/app-automate/sessions/{session_id}.json"
    auth = base64.b64encode(f"{config.bstack_username}:{config.bstack_access_key}".encode()).decode()

    req = urllib.request.Request(url)
    req.add_header('Authorization', f'Basic {auth}')

    with urllib.request.urlopen(req) as response:
        video_url = json.loads(response.read().decode()).get('automation_session', {}).get('video_url')
        if video_url:
            with urllib.request.urlopen(video_url) as video_response:
                allure.attach(video_response.read(), name="Video", attachment_type=allure.attachment_type.MP4)


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

    browser.config.driver = webdriver.Remote(config.remote_url, options=options)
    browser.config.timeout = 10

    yield

    if config.context == 'bstack':
        attach_bstack_video(browser.driver.session_id)

    browser.quit()