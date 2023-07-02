import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function')
def browser_setup():
    browser.config.window_height = '1920'
    browser.config.window_width = '1080'

    yield

    browser.quit()