from sensor.logger import logging
from sensor.exception import SensorExcepion
import sys,os
from sensor.utils import get_collection_as_dataframe
from sensor.entity import config_entity
from sensor.entity.config_entity import DataInjectionConfig
from sensor.components.data_injection import DataInjection



if __name__ == "__main__":
     try :
        training_pipeline_config = config_entity.TraningPipelineConfig()
        data_injection_config = DataInjectionConfig(training_pipeline_config)
        print(data_injection_config.to_dict())
        data_injection = DataInjection(data_injection_config=data_injection_config)
        print(data_injection.initiate_data_injection())
     except Exception as e:
        SensorExcepion(e, sys)
