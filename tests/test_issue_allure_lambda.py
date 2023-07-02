from tests.steps import steps_issue_allure_lamda as step


def test_issue_title(browser_setup):
    step.open_main_page()
    step.find_github_project()
    step.open_issues_tab()
    step.assert_issue_title()
