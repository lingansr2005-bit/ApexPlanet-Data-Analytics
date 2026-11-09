import pandas as  pd 
from pathlib import Path
print("Data Transformation Started")
print("="*50)
df=pd.read_excel("data/processed/cleaned_sales_dataset.xlsx")
print("\n 1 Origianl Dataset")
print("Rows:",df.shape[0])
print("Columns:",df.shape[1])
print("\n 2 Standardizing Date Format")
df["Order_Date"]=pd.to_datetime(df["Order_Date"],errors="coerce")
invalid_dates=df["Order_Date"].isnull().sum()
print("Invalid Dates",invalid_dates)
if invalid_dates>0:
    raise ValueError("Invalid dates found. Please check the data")
print("Data format standardized successfully.")
print("\n 2 Extract Year ")
df["Order_Year"]=df["Order_Date"].dt.year
print("\ 3 Extract Month")
df["Order_Month"]=df["Order_Date"].dt.month
print("\n 4 Extract Month Name")
df["Order_Month_Name"]=df["Order_Date"].dt.month_name()
print("\n 5 Extract Day")
df["Order_Day"]=df["Order_Date"].dt.day
print("\n 6 Extract Day Name")
df["Order_Day_Name"]=df["Order_Date"].dt.day_name()
print("\n 7 Creating Revenue Categories")
df["Total_Sales"]=pd.to_numeric(df["Total_Sales"],errors="coerce")
if df["Total_Sales"].isnull().any():
    raise ValueError("Invalid or missing sales values found.")
df["Revenue_Category"] = pd.cut(
    df["Total_Sales"],
    bins=[-float("inf"), 10000, 50000, float("inf")],
    labels=["Low", "Medium", "High"],
    right=False
)
print("Revenue categories created successfully.")
print("\n9. TRANSFORMED DATA PREVIEW")
new_columns = [
    "Order_Year",
    "Order_Month",
    "Order_Month_Name",
    "Order_Day",
    "Order_Day_Name",
    "Total_Sales",
    "Revenue_Category"
]
print(df[new_columns].head(10))
print("\n10. FINAL DATASET INFORMATION")
print("Total Rows:", df.shape[0])
print("Total Columns:", df.shape[1])
Path("data/processed").mkdir(parents=True,exist_ok=True)
df.to_excel("data/processed/transformed_sales_dataset.xlsx",index=False)
df.to_csv("data/processed/transformed_sales_dataset.csv",index=False)
print("\n" + "=" * 50)
print("DATA TRANSFORMATION COMPLETED SUCCESSFULLY")
print("Transformed Excel file saved.")
print("Transformed CSV file saved.")
print("\nFinal dataset shape:", df.shape)
# Remove completely empty columns
df.dropna(axis=1, how="all", inplace=True)

print("\nEmpty columns removed successfully!")
print("Current dataset shape:", df.shape)

# Create processed folder
Path("data/processed").mkdir(parents=True, exist_ok=True)

# Save transformed dataset
df.to_excel(
    "data/processed/transformed_sales_dataset.xlsx",
    index=False
)

df.to_csv(
    "data/processed/transformed_sales_dataset.csv",
    index=False
)

print("\n" + "=" * 50)
print("DATA TRANSFORMATION COMPLETED SUCCESSFULLY")
print("Transformed Excel file saved.")
print("Transformed CSV file saved.")
print("\nFinal dataset shape:", df.shape)