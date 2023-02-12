from sensor.logger import logging
from sensor.exception import SensorExcepion
import sys,os

def test():
     try :
          logging.info("Start the test")
          result = Somnath
          print(result)
          logging.info("End the test")
     except Exception as e:
          raise SensorExcepion(e, sys)
          logging.debug("Stopping")

if __name__ == "__main__":
     try :
          test()
     except Exception as e:
          print(e)
