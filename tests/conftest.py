import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 20)


@pytest.fixture
def logged_in(driver, base_url, credentials, wait):
    driver.get(base_url)
    driver.find_element(By.ID, "user-name").send_keys(credentials["username"])
    driver.find_element(By.ID, "password").send_keys(credentials["password"])
    driver.find_element(By.ID, "login-button").click()
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))
    return driver
