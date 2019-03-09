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

  driver_certification = args.get("driver_certification")
  driver_wageplan = args.get("driver_wageplan")
  fatigue_by_hours = args.get("fatigue_by_hours")
  fatigue_by_miles = args.get("fatigue_by_miles")
  foggy_weather = args.get("foggy_weather")
  rainy_weather = args.get("rainy_weather")
  windy_weather = args.get("windy_weather")
  
  probabilityOfViolation = np.random.randint(2, size=1)[0]
  
  # {
  #"success": true,
  #"response": {
  #  "violation": 1
  #}
  #}

  violation = { probabilityOfViolation }

  return violation
