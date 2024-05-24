from testpages.tests.tests_events import *


@pytest.mark.smoke
def test_event_on_blur(page: Page, event_on_blur):
    event_on_blur()


@pytest.mark.smoke
def test_event_on_click(page: Page, event_on_click):
    event_on_click()


@pytest.mark.smoke
def test_event_on_context_menu(page: Page, event_on_context_menu):
    event_on_context_menu()


@pytest.mark.smoke
def test_event_on_double_click(page: Page, event_on_double_click):
    event_on_double_click()


@pytest.mark.smoke
def test_event_on_focus(page: Page, event_on_focus):
    event_on_focus()

    @pytest.mark.smoke
    def test_event_on_key_down(page: Page, event_on_key_down):
        event_on_key_down()
