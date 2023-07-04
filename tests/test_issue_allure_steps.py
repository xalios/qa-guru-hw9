import allure
from allure_commons.types import Severity
from selene.support.shared import browser
from selene import by, have
from allure import step


@allure.label("owner", "xalios")
@allure.tag('smoke')
@allure.severity(Severity.NORMAL)
@allure.story('test using steps')
def test_issue_title(browser_setup):
    with step('Открываем главую страницу GitHub'):
        browser.open("https://github.com/")

    with step('Находим проект'):
        browser.element(".header-search-input").click()
        browser.element(".header-search-input").send_keys("eroshenkoam/allure-example")
        browser.element(".header-search-input").submit()
        browser.element(by.link_text("eroshenkoam/allure-example")).click()

    with step('Переходим в таб issue'):
        browser.element("#issues-tab").click()

    with step('Проверяем название issue'):
        browser.element('#issue_81_link').should(have.exact_text('issue_to_test_allure_report'))
