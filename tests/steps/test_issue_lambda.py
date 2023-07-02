from selene.support.shared import browser
from selene import by, have
import allure


@allure.step('Открываем главую страницу GitHub')
def open_main_page():
    browser.open("https://github.com/")


@allure.step('Находим проект')
def find_github_project():
    browser.element(".header-search-input").click()
    browser.element(".header-search-input").send_keys("eroshenkoam/allure-example")
    browser.element(".header-search-input").submit()
    browser.element(by.link_text("eroshenkoam/allure-example")).click()


@allure.step('Переходим в таб issue')
def open_issues_tab():
    browser.element("#issues-tab").click()


@allure.step('Проверяем название issue')
def assert_issue_title():
    browser.element('#issue_81_link').should(have.exact_text('issue_to_test_allure_report'))
