import pandas as pd
df=pd.read_excel("data/raw/ApexPlanet_DataAnalytics_Dataset11.xlsx")
print("Data Quality Assessment")
print("="*50)
print("\n Dataset dimensions")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("\n Missing Values Analysis")
missing_values = df.isnull().sum()
missing_report=pd.DataFrame({
    "Column":df.columns,
    "Missing_Values":missing_values.values,
    "Missing_Percentage":(missing_values.values/len(df)*100).round(2)
    })
print(missing_report)
print("\n3. DUPLICATE RECORD ANALYSIS")
duplicate_count = df.duplicated().sum()
print("Total duplicate rows:", duplicate_count)
print("\n DATA TYPE ANALYSIS")
print(df.dtypes)
print("\n TEXT FORMATTING ANALYSIS")
for column in df.select_dtypes(include="object").columns:
    text_data = df[column].dropna().astype(str)
    extra_spaces = (
        text_data != text_data.str.strip()).sum()
    print(column, "- Extra spaces:", extra_spaces)
print("\n  OUTLIER DETECTION")
numeric_columns = df.select_dtypes(include="number").columns
outlier_report = []
for column in numeric_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR
    outliers = df[
        (df[column] < lower_limit) |
        (df[column] > upper_limit)
    ]
    outlier_report.append({
        "Column": column,
        "Lower_Limit": lower_limit,
        "Upper_Limit": upper_limit,
        "Outlier_Count": len(outliers)
    })
    print(column, "- Outliers:", len(outliers))
    outlier_df = pd.DataFrame(outlier_report)

# Step 10: Save quality reports
missing_report.to_csv("outputs/missing_values_report.csv",index=False)
outlier_df.to_csv("outputs/outlier_report.csv",index=False)
print("\n" + "=" * 50)
print("DATA QUALITY ASSESSMENT COMPLETED")
print("Reports saved successfully!")
