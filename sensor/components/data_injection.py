from sensor import utils
from sensor.utils import get_collection_as_dataframe
from sensor.entity import config_entity,artifact_entity
from sensor.exception import SensorExcepion
from sensor.logger import logging
import os,sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

class DataInjection:
    def __init__( self,data_injection_config:config_entity.DataInjectionConfig):
        try:
            self.data_injection_config = data_injection_config
        except Exception as e:
            raise SensorExcepion(e, sys)

    def initiate_data_injection(self) -> artifact_entity.DataInjectionArtifact:
        try : 
            # Exporting collection data as Pandas dataframe 
            df:pd.DataFrame = utils.get_collection_as_dataframe(
                database_name = self.data_injection_config.database_name, 
                collection_name = self.data_injection_config.collection_name) 

            # replace na with NaN
            df.replace(to_replace= "na",value =np.NaN,inplace = True)

            # feature store

            
        except Exception as e:
            raise SensorExcepion(e, sys)