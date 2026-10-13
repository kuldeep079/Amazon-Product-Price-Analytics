-- Amazon Product Price Analytics
-- Business Analysis Queries

-- 1. Total Products
SELECT COUNT(*) AS total_products
FROM dbo.amazon_products;


-- 2. Average Rating
SELECT ROUND(AVG(rating), 2) AS average_rating
FROM dbo.amazon_products;


-- 3. Average Discount Percentage
SELECT ROUND(AVG(discount_percentage), 2) AS average_discount
FROM dbo.amazon_products;


-- 4. Average Actual Price vs Discounted Price
SELECT
    ROUND(AVG(actual_price), 2) AS average_actual_price,
    ROUND(AVG(discounted_price), 2) AS average_discounted_price
FROM dbo.amazon_products;


-- 5. Total Potential Customer Savings
SELECT
    SUM(actual_price - discounted_price) AS total_potential_savings
FROM dbo.amazon_products;


-- 6. Products by Rating
SELECT
    rating,
    COUNT(*) AS product_count
FROM dbo.amazon_products
GROUP BY rating
ORDER BY rating DESC;


-- 7. Average Discount by Category
SELECT
    category,
    ROUND(AVG(discount_percentage), 2) AS average_discount
FROM dbo.amazon_products
GROUP BY category
ORDER BY average_discount DESC;


-- 8. Top 10 Products by Potential Savings
SELECT TOP 10
    product_name,
    actual_price,
    discounted_price,
    actual_price - discounted_price AS potential_savings
FROM dbo.amazon_products
ORDER BY potential_savings DESC;
