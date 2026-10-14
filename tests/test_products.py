from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_products_are_visible_with_names_and_prices(logged_in):
    products = logged_in.find_elements(By.CLASS_NAME, "inventory_item")

    assert len(products) == 6
    assert all(
        product.find_element(By.CLASS_NAME, "inventory_item_name").text
        and product.find_element(By.CLASS_NAME, "inventory_item_price").text.startswith("$")
        for product in products
    )


def test_product_images_load(logged_in, wait):
    products = logged_in.find_elements(By.CLASS_NAME, "inventory_item")

    assert len(products) == 6
    assert all(
        wait.until(
            lambda driver: driver.execute_script(
                "return arguments[0].complete && arguments[0].naturalWidth > 0;",
                product.find_element(By.CSS_SELECTOR, ".inventory_item_img img"),
            )
        )
        for product in products
    )


def test_products_can_be_sorted_by_price_low_to_high(logged_in):
    Select(logged_in.find_element(By.CLASS_NAME, "product_sort_container")).select_by_value(
        "lohi"
    )
    prices = [
        float(
            product.find_element(By.CLASS_NAME, "inventory_item_price")
            .text.removeprefix("$")
        )
        for product in logged_in.find_elements(By.CLASS_NAME, "inventory_item")
    ]

    assert prices == sorted(prices)
