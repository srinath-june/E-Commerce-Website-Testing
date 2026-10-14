from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_checkout_completes_order(logged_in, wait):
    logged_in.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    logged_in.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart_item")))
    logged_in.find_element(By.ID, "checkout").click()

    wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
    logged_in.find_element(By.ID, "first-name").send_keys("Taylor")
    logged_in.find_element(By.ID, "last-name").send_keys("Tester")
    logged_in.find_element(By.ID, "postal-code").send_keys("10001")
    logged_in.find_element(By.ID, "continue").click()
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_info")))
    logged_in.find_element(By.ID, "finish").click()

    confirmation = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    )
    assert confirmation.text == "Thank you for your order!"
