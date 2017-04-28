from operation import Operation
from predict import Predict as predict
from adjust import  Adjust as adjust

import re
from datetime import date

class Correct(Operation):
    
    MANDATORY_PARAMS = ['lat', 'long', 'altitude', 'assumedLat', 'assumedLong']
    
    def __init__(self, param_dict):
        pass
    
    @staticmethod
    def validate_parameter(param_dict=None):
        validated = True
        error = []
        
        if not Operation.check_mandatory_param(param_dict, Correct.MANDATORY_PARAMS):
            return "mandatory information is missing"
        
        lat = param_dict['lat']
        long = param_dict['long']
        altitude = param_dict['altitude']
        assumedLat = param_dict['assumedLat']
        assumedLong = param_dict['assumedLong']
        
        # validate lat
        if type(lat) is not str:
            validated = False
            error.append('Incorrect Latitude Format: xdyy.y')
        else:
            lat = re.match('^[0-9]+d[0-9]+.\d$', lat)
            if lat:
                lat = lat.group()
                x, y = lat.split("d")
                if int(x) < -89 or int(x) > 89:
                    validated = False
                    error.append('Latitude Out of Range: -90.0 < lat < 90.0')
                    
                # trim leading 0
                y = y.lstrip("0")
                if float(y) < 0.0 or not float(y) < 60:
                    validated = False
                    error.append('Latitude Minute Out of Range: 0 <= lat < 60.0')
            else:
                validated = False
                error.append('Incorrect Latitude Format: xdyy.y')
        
        if validated:
            return True
        else:
            return error
    
    def perform(self):
        pass
