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