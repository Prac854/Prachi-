import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://10.10.1.102:6001/login")
    print("URL Hit successfully")
    time.sleep(5)
    page.get_by_role("textbox", name="User Name").click()
    print("user name found/click")
    time.sleep(5)
    page.get_by_role("textbox", name="User Name").fill("ayushi")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Cir@123")
    page.get_by_role("textbox", name="Password").press("Enter")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Master icon Masters").click()
    page.get_by_role("link", name="Additional Masters icon").click()
    page.get_by_role("link", name="Users icon Users").click()
    page.get_by_text("Ayushi Ganu").first.click()
    page.get_by_role("button", name="logout").click()
    page.get_by_role("button", name="OK").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


