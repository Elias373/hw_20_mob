import allure
from selene import be
from selene.support.shared import browser


@allure.title("Wikipedia Onboarding Test")
@allure.feature("Onboarding")
@allure.story("Complete 4 onboarding screens")
def test_wikipedia_onboarding(mobile_management):
    with allure.step("First screen: Free Encyclopedia"):
        browser.element('//*[contains(@text, "The Free Encyclopedia")]').should(be.visible)
        browser.element('//*[@text="Continue"]').click()

    with allure.step("Second screen: New ways to explore"):
        browser.element('//*[contains(@text, "New ways to explore")]').should(be.visible)
        browser.element('//*[@text="Continue"]').click()

    with allure.step("Third screen: Reading lists with sync"):
        browser.element('//*[contains(@text, "Reading lists with sync")]').should(be.visible)
        browser.element('//*[@text="Continue"]').click()

    with allure.step("Fourth screen: Data & Privacy"):
        browser.element('//*[contains(@text, "Data & Privacy")]').should(be.visible)
        browser.element('//*[@text="Get started"]').click()

    with allure.step("Verify main page loaded"):
        browser.element('//*[@resource-id="org.wikipedia.alpha:id/search_container"]').should(be.visible)