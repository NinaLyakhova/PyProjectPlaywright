from playwright.sync_api import sync_playwright

def test_example_chrome():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://playwright.dev")
        assert page.inner_text('h1') == 'Playwright enables reliable end-to-end testing for modern web apps.'
        browser.close()

def test_example_webkit():
    with sync_playwright() as p:
        browser = p.webkit.launch()
        page = browser.new_page()
        page.goto("http://playwright.dev")
        assert page.inner_text('h1') == 'Playwright enables reliable end-to-end testing for modern web apps.'
        browser.close()

def test_example_firefox():
    with sync_playwright() as p:
        browser = p.firefox.launch()
        page = browser.new_page()
        page.goto("http://playwright.dev")
        assert page.inner_text('h1') == 'Playwright enables reliable end-to-end testing for modern web apps.'
        browser.close()

def test_example_mob_chrome():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148')
        page = context.new_page()
        page.goto("http://playwright.dev")
        assert page.inner_text('h1') == 'Playwright enables reliable end-to-end testing for modern web apps.'
        browser.close()

def test_example_mob_webkit():
    with sync_playwright() as p:
        browser = p.webkit.launch(headless=False)
        context = browser.new_context(user_agent='Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Mobile/15E148 Safari/604.1', viewport={'width': 375, 'height': 667})
        page = context.new_page()
        page.goto("http://playwright.dev")
        page.wait_for_timeout(3000)
        assert page.inner_text('h1') == 'Playwright enables reliable end-to-end testing for modern web apps.'
        browser.close()