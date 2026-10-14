-- Optional standalone SQLite exercise; these are practice tables, not SauceDemo data.
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    unit_price REAL NOT NULL CHECK (unit_price >= 0)
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL REFERENCES products(product_id),
    quantity INTEGER NOT NULL CHECK (quantity > 0)
);

INSERT INTO products (product_id, product_name, unit_price) VALUES
    (1, 'Backpack', 29.99),
    (2, 'Bike Light', 9.99);

INSERT INTO orders (order_id, product_id, quantity) VALUES
    (101, 1, 2),
    (102, 2, 1);

-- Check that prices are non-negative.
SELECT product_id, product_name, unit_price
FROM products
WHERE unit_price < 0;

-- Validate order lines and calculate their expected totals.
SELECT o.order_id, p.product_name, o.quantity, p.unit_price,
       o.quantity * p.unit_price AS expected_total
FROM orders AS o
JOIN products AS p ON p.product_id = o.product_id
ORDER BY o.order_id;
