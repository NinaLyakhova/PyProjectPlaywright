import pytest
from playwright.sync_api import sync_playwright, Page, BrowserContext
from testpages.data.data_alerts import *
from testpages.locators.locators_alerts import *


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
def show_alert_box(page: Page):
    def show_alert_box_func():
        page.goto(data_page_alerts)
        page.wait_for_timeout(1000)
        def alert_dialog(dialog):
            print(dialog.message)
            dialog.accept()
        page.on('dialog', alert_dialog)
        page.click(locator_alert_box)
        page.wait_for_timeout(2000)
        page.screenshot(path="screenshots/show_alert_box.png")
    return show_alert_box_func

@pytest.fixture
def show_confirm_box_accept(page: Page):
    def show_confirm_box_accept_func():
        page.goto(data_page_alerts)
        page.wait_for_timeout(1000)
        def alert_dialog(dialog):
            print(dialog.message)
            dialog.accept()
        page.on('dialog', alert_dialog)
        page.click(locator_confirm_box)
        page.wait_for_timeout(2000)
        page.screenshot(path="screenshots/show_confirm_accept_box.png")
    return show_confirm_box_accept_func

@pytest.fixture
def show_confirm_box_dismiss(page: Page):
    def show_confirm_box_dismiss_func():
        page.goto(data_page_alerts)
        page.wait_for_timeout(1000)
        def alert_dialog(dialog):
            print(dialog.message)
            dialog.dismiss()
        page.on('dialog', alert_dialog)
        page.click(locator_confirm_box)
        page.wait_for_timeout(2000)
        page.screenshot(path="screenshots/show_confirm_dismiss_box.png")
    return show_confirm_box_dismiss_func

@pytest.fixture
def show_prompt_box(page: Page):
    def show_prompt_box_func():
        page.goto(data_page_alerts)
        page.wait_for_timeout(1000)
        def alert_dialog_prompt(dialog):
            print(dialog.message)
            dialog.accept(data_alert_prompt)
        page.on('dialog', alert_dialog_prompt)
        page.click(locator_prompt_box)
        page.wait_for_timeout(2000)
        page.screenshot(path="screenshots/show_prompt_box.png", full_page=True)
    return show_prompt_box_func
