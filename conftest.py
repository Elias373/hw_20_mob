import pytest
from selene import browser
from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.config import config
import allure
import subprocess
import json
import time


def attach_bstack_video(session_id):

    time.sleep(5)

    url = f"https://api.browserstack.com/app-automate/sessions/{session_id}.json"
    auth = f"{config.bstack_username}:{config.bstack_access_key}"

    result = subprocess.run(['curl', '-u', auth, '-s', url], capture_output=True, text=True)

    if result.returncode == 0:
        video_url = json.loads(result.stdout).get('automation_session', {}).get('video_url')
        if video_url:
            subprocess.run(['curl', '-s', '-o', 'video.mp4', video_url])
            with open('video.mp4', 'rb') as f:
                allure.attach(f.read(), name="Video", attachment_type=allure.attachment_type.MP4)
            subprocess.run(['rm', 'video.mp4'])


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