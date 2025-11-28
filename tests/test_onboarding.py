import allure
from selene import be
from selene.support.shared import browser
import time


@allure.title("Тест онбординга Wikipedia")
@allure.feature("Onboarding")
@allure.story("Прохождение 4 экранов приветствия")
def test_wikipedia_onboarding(mobile_management):
    """Тест проходит 4 экрана онбординга Wikipedia и проверяет каждый экран"""

    with allure.step("Экран 1: The Free Encyclopedia"):
        # Проверяем заголовок
        title = browser.element('//*[contains(@text, "The Free Encyclopedia")]')
        title.should(be.visible)

        # Нажимаем Continue
        continue_btn = browser.element('//*[@text="Continue"]')
        continue_btn.should(be.visible)
        continue_btn.click()

        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="screen_1_welcome",
            attachment_type=allure.attachment_type.PNG
        )

    with allure.step("Экран 2: New ways to explore"):
        # Проверяем заголовок
        title = browser.element('//*[contains(@text, "New ways to explore")]')
        title.should(be.visible)

        # Нажимаем Continue
        continue_btn = browser.element('//*[@text="Continue"]')
        continue_btn.should(be.visible)
        continue_btn.click()

        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="screen_2_explore",
            attachment_type=allure.attachment_type.PNG
        )

    with allure.step("Экран 3: Reading lists with sync"):
        # Проверяем заголовок
        title = browser.element('//*[contains(@text, "Reading lists with sync")]')
        title.should(be.visible)

        # Нажимаем Continue
        continue_btn = browser.element('//*[@text="Continue"]')
        continue_btn.should(be.visible)
        continue_btn.click()

        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="screen_3_reading",
            attachment_type=allure.attachment_type.PNG
        )

    with allure.step("Экран 4: Data & Privacy"):
        # Проверяем заголовок
        title = browser.element('//*[contains(@text, "Data & Privacy")]')
        title.should(be.visible)

        # Нажимаем Get started
        get_started_btn = browser.element('//*[@text="Get started"]')
        get_started_btn.should(be.visible)
        get_started_btn.click()

        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="screen_4_privacy",
            attachment_type=allure.attachment_type.PNG
        )

    with allure.step("Проверяем главный экран приложения"):
        # Проверяем что видна поисковая строка
        search_container = browser.element('//*[@resource-id="org.wikipedia.alpha:id/search_container"]')
        search_container.should(be.visible)

        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="main_screen",
            attachment_type=allure.attachment_type.PNG
        )