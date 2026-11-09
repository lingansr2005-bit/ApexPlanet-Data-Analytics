
import pandas as pd
from pathlib import Path

print("DATA VALIDATION STARTED")
print("=" * 55)

# 1. Load transformed dataset
input_file = "data/processed/transformed_sales_dataset.csv"

df = pd.read_csv(input_file)

print("\n1. DATASET INFORMATION")
print("Total Rows:", df.shape[0])
print("Total Columns:", df.shape[1])

# 2. Define required columns
required_columns = [
    "Order_ID",
    "Order_Date",
    "Customer_ID",
    "Customer_Name",
    "Age",
    "Gender",
    "City",
    "Product",
    "Category",
    "Quantity",
    "Unit_Price",
    "Total_Sales"
]

# 3. Check required columns
missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

print("\n2. REQUIRED COLUMN VALIDATION")

if missing_columns:
    print("Missing columns:", missing_columns)
else:
    print("All required columns are available.")

# Stop if essential columns are missing
if missing_columns:
    raise ValueError("Required columns are missing. Check the dataset.")

# 4. Check missing values
print("\n3. MISSING VALUES VALIDATION")

missing_values = df.isnull().sum()

print(missing_values)

missing_count = int(missing_values.sum())

# 5. Check duplicate records
print("\n4. DUPLICATE VALIDATION")

duplicate_count = int(df.duplicated().sum())

print("Duplicate Rows:", duplicate_count)

# 6. Check data types
print("\n5. DATA TYPE VALIDATION")

print(df.dtypes)

# 7. Validate Age
print("\n6. AGE VALIDATION")

age = pd.to_numeric(df["Age"], errors="coerce")

invalid_age = int(
    ((age < 0) | (age > 100) | age.isna()).sum()
)

print("Invalid Age Records:", invalid_age)

# 8. Validate Quantity
print("\n7. QUANTITY VALIDATION")

quantity = pd.to_numeric(
    df["Quantity"], errors="coerce"
)

invalid_quantity = int(
    ((quantity <= 0) | quantity.isna()).sum()
)

print("Invalid Quantity Records:", invalid_quantity)

# 9. Validate Unit Price
print("\n8. UNIT PRICE VALIDATION")

unit_price = pd.to_numeric(
    df["Unit_Price"], errors="coerce"
)

invalid_price = int(
    ((unit_price < 0) | unit_price.isna()).sum()
)

print("Invalid Unit Price Records:", invalid_price)

# 10. Validate Total Sales
print("\n9. SALES VALIDATION")

total_sales = pd.to_numeric(
    df["Total_Sales"], errors="coerce"
)

expected_sales = quantity * unit_price

invalid_sales = int(
    (
        total_sales.isna()
        | ~((total_sales - expected_sales).abs() < 0.01)
    ).sum()
)

print("Incorrect Sales Calculations:", invalid_sales)

# 11. Validate Order Date
print("\n10. DATE VALIDATION")

order_date = pd.to_datetime(
    df["Order_Date"], errors="coerce"
)

invalid_dates = int(order_date.isna().sum())

print("Invalid Order Dates:", invalid_dates)

# 12. Check transformed date columns
print("\n11. TRANSFORMED DATE VALIDATION")

date_checks = {}

date_columns = {
    "Order_Year": order_date.dt.year,
    "Order_Month": order_date.dt.month,
    "Order_Day": order_date.dt.day,
    "Order_Month_Name": order_date.dt.month_name(),
    "Order_Day_Name": order_date.dt.day_name()
}

for column, expected in date_columns.items():

    if column in df.columns:

        actual = df[column]

        if column in ["Order_Year", "Order_Month", "Order_Day"]:
            actual = pd.to_numeric(actual, errors="coerce")
            mismatch = (
                actual.isna() | actual.ne(expected)
            )
        else:
            mismatch = (
                actual.astype("string").str.strip()
                != expected.astype("string")
            )

        date_checks[column] = int(mismatch.sum())

        print(
            column,
            "Mismatches:",
            date_checks[column]
        )

# 13. Generate validation report
print("\n12. VALIDATION SUMMARY")

validation_results = [
    ["Missing Values", missing_count],
    ["Duplicate Rows", duplicate_count],
    ["Invalid Age", invalid_age],
    ["Invalid Quantity", invalid_quantity],
    ["Invalid Unit Price", invalid_price],
    ["Incorrect Sales", invalid_sales],
    ["Invalid Order Dates", invalid_dates]
]

for column, count in date_checks.items():
    validation_results.append(
        [column + " Mismatches", count]
    )

report = pd.DataFrame(
    validation_results,
    columns=["Validation_Check", "Issue_Count"]
)

report["Status"] = report["Issue_Count"].apply(
    lambda x: "PASS" if x == 0 else "CHECK"
)

print(report)

# 14. Save validation report
Path("outputs").mkdir(
    parents=True,
    exist_ok=True
)

report.to_csv(
    "outputs/data_validation_report.csv",
    index=False
)

# 15. Save validated dataset
Path("data/processed").mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(
    "data/processed/validated_sales_dataset.csv",
    index=False
)

# 16. Final result
print("\n" + "=" * 55)

if report["Issue_Count"].sum() == 0:
    print("ALL VALIDATION CHECKS PASSED!")
else:
    print("VALIDATION COMPLETED - SOME ISSUES NEED REVIEW.")

print("Validation report saved successfully.")
print("Validated dataset saved successfully.")

print("\nFinal Dataset Shape:", df.shape)
print("DATA VALIDATION COMPLETED")
