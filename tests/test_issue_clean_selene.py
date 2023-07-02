from selene.support.shared import browser
from selene import by, have


def test_issue_title(browser_setup):
    browser.open("https://github.com/")

    browser.element(".header-search-input").click()
    browser.element(".header-search-input").send_keys("eroshenkoam/allure-example")
    browser.element(".header-search-input").submit()
    browser.element(by.link_text("eroshenkoam/allure-example")).click()
    browser.element("#issues-tab").click()

    browser.element('#issue_81_link').should(have.exact_text('issue_to_test_allure_report'))

