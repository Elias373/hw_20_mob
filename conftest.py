import pytest
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

    # BrowserStack требует специальные capabilities
    if "browserstack" in config.remote_url:
        # BrowserStack specific capabilities
        options.set_capability('platformName', config.platform_name)
        options.set_capability('deviceName', config.device_name)  # Важно: deviceName, а не device_name
        options.set_capability('automationName', config.automation_name)

        if config.app:
            options.set_capability('app', config.app)
        if config.app_package:
            options.set_capability('appPackage', config.app_package)
        if config.app_activity:
            options.set_capability('appActivity', config.app_activity)

        # BrowserStack options
        if config.bstack_userName and config.bstack_accessKey:
            options.set_capability('bstack:options', {
                "userName": config.bstack_userName,
                "accessKey": config.bstack_accessKey,
                "projectName": "Wikipedia Onboarding",
                "buildName": "Jenkins Build",
                "sessionName": "Onboarding Test",
                "appiumVersion": "2.0.0"
            })
    else:
        # Local Appium settings
        options.platform_name = config.platform_name
        options.device_name = config.device_name
        options.automation_name = config.automation_name

        if config.app:
            options.app = config.app
        if config.app_package:
            options.app_package = config.app_package
        if config.app_activity:
            options.app_activity = config.app_activity

    try:
        from selene.support.shared import browser
        print(f"🚀 Connecting to: {config.remote_url}")
        print(f"📱 Device: {config.device_name}")
        print(f"🔑 Username: {config.bstack_userName}")

        browser.config.driver = webdriver.Remote(config.remote_url, options=options)
        browser.config.timeout = 30

        yield browser

        browser.quit()
    except Exception as e:
        print(f"❌ Browser setup failed: {e}")
        raise