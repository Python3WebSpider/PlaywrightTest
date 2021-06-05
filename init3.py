from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
for browser_type in [playwright.chromium, playwright.firefox, playwright.webkit]:
    browser = browser_type.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.baidu.com')
    page.screenshot(path=f'screenshot-{browser_type.name}.png')
    print(page.title())
    browser.close()
playwright.stop()
