-- Amazon Product Price Analytics
-- Data Quality Checks

-- 1. Check total records
SELECT COUNT(*) AS total_records
FROM dbo.amazon_products;

-- 2. Check missing product names
SELECT COUNT(*) AS missing_product_names
FROM dbo.amazon_products
WHERE product_name IS NULL
   OR LTRIM(RTRIM(product_name)) = '';

-- 3. Validate product ratings
SELECT COUNT(*) AS invalid_ratings
FROM dbo.amazon_products
WHERE rating < 0 OR rating > 5 OR rating IS NULL;

-- 4. Validate prices
SELECT COUNT(*) AS invalid_prices
FROM dbo.amazon_products
WHERE actual_price < 0
   OR discounted_price < 0
   OR discounted_price > actual_price;

-- 5. Validate discount percentage
SELECT COUNT(*) AS invalid_discounts
FROM dbo.amazon_products
WHERE discount_percentage < 0
   OR discount_percentage > 100;

-- 6. Check duplicate product IDs
SELECT product_id, COUNT(*) AS duplicate_count
FROM dbo.amazon_products
GROUP BY product_id
HAVING COUNT(*) > 1;
