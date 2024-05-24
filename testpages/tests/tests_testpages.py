from testpages.config.config_playwright import *
from testpages.data.data_testpages import *
from testpages.locators.locators_testpages import *

@pytest.fixture
def testpages_one(page: Page):
    def testpages_one_func():
        page.goto(data_page_testpages)
        assert page.inner_text(locator_h1) == data_h1_testpages
        page.mouse.wheel(0, 10000)
        page.wait_for_timeout(3000)
    return testpages_one_func

@pytest.fixture
def testpages_index(page: Page):
    def testpages_one_func():
        page.goto(data_page_testpages)
        page.click(locator_testpages_index)
        assert page.inner_text(locator_h1) == data_h1_testpages
    return testpages_one_func
