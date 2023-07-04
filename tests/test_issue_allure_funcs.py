import allure
from allure_commons.types import Severity
from tests.steps import steps_issue_allure_funcs as step


@allure.label("owner", "xalios")
@allure.tag('smoke')
@allure.severity(Severity.NORMAL)
@allure.story('test using functions')
def test_issue_title(browser_setup):
    step.open_main_page()
    step.find_github_project()
    step.open_issues_tab()
    step.assert_issue_title()
