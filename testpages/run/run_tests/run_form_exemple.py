from testpages.tests.tests_form_exemple import *


@pytest.mark.smoke
def test_username_press(page: Page, username_press):
    username_press()


@pytest.mark.smoke
def test_textarea(page: Page, textarea):
    textarea()