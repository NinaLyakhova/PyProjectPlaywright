import pytest
from playwright.sync_api import sync_playwright, Page, BrowserContext
from testpages.data.data_form_example import *
from testpages.locators.locators_form_exemple import *


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
        page.goto(data_page_form_exemple)
        page.wait_for_timeout(3000)
        page.locator(locator_username).fill(data_username)
        page.locator(locator_password).fill(data_password)
        page.wait_for_timeout(3000)
        page.click(locator_submit)
        page.wait_for_timeout(3000)
        page.screenshot(path="screenshots/username_press.png")

    return username_press_func


@pytest.fixture
def textarea(page: Page):
    def textarea_func():
        page.goto(data_page_form_exemple)
        page.wait_for_timeout(3000)

    def key_textarea(locator_textarea: str, data_textarea: str):
        page.click(locator_textarea)
        page.keyboard.down('Shift')
        for _ in range(8):
            page.keyboard.press('ArrowLeft')
            page.keyboard.up('Shift')
            page.keyboard.type(data_textarea)

        key_textarea(locator_textarea, data_textarea)
        page.wait_for_timeout(3000)
        page.click(locator_submit)
        page.wait_for_timeout(3000)
        page.screenshot(path="screenshots/username_press.png")

    return textarea_func


@pytest.fixture
def set_filename(page: Page):
    def set_filename_func():
        page.goto(data_page_form_exemple)
        page.wait_for_timeout(1000)
        page.click(locator_filename)
        page.set_input_files('input[type="file"]', data_filename_path)
        page.wait_for_timeout(1000)
        page.click(locator_submit)
        page.wait_for_timeout(1000)
        page.screenshot(path="screenshots/set_filename.png")

    return set_filename_func


@pytest.fixture
def checkbox_items(page: Page):
    def checkbox_items_func():
        page.goto(data_page_form_exemple)
        page.wait_for_timeout(1000)
        page.check('#HTMLFormElements > table > tbody > tr:nth-child(5) > td > input[type=checkbox]:nth-child(2)')
        page.wait_for_timeout(1000)
        page.check('#HTMLFormElements > table > tbody > tr:nth-child(5) > td > input[type=checkbox]:nth-child(3)')
        page.wait_for_timeout(1000)
        page.uncheck('#HTMLFormElements > table > tbody > tr:nth-child(5) > td > input[type=checkbox]:nth-child(4)')
        page.wait_for_timeout(1000)
        page.click(locator_submit)
        page.wait_for_timeout(1000)
        page.screenshot(path="screenshots/set_filename.png")

    return checkbox_items_func


@pytest.fixture
def radio_items(page: Page):
    def radio_items_func():
        page.goto(data_page_form_exemple)
        page.wait_for_timeout(1000)
        page.check('#HTMLFormElements > table > tbody > tr:nth-child(6) > td > input[type=radio]:nth-child(2)')
        page.wait_for_timeout(1000)
        page.click(locator_submit)
        page.wait_for_timeout(1000)
        page.screenshot(path="screenshots/radio_items.png")

    return radio_items_func


@pytest.fixture
def multiple_select_values(page: Page):
    def multiple_select_values_func():
        page.goto(data_page_form_exemple)
        page.wait_for_timeout(1000)
        page.select_option('#HTMLFormElements > table > tbody > tr:nth-child(7) > td > select', value=['ms1'])
        page.wait_for_timeout(1000)
        page.select_option('#HTMLFormElements > table > tbody > tr:nth-child(7) > td > select', value=['ms2'])
        page.wait_for_timeout(1000)
        page.select_option('#HTMLFormElements > table > tbody > tr:nth-child(7) > td > select', value=['ms3'])
        page.wait_for_timeout(1000)
        page.select_option('#HTMLFormElements > table > tbody > tr:nth-child(7) > td > select', value=['ms4'])
        page.wait_for_timeout(1000)
        page.click(locator_submit)
        page.wait_for_timeout(1000)
        page.screenshot(path="screenshots/select_values.png")

    return multiple_select_values_func


@pytest.fixture
def dropdown(page: Page):
    def dropdown_func():
        page.goto(data_page_form_exemple)
        page.wait_for_timeout(1000)
        page.select_option('#HTMLFormElements > table > tbody > tr:nth-child(8) > td > select', value='dd1')
        page.wait_for_timeout(1000)
        page.select_option('#HTMLFormElements > table > tbody > tr:nth-child(8) > td > select', value='dd2')
        page.wait_for_timeout(1000)
        page.select_option('#HTMLFormElements > table > tbody > tr:nth-child(8) > td > select', value='dd5')
        page.wait_for_timeout(1000)
        page.click(locator_submit)
        page.wait_for_timeout(1000)
        page.screenshot(path="screenshots/dropdown.png")

    return dropdown_func
