from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://spa6.scrape.center/')
    page.wait_for_load_state('networkidle')
    element = page.query_selector('a.name')
    print(element.get_attribute('href'))
    print(element.text_content())
    browser.close()
