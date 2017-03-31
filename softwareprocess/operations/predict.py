from operation import Operation
from softwareprocess.utility.stars import STARS
import re
import math
from datetime import date


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
            input_date = param_dict['date']
            input_date = re.match('^2[0-9]{3}-[0-9]{2}-[0-9]{2}$', input_date)
            
            if input_date:
                input_date = input_date.group()
                (year, month, day) = input_date.split('-')
                year = int(year)
                month = int(month)
                day = int(day)
                if year < 2001:
                    validated = False
                    error.append('Date Out of Range: Date Must be at least 2001')
                else:
                    try:
                        date(year, month, day)
                    except ValueError:
                        validated = False
                        error.append('Invalid Date')
            else:
                validated = False
                error.append('Incorrect Date Format: Must be yyyy-mm-dd')
        
        if "time" in param_dict:
            input_time = param_dict['time']
            input_time = re.match('^[0-9]{2}:[0-9]{2}:[0-9]{2}$', input_time)
            
            if input_time:
                input_time = input_time.group()
                (hour, minute, second) = input_time.split(':')
                hour = int(hour)
                minute = int(minute)
                second = int(second)
                if hour > 23 or minute > 59 or second > 59:
                    validated = False
                    error.append('Invalid Time')
            else:
                validated = False
                error.append('Incorrect Time Format: Must be hh:mm:ss')
        
        if validated:
            return True
        else:
            return error
    
    def perform(self):
        return {}
