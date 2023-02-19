import os,sys   
from datetime import datetime
from sensor.exception import SensorExcepion
from sensor.logger import logging

FILE_NAME = "sensor.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

class TraningPipelineConfig:

    def __init__(self):
        try: 
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')})")
        except Exception as e:
            raise SensorExcepion(e, sys)


class DataInjectionConfig:

    def __init__(self,trainingpipelineconfig:TraningPipelineConfig):
        try:
            self.database_name = "aps"
            self.collection_name = "sensor"
            self.data_injection_dir = os.path.join(trainingpipelineconfig.artifact_dir,"data_injection")
            self.feature_store_file_path = os.path.join(self.data_injection_dir,"feature_store",FILE_NAME)
            self.train_file_path = os.path.join(self.data_injection_dir,"dataset",TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_injection_dir,"dataset",TEST_FILE_NAME)
            self.test_size = 0.2
        except Exception as e:
            raise SensorExcepion(e, sys)

    def to_dict(self,)->dict:
        try:
            return self.__dict__
        except Exception as e :
            raise SensorExcepion(e, sys)


class DataValidationConfig:...
class DataTransformationConfig:...
class ModelTrainerConfig:...
class ModelEvaluateConfig:...
class ModelPusherConfig:...