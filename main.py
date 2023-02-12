from sensor.logger import logging
from sensor.exception import SensorExcepion
from sensor.utils import get_collection_as_dataframe
import sys,os
from sensor.entity.config_entity import DataInjectionConfig
from sensor.entity import config_entity


if __name__ == "__main__":
     try :
          training_pipeline_config = config_entity.TraningPipelineConfig()
          data_injection_config = DataInjectionConfig(trainingpipelineconfig=training_pipeline_config)
          print(data_injection_config.to_dict())
     except Exception as e:
          print(e)
