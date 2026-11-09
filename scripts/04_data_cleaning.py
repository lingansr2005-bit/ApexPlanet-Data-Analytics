import pandas as pd
df=pd.read_excel("data/raw/ApexPlanet_DataAnalytics_Dataset11.xlsx")
print("Original Dataset")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("\n Missing Values Before Cleaning")
print(df.isnull().sum())
age_median = df["Age"].median()
df["Age"] = df["Age"].fillna(age_median)
print("\n Missind Age values Handled")
print("\n3. CLEANING CITY COLUMN")
city_mode=df["City"].mode()

if not city_mode.empty:
    most_common_city = city_mode[0]
    df["City"] = df["City"].fillna(most_common_city)
    print("Missing City values filled with:", most_common_city)
else:
    print("No available city value to use for filling.")
print("\n4. CLEANING TEXT FORMATTING")
text_columns = df.select_dtypes(include=["object", "string"]).columns

for column in text_columns:
    df[column] = df[column].apply(
        lambda value: value.strip()
        if isinstance(value, str)
        else value
    )
print("Unnecessary spaces removed.")
print("\n5. REMOVING DUPLICATE ROWS")
duplicates_before = df.duplicated().sum()
df = df.drop_duplicates()
print("Duplicate rows found:", duplicates_before)
print("Duplicate rows removed:", duplicates_before - df.duplicated().sum())
print("\n6. MISSING VALUES AFTER CLEANING")
print(df.isnull().sum())
print("\n7. DUPLICATES AFTER CLEANING")
print("Duplicate rows:", df.duplicated().sum())
from pathlib import Path
Path("data/processed").mkdir(
    parents=True,
    exist_ok=True
)
df.to_excel(
    "data/processed/cleaned_sales_dataset.xlsx",
    index=False
)
df.to_csv(
    "data/processed/cleaned_sales_dataset.csv",
    index=False
)
print("\n" + "=" * 50)
print("DATA CLEANING COMPLETED SUCCESSFULLY")
print("Final rows:", df.shape[0])
print("Final columns:", df.shape[1])
print("\nCleaned files saved successfully!")