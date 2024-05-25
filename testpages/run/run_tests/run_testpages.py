from testpages.tests.tests_testpages import *


@pytest.mark.smoke
def test_testpages_one(page: Page, testpages_one):
    testpages_one()


@pytest.mark.smoke
def test_testpages_index(page: Page, testpages_index):
    testpages_index()
