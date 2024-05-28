from testpages.config.config_playwright import *
from testpages.data.data_testpages import *
from testpages.locators.locators_testpages import *


@pytest.fixture
def web_page_example(page: Page):
    def web_page_example_func():
        page.goto(data_web_page_example)
        assert page.url == data_web_page_example, "Проверка загрузки страницы - не загрузилась"
        page.click(locator_web_page_example)
        page.wait_for_timeout(3000)
        page.screenshot(path='screenshots/web_page_example.png')

    return web_page_example_func


@pytest.fixture
def element_attributes(page: Page):
    def element_attributes_func():
        page.goto(data_element_attributes)
        page.wait_for_timeout(3000)
        page.click(locator_element_attributes)
        page.wait_for_timeout(3000)
        page.screenshot(path='screenshots/element_attributes.png')

    return element_attributes_func
