from testpages.tests.tests_events import *


@pytest.mark.smoke
def test_event_on_blur(page: Page, event_on_blur):
    event_on_blur()


@pytest.mark.smoke
def test_event_on_clic(page: Page, event_on_clic):
    event_on_clic()


@pytest.mark.smoke
def test_event_context_menu(page: Page, event_context_menu):
    event_context_menu()


@pytest.mark.smoke
def test_event_double_click(page: Page, event_double_click):
    event_double_click()


@pytest.mark.smoke
def test_event_focus(page: Page, event_focus):
    event_focus()


@pytest.mark.smoke
def test_event_key_down(page: Page, event_key_down):
    event_key_down()


@pytest.mark.smoke
def test_event_on_mouse_down(page: Page, event_on_mouse_down):
    event_on_mouse_down()