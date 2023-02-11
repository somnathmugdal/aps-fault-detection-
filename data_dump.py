import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

# Database Name
Database_Name = "aps"

# Collection Name
Collection_Name = "sensor"

#Data File Path
Data_file_path = "/config/workspace/aps_failure_training_set1.csv"

if  __name__ == "__main__":
    df = pd.read_csv(Data_file_path)
    print(f"Rows & Columns : {df.shape}")

# Convert dataframe to JSON to dump the data into MongoDB
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

# Insert Converted json data to MongoDB
    client[Database_Name][Collection_Name].insert_many(json_record)
