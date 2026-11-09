ApexPlanet Data Analytics – Task 1

Project Overview

This project is part of the ApexPlanet Data Analytics Internship – Task 1.

The main objective of this project is to perform data exploration, data quality assessment, data cleaning, data transformation, data validation, and final dataset export using Python.

The project uses a sales dataset containing customer information, product details, order dates, quantities, and sales values.

Objectives

- Understand the structure of the dataset.
- Perform initial data exploration.
- Create a data dictionary.
- Identify missing values and outliers.
- Clean the dataset.
- Transform and prepare data for analysis.
- Validate the final dataset.
- Export the processed dataset into CSV and Excel formats.

Technologies Used

- Python
- Pandas
- NumPy
- OpenPyXL
- Visual Studio Code
- Microsoft Excel

Project Folder Structure

ApexPlanet_Data_Analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── outputs/
├── reports/
├── scripts/
├── venv/
└── README.md

Project Workflow

1. Data Exploration

Script: "01_data_exploration.py"

- Load the original dataset.
- Display the first and last records.
- Understand dataset dimensions.
- Examine column names and data types.
- Generate basic statistical information.

2. Data Dictionary

Script: "02_data_dictionary.py"

- Identify dataset columns.
- Understand data types.
- Generate a data dictionary.
- Export the dictionary as a CSV file.

3. Data Quality Assessment

Script: "03_data_quality.py"

- Identify missing values.
- Calculate missing value percentages.
- Check duplicate records.
- Examine dataset quality.

4. Data Cleaning

Script: "04_data_cleaning.py"

- Handle missing values.
- Remove duplicate records.
- Correct data types.
- Perform data cleaning.
- Export cleaned datasets.

5. Data Transformation

Script: "05_data_transformation.py"

- Extract year from order date.
- Extract month number and month name.
- Extract day and day name.
- Create revenue categories.
- Generate additional analytical columns.

6. Data Validation

Script: "06_data_validation.py"

- Validate the processed dataset.
- Check data consistency.
- Verify required columns.
- Perform validation checks.

7. Final Data Export

Script: "07_final_export.py"

- Perform final dataset cleanup.
- Check duplicate records.
- Export the final dataset.
- Generate project summary and documentation.

Dataset Information

- Original dataset: Excel format
- Original records: 1,000
- Original columns: 12
- Final records: 1,000
- Final columns: 19

Final Output Files

The project generates the following files:

Processed Dataset ("data/processed/")

- "cleaned_sales_dataset.csv"
- "cleaned_sales_dataset.xlsx"
- "transformed_sales_dataset.csv"
- "transformed_sales_dataset.xlsx"
- "final_sales_dataset.csv"
- "final_sales_dataset.xlsx"

Reports ("outputs/")

- "data_dictionary.csv"
- "data_validation_report.csv"
- "missing_values_report.csv"
- "outlier_report.csv"

Documentation ("reports/")

- "project_documentation.txt"
- "project_summary.csv"

Installation and Execution

Step 1: Install Python Libraries

pip install pandas numpy openpyxl

Step 2: Activate Virtual Environment

Windows PowerShell:

.\venv\Scripts\Activate.ps1

Step 3: Execute Python Programs

Run the programs in the following order:

python scripts/01_data_exploration.py

python scripts/02_data_dictionary.py

python scripts/03_data_quality.py

python scripts/04_data_cleaning.py

python scripts/05_data_transformation.py

python scripts/06_data_validation.py

python scripts/07_final_export.py

Project Results

The project successfully processed the sales dataset.

- Original dataset contained 1,000 records and 12 columns.
- Final dataset contains 1,000 records and 19 columns.
- Duplicate records in the final dataset: 0.
- Cleaned, transformed, and validated datasets were exported.
- Project summary and documentation files were generated.

Conclusion

This project provided practical experience in Python-based data analytics. It covered the complete data preprocessing workflow, starting from initial data exploration to final dataset validation and export.

The final processed dataset is ready for further analysis and visualization using tools such as Microsoft Excel and Power BI.

Author

Lingaraj S.

ApexPlanet Data Analytics Internship – Task 1