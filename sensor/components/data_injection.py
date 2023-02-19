from sensor import utils
from sensor.utils import get_collection_as_dataframe
from sensor.entity import config_entity,artifact_entity
from sensor.exception import SensorExcepion
from sensor.logger import logging
import os,sys
import pandas as pd
import numpy as np
from sklearn.model_selection  import train_test_split

class DataInjection:
    def __init__( self,data_injection_config:config_entity.DataInjectionConfig):
        try:
            logging.info(f"{'>>'*20} Data Ingestion {'<<'*20}")
            self.data_injection_config = data_injection_config
        except Exception as e:
            raise SensorExcepion(e, sys)

    def initiate_data_injection(self) -> artifact_entity.DataInjectionArtifact:
        try : 
            logging.info(f"Exporting collection data as pandas dataframe ")
            # Exporting collection data as Pandas dataframe 
            df:pd.DataFrame = utils.get_collection_as_dataframe(
                database_name = self.data_injection_config.database_name, 
                collection_name = self.data_injection_config.collection_name) 

            # replace na with NaN
            df.replace(to_replace= "na",value =np.NaN,inplace = True)

            
            logging.info("Save data in feature store")
            # saving data in feature 
            logging.info("Create feature store folder if not available")
            # Creating feature store if not available
            feature_store_dir = os.path.dirname(self.data_injection_config.feature_store_file_path)
            os.makedirs(feature_store_dir, exist_ok=True)

            logging.info("save df to feature store")
            # save df to feature store
            df.to_csv(path_or_buf=self.data_injection_config.feature_store_file_path,index=False,header= True)            
            
            logging.info("Split dataset into train-test set")
            # Split dataset into train-test set
            train_df,test_df = train_test_split(df,test_size=self.data_injection_config.test_size,random_state=42)
            
            logging.info("Create dataset directory folder if not available")
            #Create dataset directory folder if not available
            dataset_dir = os.path.dirname(self.data_injection_config.train_file_path)
            os.makedirs(dataset_dir,exist_ok=True)
            
            logging.info("save df to feature store folder")
            #save df to feature store folder
            train_df.to_csv(path_or_buf= self.data_injection_config.train_file_path,index=True,header=False)
            test_df.to_csv(path_or_buf= self.data_injection_config.test_file_path,index=True,header=False)

            #prepare artifact 
            data_injection_artifact = artifact_entity.DataInjectionArtifact(
                feature_store_file_path=self.data_injection_config.feature_store_file_path,
                train_file_path = self.data_injection_config.train_file_path,
                test_file_path = self.data_injection_config.test_file_path
            )
            logging.info(f"Data Injection Artifact : {data_injection_artifact}")
            return data_injection_artifact
        
        except Exception as e:
            raise SensorExcepion(error_message=e, errro_details =sys)