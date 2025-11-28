import pytest
from selene.support.shared import browser
from appium import webdriver
from appium.options.android import UiAutomator2Options
from config import Config


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        action="store",
        default="local_emulator",
        help="Context for test configuration: local_emulator, local_real, bstack"
    )


@pytest.fixture(scope="session")
def config(request):
    context = request.config.getoption("--context")
    return Config(context=context)


@pytest.fixture(scope="function")
def mobile_browser(config):
    options = UiAutomator2Options()
    options.platform_name = config.platform_name
    options.device_name = config.device_name
    options.automation_name = config.automation_name
    options.app_package = config.app_package
    options.app_activity = config.app_activity

    browser.config.driver = webdriver.Remote(config.remote_url, options=options)
    browser.config.timeout = 10

    yield browser

    browser.quit()