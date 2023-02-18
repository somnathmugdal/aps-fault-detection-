from sensor.logger import logging
from sensor.exception import SensorExcepion
from sensor.utils import get_collection_as_dataframe
import sys,os
from sensor.entity.config_entity import DataInjectionConfig
from sensor.entity import config_entity
from sensor.utils import get_collection_as_dataframe


if __name__ == "__main__":
     try :
         get_collection_as_dataframe(database_name= "aps", collection_name= "sensor")
     except Exception as e:
          print(e)
