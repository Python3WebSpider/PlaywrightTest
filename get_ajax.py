from playwright.sync_api import sync_playwright


def on_response(response):
    if '/api/movie/' in response.url and response.status == 200:
        print(response.json())


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.on('response', on_response)
    page.goto('https://spa6.scrape.center/')
    page.wait_for_load_state('networkidle')
    browser.close()
