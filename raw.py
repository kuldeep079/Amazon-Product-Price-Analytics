import pandas as pd

# Read Amazon Dataset
df = pd.read_csv("data/raw/amazon.csv")

# 1. Dataset Shape
print("DATASET SHAPE")
print(df.shape)

# 2. Column Names
print("\nCOLUMN NAMES")
print(df.columns.tolist())

# 3. Data Types
print("\nDATA TYPES")
print(df.dtypes)

# 4. Missing Values
print("\nMISSING VALUES")
print(df.isnull().sum())

# 5. Duplicate Rows
print("\nDUPLICATE ROWS")
print(df.duplicated().sum())





print("DATA QUALITY CHECKS\n")
print(df.isnull().sum())



import pandas as pd
df = pd.read_csv("data/raw/amazon.csv")
print(df['rating_count'].isnull().sum())

print("\nROWS WITH MISSING rating count")
print(df[df['rating_count'].isnull()])

#Remove missing values in rating_count column
df_clean = df.dropna(subset=["rating_count"]).copy()

print("BEFORE CLEANING:",df.shape)
print("AFTER CLEANING:",df_clean.shape)


#3. Duplicate Rows check
print("\nDUPLICATE ROWS")
print(df_clean.duplicated().sum())


print("\nDATA TYPES AFTER CLEANING")
print(df_clean.dtypes)

#convert price columns

price_cols = ["discounted_price", "actual_price"]
for col in price_cols:
    df[col] = df[col].str.replace("₹", "", regex=False)
    df[col] = df[col].str.replace(",", "", regex=False)
    df[col] = pd.to_numeric(df[col], errors='coerce')
    print(df[price_cols].dtypes)
    print(df[price_cols].head())

# Convert percentage
df["discount_percentage"] = pd.to_numeric(df["discount_percentage"].str.replace("%", "", regex=False), errors="coerce")

# Convert rating
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

# Convert rating count
df["rating_count"] = df["rating_count"].str.replace(",", "", regex=False)
df["rating_count"] = pd.to_numeric(df["rating_count"], errors="coerce")


print(df[["discount_percentage", "rating", "rating_count"]].dtypes)
print(df[["discount_percentage", "rating", "rating_count"]].head())

# find missing values identify
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])

missing_values_percentage = (df.isna().sum() / len(df)) * 100
print(missing_values_percentage[missing_values_percentage > 0])

#identify rows with missing values

missing_rows = df[df.isna().any(axis=1)]
print(missing_rows)
print(df.isna().sum())

#Handle missing values
df["rating"] = df["rating"].fillna(df["rating"].median())
df["rating_count"] = df["rating_count"].fillna(df["rating_count"].median())
print(df.isna().sum())

#duplicate rows check
print(df.duplicated().sum())

#clean text columns
text_cols = df.select_dtypes(include=["object","str"]).columns
for col in text_cols:
    df[col] = df[col].str.strip()
#Validate product prices
print("Invalid discounted prices:")
print(df[df["discounted_price"] < 0])

print("Invalid actual prices:")
print(df[df["actual_price"] < 0])
#Rating validation
print(df[(df["rating"] < 0) | (df["rating"] > 5)])
#Discount percentage validation
print(df[(df["discount_percentage"] < 0) | (df["discount_percentage"] > 100)])
#Business Rules Validation
print(df[(df["discounted_price"] > df["actual_price"])])
#Check Data Types
print(df.dtypes)
print(df.info())
print("final shape:", df.shape)
print("missing values :", df.isnull().sum().sum())
print("duplicate rows :", df.duplicated().sum())

#price savings calutlation
df["price_savings"] = df["actual_price"] - df["discounted_price"]
print(df[["actual_price","discounted_price","price_savings"]].head())

#Final Data Validation
print("\n---FINAL DATA VALIDATION---")
print("Total Rows:", len(df))
print("missing Values:", df.isnull().sum().sum())
print("duplicate Rows:", df.duplicated().sum())
print("Invalid Ratings:",((df["rating"] < 0) | (df["rating"] > 5)).sum())
print("Invalid Discount:",((df["discount_percentage"] < 0) | (df["discount_percentage"] > 100)).sum())
print("Invalid prices:",((df["actual_price"] <= 0) | (df["discounted_price"] <= 0)).sum())
print("Business Rule Violations:",(df["actual_price"] < df["discounted_price"]).sum())
print("Invalid Price savings:",(df["price_savings"]!=df["actual_price"] - df["discounted_price"]).sum())

df.to_csv("data/processed/amazon_cleaned.csv", index=False)   

























