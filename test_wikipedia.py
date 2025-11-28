import pytest
import allure
from selene.support.shared import browser
from selene import be


@allure.epic("Wikipedia Mobile")
@allure.feature("Onboarding Screens")
class TestWikipediaOnboarding:

    @allure.story("Complete 4-step onboarding process")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_complete_onboarding_screens(self, mobile_browser):


        # Screen 1: The Free Encyclopedia
        with allure.step("Screen 1: Verify 'The Free Encyclopedia' and click Continue"):
            browser.element('//*[contains(@text, "The Free Encyclopedia")]').should(be.visible)
            allure.attach(
                browser.driver.get_screenshot_as_png(),
                name="screen_1_free_encyclopedia",
                attachment_type=allure.attachment_type.PNG
            )
            browser.element('//*[@text="Continue"]').click()

        # Screen 2: New ways to explore
        with allure.step("Screen 2: Verify 'New ways to explore' and click Continue"):
            browser.element('//*[contains(@text, "New ways to explore")]').should(be.visible)
            allure.attach(
                browser.driver.get_screenshot_as_png(),
                name="screen_2_new_ways",
                attachment_type=allure.attachment_type.PNG
            )
            browser.element('//*[@text="Continue"]').click()

        # Screen 3: Reading lists with sync
        with allure.step("Screen 3: Verify 'Reading lists with sync' and click Continue"):
            browser.element('//*[contains(@text, "Reading lists with sync")]').should(be.visible)
            allure.attach(
                browser.driver.get_screenshot_as_png(),
                name="screen_3_reading_lists",
                attachment_type=allure.attachment_type.PNG
            )
            browser.element('//*[@text="Continue"]').click()

        # Screen 4: Data & Privacy
        with allure.step("Screen 4: Verify 'Data & Privacy' and click Get started"):
            browser.element('//*[contains(@text, "Data & Privacy")]').should(be.visible)
            allure.attach(
                browser.driver.get_screenshot_as_png(),
                name="screen_4_data_privacy",
                attachment_type=allure.attachment_type.PNG
            )
            browser.element('//*[@text="Get started"]').click()

