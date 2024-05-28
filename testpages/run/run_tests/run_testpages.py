from testpages.tests.tests_testpages import *


@pytest.mark.smoke
def test_web_page_example(page: Page, web_page_example):
    web_page_example()


@pytest.mark.smoke
def test_element_attributes(page: Page, element_attributes):
    element_attributes()
