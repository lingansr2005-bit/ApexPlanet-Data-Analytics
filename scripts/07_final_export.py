
import pandas as pd
from pathlib import Path
from datetime import datetime

print("FINAL DATASET EXPORT STARTED")
print("=" * 55)

# 1. Define file paths
input_file = Path(
    "data/processed/validated_sales_dataset.csv"
)

processed_folder = Path("data/processed")
reports_folder = Path("reports")

# 2. Check input file
if not input_file.exists():
    raise FileNotFoundError(
        "Validated dataset not found. Run Program 6 first."
    )

# 3. Load validated dataset
df = pd.read_csv(input_file)

print("\n1. LOADING VALIDATED DATASET")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 4. Remove completely empty columns
df.dropna(axis=1, how="all", inplace=True)

print("\n2. FINAL DATASET CLEANUP")
print("Empty columns removed.")
print("Final shape:", df.shape)

# 5. Check duplicate records
duplicates = df.duplicated().sum()

print("\n3. DUPLICATE CHECK")
print("Duplicate rows:", duplicates)

# 6. Create output folders
processed_folder.mkdir(parents=True, exist_ok=True)
reports_folder.mkdir(parents=True, exist_ok=True)

# 7. Export final Excel file
excel_path = processed_folder / "final_sales_dataset.xlsx"

df.to_excel(
    excel_path,
    index=False
)

print("\nFinal Excel file exported.")

# 8. Export final CSV file
csv_path = processed_folder / "final_sales_dataset.csv"

df.to_csv(
    csv_path,
    index=False
)

print("Final CSV file exported.")

# 9. Read validation report if available
validation_file = Path(
    "outputs/data_validation_report.csv"
)

if validation_file.exists():

    validation_df = pd.read_csv(validation_file)

    validation_issues = int(
        validation_df["Issue_Count"].sum()
    )

else:
    validation_issues = None

# 10. Generate project summary
summary = {
    "Project": "ApexPlanet Data Analytics",
    "Dataset": "Sales Dataset",
    "Total Records": df.shape[0],
    "Total Columns": df.shape[1],
    "Duplicate Rows": int(duplicates),
    "Validation Issues": validation_issues,
    "Export Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "Final Excel": str(excel_path),
    "Final CSV": str(csv_path)
}

summary_df = pd.DataFrame(
    list(summary.items()),
    columns=["Description", "Details"]
)

# 11. Save project summary
summary_path = reports_folder / "project_summary.csv"

summary_df.to_csv(
    summary_path,
    index=False
)

# 12. Generate documentation
documentation = f"""
APEXPLANET DATA ANALYTICS PROJECT
=================================

PROJECT: Sales Data Analysis

OBJECTIVE:
To explore, clean, transform, validate and
prepare the sales dataset for further analysis.

DATASET INFORMATION:
Total Records: {df.shape[0]}
Total Columns: {df.shape[1]}

ACTIVITIES COMPLETED:
1. Data Exploration
2. Data Dictionary Creation
3. Data Quality Assessment
4. Data Cleaning
5. Data Transformation
6. Data Validation
7. Final Dataset Export

FINAL DATASET:
Excel: final_sales_dataset.xlsx
CSV: final_sales_dataset.csv

DATA QUALITY:
Duplicate Rows: {duplicates}
Validation Issues: {validation_issues}

CONCLUSION:
The sales dataset has been processed and
exported for further data analysis and reporting.

=================================
PROJECT COMPLETED
"""

documentation_path = reports_folder / "project_documentation.txt"

with open(documentation_path, "w", encoding="utf-8") as file:
    file.write(documentation)

# 13. Final output
print("\n" + "=" * 55)
print("FINAL EXPORT COMPLETED SUCCESSFULLY!")
print("=" * 55)

print("Final Excel:", excel_path)
print("Final CSV:", csv_path)
print("Project Summary:", summary_path)
print("Documentation:", documentation_path)

print("\nFinal Dataset Shape:", df.shape)
