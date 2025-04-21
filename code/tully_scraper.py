import re
from playwright.sync_api import Playwright, sync_playwright
from menuitemextractor import extract_menu_item
from menuitem import MenuItem
import pandas as pd

def tullyscraper(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.tullysgoodtimes.com/menus/")

        # Wait for the page to load (you may need to adjust the selector depending on the page)
    page.wait_for_selector(".menu-item")  # Adjust this selector as needed
    
    # Extract the menu items from the page
    menu_items = []
    
    # Assuming the menu items are within a container with class '.menu-item'
    menu_elements = page.query_selector_all(".menu-item")  # Update with actual selector
    
    for item in menu_elements:
        # Extracting data (name, description, price) - adjust based on actual HTML structure
        name = item.query_selector(".menu-item-name").inner_text()  # Replace with actual selector
        description = item.query_selector(".menu-item-description").inner_text()  # Replace with actual selector
        price_text = item.query_selector(".menu-item-price").inner_text()  # Replace with actual selector
        price = float(re.sub(r'[^\d.]', '', price_text))  # Clean the price string
        
        # Create a MenuItem object
        menu_item = MenuItem(name=name, price=price, category="Menu", description=description)
        menu_items.append(menu_item)
    
    # Optionally convert to a DataFrame
    menu_data = [item.to_dict() for item in menu_items]
    df = pd.DataFrame(menu_data)
    
    # Save to CSV or display (for example, saving to a CSV)
    df.to_csv("tullys_menu.csv", index=False)

    
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    tullyscraper(playwright)
