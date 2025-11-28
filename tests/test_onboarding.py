import allure
from selene import be
from selene.support.shared import browser



@allure.title("Wikipedia Test")
@allure.feature("Onboarding")
@allure.story("4 Screens")
def test_wikipedia_onboarding(mobile_management):


    with allure.step("he Free Encyclopedia"):

        title = browser.element('//*[contains(@text, "The Free Encyclopedia")]')
        title.should(be.visible)


        continue_btn = browser.element('//*[@text="Continue"]')
        continue_btn.should(be.visible)
        continue_btn.click()

        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="screen_1_welcome",
            attachment_type=allure.attachment_type.PNG
        )

    with allure.step("New ways to explore"):

        title = browser.element('//*[contains(@text, "New ways to explore")]')
        title.should(be.visible)


        continue_btn = browser.element('//*[@text="Continue"]')
        continue_btn.should(be.visible)
        continue_btn.click()

        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="screen_2_explore",
            attachment_type=allure.attachment_type.PNG
        )

    with allure.step("Reading lists with sync"):

        title = browser.element('//*[contains(@text, "Reading lists with sync")]')
        title.should(be.visible)


        continue_btn = browser.element('//*[@text="Continue"]')
        continue_btn.should(be.visible)
        continue_btn.click()

        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="screen_3_reading",
            attachment_type=allure.attachment_type.PNG
        )

    with allure.step("Data & Privacy"):

        title = browser.element('//*[contains(@text, "Data & Privacy")]')
        title.should(be.visible)


        get_started_btn = browser.element('//*[@text="Get started"]')
        get_started_btn.should(be.visible)
        get_started_btn.click()

        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="screen_4_privacy",
            attachment_type=allure.attachment_type.PNG
        )

    with allure.step("Main page"):

        search_container = browser.element('//*[@resource-id="org.wikipedia.alpha:id/search_container"]')
        search_container.should(be.visible)

        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="main_screen",
            attachment_type=allure.attachment_type.PNG
        )