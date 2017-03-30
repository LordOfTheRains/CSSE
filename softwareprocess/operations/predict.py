from operation import Operation
from softwareprocess.utility.stars import STARS
import re
import math


class Predict(Operation):
    DEFAULT_DATE = '2001-01-01'
    DEFAULT_TIME = "00:00:00"
    
    def __init__(self, param_dict):
        Operation.__init__(self)
    
    @staticmethod
    def validate_parameter(param_dict=None):
        validated = True
        error = []
        
        if "name" not in param_dict:
            validated = False
            error.append('Missing Star Name in Dictionary')
        else:
            star_name = param_dict['name']
            if star_name not in STARS:
                validated = False
                error.append('Star Not Found on Star List')
        
        if "date" in param_dict:
            pass
        
        if "time" in param_dict:
            pass
        
        if validated:
            return True
        else:
            return error
    
    def perform(self):
        return {}
