from playwright.sync_api import sync_playwright

url = 'https://www.komplett.no/product/1251458'

def remove_non_digits(s):
    return ''.join([c for c in s if c.isdigit()])

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()

    # Navigate to the website
    page.goto(url)

    text_content = page.locator('.product-price-now').text_content()

    price = remove_non_digits(text_content)

    print(float(price))

    # Close the browser
    browser.close()

with sync_playwright() as playwright:
    run(playwright)