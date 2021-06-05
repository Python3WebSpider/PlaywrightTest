from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.baidu.com/
    page.goto("https://www.baidu.com/")

    # Click input[name="wd"]
    page.click("input[name=\"wd\"]")

    # Fill input[name="wd"]
    page.fill("input[name=\"wd\"]", "nba")

    # Press Enter
    # with page.expect_navigation(url="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=nba&fenlei=256&rsv_pq=c4e7c93800022149&rsv_t=51eei5XA6At5rtVRipYK2c1guDYFZrhsJewHdsvB6cVWepemT4sW1L7%2B4Io&rqlang=cn&rsv_enter=1&rsv_dl=ib&rsv_sug3=4&rsv_sug1=3&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&inputT=1108&rsv_sug4=2164"):
    with page.expect_navigation():
        page.press("input[name=\"wd\"]", "Enter")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)