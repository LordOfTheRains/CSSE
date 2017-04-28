from operation import Operation
from predict import Predict as predict
from adjust import  Adjust as adjust

import re


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
        longitude = param_dict['long']
        altitude = param_dict['altitude']
        assumedLat = param_dict['assumedLat']
        assumed_long = param_dict['assumedLong']
        
        # validate lat
        if type(lat) is not str:
            validated = False
            error.append('Latitude Must be A String Value')
        else:
            lat = re.match('^[-]?[0-9]+d[0-9]{1,2}.\d$', lat)
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
        
        # validate long
        if type(longitude) is not str:
            validated = False
            error.append('Longitude Must be A String Value')
        else:
            longitude = re.match('^[-]?[0-9]+d[0-9]{1,2}.\d$', longitude)
            if longitude:
                longitude = longitude.group()
                x, y = longitude.split("d")
                if int(x) < 0 or int(x) > 359:
                    validated = False
                    error.append('Longitude Out of Range: 0.0 <= long < 360.0')
                    
                # trim leading 0
                y = y.lstrip("0")
                if float(y) < 0.0 or not float(y) < 60:
                    validated = False
                    error.append('Longitude Minute Out of Range: 0 <= long < 60.0')
            else:
                validated = False
                error.append('Incorrect Longitude Format: xdyy.y')
        
        # validate assumedLong
        if type(assumed_long) is not str:
            validated = False
            error.append('Assumed Longitude Must be A String Value')
        else:
            assumed_long = re.match('^[-]?[0-9]+d[0-9]{1,2}.\d$', assumed_long)
            if assumed_long:
                assumed_long = assumed_long.group()
                x, y = assumed_long.split("d")
                if int(x) < 0 or int(x) > 359:
                    validated = False
                    error.append('Assumed Longitude Out of Range: 0.0 <= assumedLong < 360.0')
                    
                # trim leading 0
                y = y.lstrip("0")
                if float(y) < 0.0 or not float(y) < 60:
                    validated = False
                    error.append('Assumed Longitude Minute Out of Range: 0 <= assumedLong < 60.0')
            else:
                validated = False
                error.append('Incorrect Assumed Longitude Format: xdyy.y')
        
        if validated:
            return True
        else:
            return error
    
    def perform(self):
        pass
