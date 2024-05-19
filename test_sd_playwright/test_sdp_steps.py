from playwright.sync_api import sync_playwright, Page, BrowserContext
import pytest
from locator import *
from test_data import *

@pytest.fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture
def browser(get_playwright):
    # browser = get_playwright.chromium.launch(headless=False)
    browser = get_playwright.chromium.launch()
    yield browser
    browser.close()

@pytest.fixture
def browser_context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture
def page(browser_context: BrowserContext):
    page = browser_context.new_page()
    yield page
    page.close()

@pytest.fixture
def login(page: Page):
    def login_function():
        page.goto(data_web_adress_saucedemo)
        page.fill(locator_field_user_name, data_standard_user)
        page.fill(locator_field_user_pass, data_password)
        page.click(locator_button_login)
        page.screenshot(path=f"screenshot/login.png")
    return login_function

@pytest.fixture
def logout(page: Page):
    def logout_function():
        page.click(locator_button_menu)
        page.click(locator_button_logout)
        page.screenshot(path=f"screenshot/logout.png")
    return logout_function

@pytest.fixture
def sort_products(page: Page):
    def sort_products_function():
        page.select_option(locator_sort_2, value=data_sort_option_low)
        page.screenshot(path=f"screenshot/sort.png")
    return sort_products_function

@pytest.fixture
def get_product(page: Page):
    def get_product_function():
        page.click(locator_add_cart_product_1)
        page.click(locator_add_cart_product_2)
        page.click(locator_shopping_cart)
        page.click(locator_button_checkout)
        page.fill(locator_field_first_name, data_first_name)
        page.fill(locator_field_last_name, data_last_name)
        page.fill(locator_field_postal_code, data_zip_code)
        page.click(locator_button_submit)
        page.click(locator_button_finish)
        page.screenshot(path=f"screenshot/get.png")
    return get_product_function

@pytest.fixture
def login_successful(page: Page):
    def test_login_successful_function():
        assert "https://www.saucedemo.com/inventory.html" in page.url.lower()
        print('\n--- Вход успешный ---')
    return test_login_successful_function

@pytest.fixture
def logout_successful(page: Page):
    def test_logout_successful_function():
        assert "https://www.saucedemo.com/" in page.url.lower()
        print('\n--- Выход успешный ---')
    return test_logout_successful_function

@pytest.fixture
def sort_products_successful(page: Page):
    def sort_products_successful_function():
        first_product_id = page.query_selector(locator_sort_first_prod).get_attribute("class")
        assert first_product_id == "inventory_item_img"
        print(f'\n--- Сортировка успешна, данные: {first_product_id} ---')
    return sort_products_successful_function

@pytest.fixture
def get_product_successful(page: Page):
    def get_product_successful_function():
        assert "https://www.saucedemo.com/checkout-complete.html" in page.url.lower()
        print('\n--- Покупка успешна ---')
    return get_product_successful_function