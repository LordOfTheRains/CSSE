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
            error.append('Invalid [lat] Value')
        else:
            lat = re.match('^[0-9]+d[0-9]+.\d$', lat)
            
        
            if lat:
                observation = observation.group()
                x, y = observation.split("d")
                if int(x) < 0 or int(x) > 89:
                    validated = False
                    error.append('Observation degree must be integer between 0 and 89. inclusive')
                    
                # trim leading 0
                y = y.lstrip("0")
                if float(y) < 0.0 or not float(y) < 60:
                    validated = False
                    error.append('Observation minute must be float between GE 0.0 and LT 60.0.')
                if int(x) == 0 and float(y) < 0.1:
                    validated = False
                    error.append('Observation value cannot be less than 0d0.1')
            else:
                validated = False
                error.append('Invalid Observation Value in Dictionary')
        
        if validated:
            return True
        else:
            return error
    
    def perform(self):
        pass
