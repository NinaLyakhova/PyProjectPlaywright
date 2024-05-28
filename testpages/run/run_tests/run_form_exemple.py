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


@pytest.mark.smoke
def test_radio_items(page: Page, radio_items):
    radio_items()


def test_multiple_select_values(page: Page, multiple_select_values):
    multiple_select_values()


def test_dropdown(page: Page, dropdown):
    dropdown()