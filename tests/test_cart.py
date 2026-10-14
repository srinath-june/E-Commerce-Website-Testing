from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_adding_and_removing_product_updates_cart(logged_in, wait):
    logged_in.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert badge.text == "1"

    logged_in.find_element(By.ID, "remove-sauce-labs-backpack").click()
    wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))


def test_cart_contains_added_product(logged_in, wait):
    logged_in.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    logged_in.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    item = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart_item")))
    assert item.find_element(By.CLASS_NAME, "inventory_item_name").text == (
        "Sauce Labs Backpack"
    )
