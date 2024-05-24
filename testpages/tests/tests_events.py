import pytest
from playwright.sync_api import sync_playwright, Page, BrowserContext
from testpages.data.data_events import *
from testpages.locators.locators_events import *


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
def event_on_blur(page: Page):
    def event_on_blur_func():
        page.goto(data_page_events)
        page.wait_for_timeout(1000)
        page.click(locator_on_blur)
        page.mouse.move(10, 0)
        page.mouse.down()
        page.mouse.up()
        page.wait_for_timeout(1000)
        page.screenshot(path="screenshots/event_on_blur.png")

    return event_on_blur_func


@pytest.fixture
def event_on_click(page: Page):
    def event_on_click_func():
        page.goto(data_page_events)
        page.wait_for_timeout(1000)
        page.click(locator_on_click)
        page.wait_for_timeout(1000)
        page.screenshot(path="screenshots/event_on_click.png")

    return event_on_click_func


@pytest.fixture
def event_on_context_menu(page: Page):
    def event_on_context_menu_func():
        page.goto(data_page_events)
        page.wait_for_timeout(1000)
        page.click(locator_on_context_menu, button="right")
        page.wait_for_timeout(1000)
        page.screenshot(path="screenshots/event_on_context_menu.png")

    return event_on_context_menu_func


@pytest.fixture
def event_on_double_click(page: Page):
    def event_on_double_click_func():
        page.goto(data_page_events)
        page.wait_for_timeout(1000)
        page.dblclick(locator_on_double_click)
        page.wait_for_timeout(1000)
        page.screenshot(path="screenshots/event_on_double_click.png")

    return event_on_double_click_func


@pytest.fixture
def event_on_focus(page: Page):
    def event_on_focus_func():
        page.goto(data_page_events)
        page.wait_for_timeout(1000)
        page.click(locator_on_focus)
        page.wait_for_timeout(1000)
        page.screenshot(path="screenshots/event_on_focus.png")

    return event_on_focus_func


@pytest.fixture
def event_on_key_down(page: Page):
    def event_on_key_down_func():
        page.goto(data_page_events)
        page.wait_for_timeout(1000)
        page.click(locator_on_key_down, button="middle")
        page.wait_for_timeout(1000)
        page.screenshot(path="screenshots/event_on_key_down.png")

    return event_on_key_down_func
