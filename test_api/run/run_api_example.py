from test_api.test.test_api_example import *


@pytest.mark.smoke
def test_api_get_pet(page: Page, api_get_pet):
    api_get_pet()


@pytest.mark.smoke
def test_api_get_weather(page: Page, api_get_weather):
    api_get_weather()


@pytest.mark.smoke
def test_api_post_json(page: Page, api_post_json):
    api_post_json()
