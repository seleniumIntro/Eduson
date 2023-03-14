import time

from playwright.sync_api import Page


def test_page(playwright, page: Page):
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://amazon.com")
    page.locator("#nav-link-accountList-nav-line-1").click()
    page.locator("//input[@type=\"email\"]").fill('selenium.introduction@mail.ru')
    page.click('input[type=submit]')
    page.locator("#ap_password").fill('123456')
    page.locator("#signInSubmit").click()
    assert page.locator("#nav-link-accountList-nav-line-1").text_content() == "Hello, test"

def test_adress(browser_context_args, playwright, page: Page):
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://amazon.com")
    page.locator("#nav-link-accountList-nav-line-1").click()
    page.locator("//input[@type=\"email\"]").fill('selenium.introduction@mail.ru')
    page.click('input[type=submit]')
    page.locator("#ap_password").fill('123456')
    page.locator("#signInSubmit").click()

    page.locator("#nav-link-accountList-nav-line-1").click()
    page.locator("h2:text(\"Your addresses\")").click()
    page.locator("#ya-myab-plus-address-icon").click()

    #заполнение полей
    page.locator("#address-ui-widgets-enterAddressLine1").fill('1201 HOWARD ST')
    page.locator("#address-ui-widgets-enterAddressLine2").fill('SAN FRANCISCO CA 94103')
    page.locator("#address-ui-widgets-enterAddressCity").fill('San Francisco')
    page.select_option('select#address-ui-widgets-enterAddressStateOrRegion-dropdown-nativeId', value='CA')
    page.locator("#address-ui-widgets-enterAddressPostalCode").fill('94103')
    page.locator("#address-ui-widgets-use-as-my-default").click()
    time.sleep(5)
    page.locator("//span[@data-action=\"form-submit-button-click\"]").click()
    time.sleep(5)