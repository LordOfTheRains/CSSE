from operation import Operation
from softwareprocess.utility.stars import STARS
import re
import math
import time


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
            date = param_dict['date']
            date = re.match('^2[0-9]{3}-[0-9]{2}-[0-9]{2}$', date)
            
            if date:
                date = date.group()
                (year, month, day) = date.split('-')
                print (year)
                print (month)
                print (day)
                if year < 2001:
                    validated = False
                    error.append('Date Out of Range: Date Must be at least 2001')
                else:
                    pass
            else:
                validated = False
                error.append('Incorrect Date Format: Must be yyyy-mm-dd')
        
        if "time" in param_dict:
            pass
        
        if validated:
            return True
        else:
            return error
    
    def perform(self):
        return {}
