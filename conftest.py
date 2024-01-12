import pytest
from selene import browser

@pytest.fixture(scope="function", autouse=True)
def browser_size():
    browser.config.window_width = 1280
    browser.config.window_height = 720

    yield

    browser.quit()