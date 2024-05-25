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
        page.wait_for_timeout(3000)
        page.click(locator_on_blur)
        page.mouse.move(10, 0)
        page.mouse.down()
        page.mouse.up()
        page.wait_for_timeout(3000)
        page.screenshot(path="screenshots/event_on_blur.png")
        class_event = page.query_selector(locator_on_blur).get_attribute("class")
        assert class_event == data_class_event, f"Класс кнопки {class_event}"

    return event_on_blur_func


@pytest.fixture
def event_on_clic(page: Page):
    def event_on_clic_func():
        page.goto(data_page_events)
        page.wait_for_timeout(3000)
        page.click(locator_on_click)
        page.wait_for_timeout(3000)
        page.screenshot(path="screenshots/event_on_click.png")
        class_event = page.query_selector(locator_on_click).get_attribute("class")
        assert class_event == data_class_event, f"Класс кнопки {class_event}"

    return event_on_clic_func


@pytest.fixture
def event_context_menu(page: Page):
    def event_on_context_menu_func():
        page.goto(data_page_events)
        page.wait_for_timeout(3000)
        page.click(locator_on_context_menu, button='right')
        page.wait_for_timeout(3000)
        page.screenshot(path="screenshots/event_on_context_menu.png")
        class_event = page.query_selector(locator_on_context_menu).get_attribute("class")
        assert class_event == data_class_event, f"Класс кнопки {class_event}"

    return event_on_context_menu_func


@pytest.fixture
def event_double_click(page: Page):
    def double_click_func():
        page.goto(data_page_events)
        page.wait_for_timeout(1000)
        page.dblclick(locator_on_double_click)
        page.wait_for_timeout(1000)
        page.screenshot(path="screenshots/show_double_click.png")
        class_event = page.query_selector(locator_on_double_click).get_attribute("class")
        assert class_event == data_class_event, f"Класс кнопки {class_event}"

    return double_click_func()


@pytest.fixture
def event_focus(page: Page):
    def event_focus_func():
        page.goto(data_page_events)
        page.wait_for_timeout(1000)
        button = page.locator("#onfocus")
        button.focus()
        page.wait_for_timeout(1000)
        page.screenshot(path="screenshots/event_on_focus.png", full_page=True)
        class_event = page.query_selector(locator_on_focus).get_attribute("class")
        assert class_event == data_class_event, f"Класс кнопки {class_event}"

    return event_focus_func


@pytest.fixture
def event_key_down(page: Page):
    def event_on_key_down_func():
        page.goto(data_page_events)
        page.wait_for_timeout(3000)
        page.press('#onkeydown', 'ArrowDown')
        page.wait_for_timeout(3000)
        page.screenshot(path="screenshots/event_on_key_down.png")
        class_event = page.query_selector(locator_on_key_down).get_attribute("class")
        assert class_event == data_class_event, f"Класс кнопки {class_event}"

    return event_on_key_down_func


@pytest.fixture
def event_key_up(page: Page):
    def event_on_key_up_func():
        page.goto(data_page_events)
        page.wait_for_timeout(3000)
        page.press('#onkeyup', 'ArrowUp')
        page.wait_for_timeout(3000)
        page.screenshot(path="screenshots/event_on_key_up.png")
        class_event = page.query_selector(locator_on_key_up).get_attribute("class")
        assert class_event == data_class_event, f"Класс кнопки {class_event}"

    return event_on_key_up_func


@pytest.fixture
def event_key_press(page: Page):
    def event_on_key_press_func():
        page.goto(data_page_events)
        page.wait_for_timeout(3000)
        page.press('#onkeypress', 'Space')
        page.wait_for_timeout(3000)
        page.screenshot(path="screenshots/event_on_key_press.png")
        class_event = page.query_selector(locator_on_key_press).get_attribute("class")
        assert class_event == data_class_event, f"Класс кнопки {class_event}"

    return event_on_key_press_func


@pytest.fixture
def event_mouse_over(page: Page):
    def event_on_mouse_over_func():
        page.goto(data_page_events)
        page.wait_for_timeout(3000)
        page.hover('#onmouseover')
        page.wait_for_timeout(3000)
        page.screenshot(path="screenshots/event_on_mouse_over.png")
        class_event = page.query_selector(locator_on_mouse_over).get_attribute("class")
        assert class_event == data_class_event, f"Класс кнопки {class_event}"

    return event_on_mouse_over_func


@pytest.fixture
def event_mouse_leave(page: Page):
    def event_on_mouse_leave():
        page.goto(data_page_events)
        page.wait_for_timeout(3000)
        page.click(locator_on_mouse_leave)
        page.mouse.move(10, 0)
        page.mouse.down()
        page.mouse.up()
        page.wait_for_timeout(3000)
        page.screenshot(path="screenshots/event_on_mouse_leave.png")
        class_event = page.query_selector(locator_on_mouse_leave).get_attribute("class")
        assert class_event == data_class_event, f"Класс кнопки {class_event}"

    return event_on_mouse_leave



@pytest.fixture
def event_on_mouse_down(page: Page):
    def event_on_mouse_down_func():
        page.goto(data_page_events)
        page.wait_for_timeout(1000)
        button = page.locator("#onmousedown")
        button.dispatch_event("mousedown")
        page.wait_for_timeout(1000)
        page.screenshot(path="screenshots/event_on_mouse_down.png", full_page=True)
        text_content = page.inner_text("#onmousedownstatus")
        assert "Event Triggered" in text_content

    return event_on_mouse_down_func
