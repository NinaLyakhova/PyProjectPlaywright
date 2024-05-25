from testpages.tests.tests_form_exemple import *


@pytest.mark.smoke
def test_username_press(page: Page, username_press):
    username_press()


@pytest.mark.smoke
def test_textarea(page: Page, textarea):
    textarea()


@pytest.mark.smoke
def test_set_filename(page: Page, set_filename):
    set_filename()


@pytest.mark.smoke
def test_checkbox_items(page: Page, checkbox_items):
    checkbox_items()
