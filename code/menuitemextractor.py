if __name__ == "__main__":
    import sys
    sys.path.append('code')
    from menuitem import MenuItem
else:
    from code.menuitem import MenuItem


def clean_price(price: str) -> float:
    # Remove non-numeric characters (e.g., "$", ",") and ensure it doesn't pick up description text
    cleaned_price = ''.join(c for c in price if c.isdigit() or c == '.')
    
    if not cleaned_price:
        raise ValueError(f"Invalid price format: {price}")
    
    return float(cleaned_price)



def clean_scraped_text(scraped_text: str) -> list[str]:
    # List of unwanted strings to filter out
    unwanted = ['NEW!', 'GS', 'V']  # Add 'V' to the unwanted list
    
    # Split the text by new lines and remove extra spaces from each line
    cleaned_text = [line.strip() for line in scraped_text.split("\n") if line.strip()]
    
    # Filter out unwanted items from the cleaned list
    cleaned_text = [line for line in cleaned_text if all(u not in line for u in unwanted)]
    
    return cleaned_text



def extract_menu_item(title: str, scraped_text: str) -> MenuItem:
    # Extract the price from the text (assuming some method of extraction exists)
    price_str = extract_price(scraped_text)  # This is an example function

    # Check if price_str is valid before cleaning
    if not price_str or not any(char.isdigit() for char in price_str):
        raise ValueError(f"Invalid price data: {price_str}")

    # Clean the price string
    price = clean_price(price_str)

    # Process the rest of the scraped text (for title, description, etc.)
    description = extract_description(scraped_text)

    return MenuItem(title, price, description)


if __name__ == '__main__':
    # Example usage (fill in with actual scraped data):
    title = "Mozzarella Sticks"
    scraped_text = "Fried cheese sticks served with marinara sauce.\n$8.99"
    menu_item = extract_menu_item(title, scraped_text)
    print(menu_item)
