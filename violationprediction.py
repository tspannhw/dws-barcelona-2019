import datetime
import math
import random, string
from time import gmtime, strftime
import os
import time
import numpy as np

# Predict based on 7 args/features
#
def predict(args):
  
  driver_certification = args["driver_certification"]
  driver_wageplan = args["driver_wageplan"]
  fatigue_by_hours = args["fatigue_by_hours"]
  fatigue_by_miles = args["fatigue_by_miles"]
  foggy_weather = args["foggy_weather"]
  rainy_weather = args["rainy_weather"]
  windy_weather = args["windy_weather"]
  
  probabilityOfViolation = np.random.randint(2, size=1)[0]
  
  result = { probabilityOfViolation }

  return result
