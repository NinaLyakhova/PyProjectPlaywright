import pytest
from playwright.sync_api import sync_playwright, Page, BrowserContext
from testpages.data.data_form_example import *
from testpages.locators.locators_form_exemple import *
from testpages.data.data_faker import *

@pytest.fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture
def browser(get_playwright):
    browser = get_playwright.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture
def browser_context(browser):
    context = browser.new_context(accept_downloads=True)
    yield context
    context.close()


@pytest.fixture
def page(browser_context: BrowserContext):
    page = browser_context.new_page()
    yield page
    page.close()


@pytest.fixture
def username_press(page: Page):
    def username_press_func():
        test_data = generate_test_data_mimesis()
        page.goto(data_page_form_exemple)
        page.wait_for_timeout(3000)
        page.locator(locator_username).fill(test_data["name"])
        page.locator(locator_password).fill(test_data["pass"])
        page.wait_for_timeout(3000)
        page.click(locator_submit)
        page.wait_for_timeout(3000)
        page.screenshot(path="screenshots/username_press.png")

    return username_press_func


@pytest.fixture
def textarea(page: Page):
    def textarea_func():
        test_data = generate_test_data_mimesis()
        page.goto(data_page_form_exemple)
        page.wait_for_timeout(3000)
        page.locator(locator_textarea).fill(test_data["text"])

    #def key_textarea(locator_textarea: str, data_textarea: str):
    #    page.click(locator_textarea)
    #    page.keyboard.down('Shift')
    #    for _ in range(8):
    #        page.keyboard.press('ArrowLeft')
    #        page.keyboard.up('Shift')
    #        page.keyboard.type(data_textarea)
    #    key_textarea(locator_textarea, data_textarea)
        page.wait_for_timeout(3000)
        page.click(locator_submit)
        page.wait_for_timeout(3000)
        page.screenshot(path="screenshots/username_press.png")

    return textarea_func