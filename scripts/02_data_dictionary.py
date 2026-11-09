import pandas as pd
df=pd.read_excel("data/raw/ApexPlanet_DataAnalytics_Dataset11.xlsx")
description={  "Order_ID": "Unique identification of an order",
    "Order_Date": "Date when the order was placed",
    "Customer_ID": "Identification number of the customer",
    "Customer_Name": "Name of the customer",
    "Age": "Age of the customer",
    "Gender": "Gender of the customer",
    "City": "City where the customer is located",
    "Product": "Name of the purchased product",
    "Category": "Category of the purchased product",
    "Quantity": "Number of products purchased",
    "Unit_Price": "Price of one product unit",
    "Total_Sales": "Total sales amount of the order"}
relevance={ "Order_ID": "Order tracking",
    "Order_Date": "Sales trend analysis",
    "Customer_ID": "Customer identification",
    "Customer_Name": "Customer information",
    "Age": "Customer segmentation",
    "Gender": "Customer demographic analysis",
    "City": "Location-based analysis",
    "Product": "Product performance analysis",
    "Category": "Category-wise sales analysis",
    "Quantity": "Sales volume analysis",
    "Unit_Price": "Product pricing analysis",
    "Total_Sales": "Revenue analysis"}
dictionary_data=[]
for column in  df.columns:
    column_info = {
        "Column Name":column,
        "Data_Type":str(df[column].dtype),
        "Description":description.get(column, "desccription not Defined"),
        "Business_Relevance":relevance.get(column, "Relevance not defined"),
        "Missing_Values":df[column].isnull().sum(),
        "Unique_Values":df[column].nunique(),
    }
    dictionary_data.append(column_info)
    data_dictionary=pd.DataFrame(dictionary_data)
    print(data_dictionary)
    data_dictionary.to_csv(  "outputs/data_dictionary.csv",index=False)
    print("\nData Dictionary created successfully!")
    print("File saved in outputs/data_dictionary.csv")