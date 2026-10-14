from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_login_with_valid_credentials(driver, base_url, credentials, wait):
    driver.get(base_url)
    driver.find_element(By.ID, "user-name").send_keys(credentials["username"])
    driver.find_element(By.ID, "password").send_keys(credentials["password"])
    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))
    assert driver.current_url.endswith("/inventory.html")


def test_login_with_invalid_password_shows_error(driver, base_url, wait):
    driver.get(base_url)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()

    error = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container"))
    )
    assert "Username and password do not match" in error.text


def test_login_with_empty_fields_shows_required_error(driver, base_url, wait):
    driver.get(base_url)
    driver.find_element(By.ID, "login-button").click()

    error = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container"))
    )
    assert "Username is required" in error.text
