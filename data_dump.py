
"""
Data Dump Script
-----------------
This script reads flight fare data from an Excel file and inserts it into
a MongoDB database.

Why this conversion is needed:
Excel stores data in a tabular format (rows and columns). MongoDB, however,
is a document-based database — it stores data as a collection of documents,
similar to a list of dictionaries in Python, where each document represents
one record (key-value pairs).

How the conversion works:
- df.to_json(orient="records") converts the DataFrame into a JSON string,
  where each row becomes a separate dictionary and all rows together form
  a list of dictionaries.
- json.loads() then parses that JSON string back into an actual Python
  list of dictionaries (since to_json() only returns a string, not a
  usable Python object).

This list of dictionaries is exactly the format insert_many() requires,
since that is how MongoDB stores and works with data.
"""




import pymongo
import json 
import pandas as pd

client=pymongo.MongoClient("mongodb+srv://salehasohail064_db_user:Pakistan123@cluster0.hqfxr5k.mongodb.net/?appName=Cluster0")

DATA_FILE_PATH=(r"D:\FareCast\FareCast\Data_Train.xlsx")
DATABASE_NAME="FlightFare"
COLLECTION_NAME="FlightFare_Project"

if __name__=="__main__":
    df=pd.read_excel(DATA_FILE_PATH)
    print(f"Rows and columns in dataset: {df.shape}")

    df.reset_index(drop=True,inplace=True)


    json_record=json.loads(df.to_json(orient="records"))
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)