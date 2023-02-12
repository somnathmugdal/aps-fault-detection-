import pandas as pd
from sensor.config import mongo_client
from sensor.logger import logging
from sensor.exception import SensorExcepion
import os,sys

def get_collection_as_dataframe(database_name:str,collection_name:str) -> pd.DataFrame :
    """
    This Function returns collection as DataFrame
    database_name : database name 
    collection_name : collection name 
    =======================================
    retrun pandas dataframe of a collection 
    """
    try:
        logging.info(f"Reading data from database :{database_name} and collection :{collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found Columns :{df.columns}")

        if "_id" in df.columns :
            logging.info(f"Dropping Columns :_id")
            df = df.drop("_id",axis=1)
        
        logging.info(f"Rows & Columns in df : {df.shape}")
        return df   
    except Exception as e:
        raise SensorExcepion(e, sys)
    
