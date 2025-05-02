import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})

    page = context.new_page()
    page.goto("http://10.10.1.102:6001/login")
    time.sleep(2)
    # Login Page
    page.get_by_role("textbox", name="User Name").click()
    page.get_by_role("textbox", name="User Name").fill("Prachi1")
    time.sleep(2)

    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Cir@123")
    time.sleep(2)

    page.get_by_role("button", name="Login").click()
    page.wait_for_load_state("networkidle")
    time.sleep(2)
    # Masters
    page.get_by_text("Masters").nth(0).click()
    time.sleep(2)

    page.wait_for_selector("text=Plant")
    page.get_by_role("link", name="Plant").nth(0).click()
    time.sleep(2)
    # Plant Master
    page.get_by_role("button", name="Add").click()
    time.sleep(2)

    page.locator("#AddZBCPlant_PlantName").click()
    page.locator("#AddZBCPlant_PlantName").fill("Test Kitto 1")
    time.sleep(2)

    page.locator("#AddZBCPlant_PlantCode").click()
    page.locator("#AddZBCPlant_PlantCode").fill("8792")
    time.sleep(2)

    page.locator("#AddZBCPlant_Currency").click()
    page.locator("#AddZBCPlant_Currency").fill("USD")
    time.sleep(2)

    page.locator("#react-select-Currency-option-8").click()
    time.sleep(2)

    page.locator("#AddZBCPlant_CompanyName").click()
    page.get_by_text("CIR(CIR1)", exact=True).click()
    time.sleep(2)

    page.locator("#AddZBCPlant_PhoneNumber").click()
    page.locator("#AddZBCPlant_PhoneNumber").fill("1111111111")
    time.sleep(2)

    page.locator("#AddZBCPlant_AddressLine1").click()
    page.locator("#AddZBCPlant_AddressLine1").fill("A1")
    time.sleep(2)

    page.locator("#AddZBCPlant_AddressLine2").click()
    page.locator("#AddZBCPlant_AddressLine2").fill("A2")
    time.sleep(2)

    page.locator("#AddZBCPlant_CountryId").click()
    page.locator("#AddZBCPlant_CountryId").fill("india")
    page.locator("#react-select-CountryId-option-99").click()
    time.sleep(2)

    page.locator("#AddZBCPlant_StateId").click()
    page.locator("#AddZBCPlant_StateId").fill("madhya pradesh")
    page.locator("#react-select-StateId-option-20").click()
    time.sleep(2)

    page.locator("#AddZBCPlant_CityId").click()
    page.locator("#AddZBCPlant_CityId").fill("indore")
    page.locator("div[id^='react-select-CityId-option-']").filter(has_text="Indore").click()
    time.sleep(2)

    page.locator("#AddZBCPlant_ZipCode").click()
    page.locator("#AddZBCPlant_ZipCode").fill("452001")
    time.sleep(2)

    page.get_by_role("button", name="Save").click()
    time.sleep(2)

    page.get_by_role("textbox", name="Plant Name Filter Input").click()
    page.get_by_role("textbox", name="Plant Name Filter Input").fill("test kitto 1")
    time.sleep(2)

    # View action
    view_button = page.get_by_role("button", name="View", exact=True)
    view_button.scroll_into_view_if_needed()
    view_button.hover()
    time.sleep(1)  # to visually highlight for user
    view_button.click()
    time.sleep(2)

    # Cancel view
    cancel_button = page.get_by_role("button", name="Cancel")
    cancel_button.scroll_into_view_if_needed()
    cancel_button.hover()
    time.sleep(1)
    cancel_button.click()
    time.sleep(2)

    # Edit action
    edit_button = page.get_by_role("button", name="Edit")
    edit_button.scroll_into_view_if_needed()
    edit_button.hover()
    time.sleep(1)
    edit_button.click()
    time.sleep(2)

    page.locator("#AddZBCPlant_AddressLine2").click()
    page.locator("#AddZBCPlant_AddressLine2").fill("A22")
    time.sleep(2)

    page.locator("#AddZBCPlant_AddressLine1").click()
    page.locator("#AddZBCPlant_AddressLine1").fill("A11")
    time.sleep(2)

    page.get_by_role("button", name="Update").click()
    time.sleep(2)

    # Filter the row for 'Test Kitto 1'
    page.get_by_role("textbox", name="Plant Name Filter Input").click()
    page.get_by_role("textbox", name="Plant Name Filter Input").fill("test kitto 1")
    time.sleep(2)

    # First, locate and click the Delete button
    delete_button = page.locator("//button[@title='Delete']").first
    delete_button.scroll_into_view_if_needed()  # Ensure it's visible
    delete_button.hover()
    time.sleep(2)  # Optional to see the hover effect
    delete_button.click()

    # Confirm deletion (OK button)
    page.get_by_role("button", name="OK").click()

    # Wait for the deletion success message (to be safe, not for button again)
    success_toast = page.locator("text=Plant deleted successfully")
    success_toast.wait_for(state="visible", timeout=10000)  # Wait for success confirmation

    print("Plant deleted successfully toast appeared.")
    time.sleep(5)

    # Logout
    logout_button = page.get_by_role("button", name="logout")
    logout_button.scroll_into_view_if_needed()
    logout_button.hover()
    time.sleep(5)
    logout_button.click()
    page.get_by_role("button", name="OK").click()
    time.sleep(5)

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
