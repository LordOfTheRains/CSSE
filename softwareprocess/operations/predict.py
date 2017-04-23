from operation import Operation
from softwareprocess.utility.stars import STARS
from softwareprocess.utility.angle import Angle
from softwareprocess.utility.aries import Aries

import re
from datetime import date


class Predict(Operation):
    DEFAULT_DATE = '2001-01-01'
    DEFAULT_TIME = "00:00:00"
    MANDATORY_PARAMS = ['body']
    
    def __init__(self, param_dict):
        Operation.__init__(self)
        self.original = param_dict
        
        self.body = param_dict['body'].lower().capitalize()
        if 'date' in param_dict:
            self.date = param_dict['date']
        else:
            self.date = self.DEFAULT_DATE
        
        if 'time' in param_dict:
            self.time = param_dict['time']
        else:
            self.time = self.DEFAULT_TIME
        self.sidereal = STARS[self.body]['sidereal']
        self.declination = STARS[self.body]['declination']
        
    @staticmethod
    def validate_parameter(param_dict=None):
        validated = True
        error = []
        
        if not Operation.check_mandatory_param(param_dict, Predict.MANDATORY_PARAMS):
            return "mandatory information is missing"
        
        if "lat" in param_dict or "long" in param_dict:
            validated = False
            error.append('[lat] or [long] key cannot be in Dictionary')
        
        if "body" not in param_dict:
            validated = False
            error.append('Missing Star Name in Dictionary')
        else:
            if type(param_dict['body']) is not str:
                validated = False
                error.append('Invalid Star Name')
            else:
                star_name = param_dict['body'].lower().capitalize()
                if star_name not in STARS:
                    validated = False
                    error.append('Star Not Found on Star List')
            
        if "date" in param_dict:
            input_date = param_dict['date']
            if type(input_date) is not str:
                validated = False
                error.append('Invalid Date Value')
            else:
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
            if type(input_time) is not str:
                validated = False
                error.append('Invalid Time Value')
            else:
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
        lat = Angle.from_string(self.declination)
        (year, month, day) = self.date.split("-")
        (hour, minute, sec) = self.time.split(":")
        year = int(year)
        month = int(month)
        day = int(day)
        hour = int(hour)
        minute = int(minute)
        sec = int(sec)
        star_gha = Aries.get_greenwich_hour_angle(year, month, day, hour, minute, sec)
        star_sha = Angle.from_string(self.sidereal)
        
        longitude = Angle.add(star_gha, star_sha)
        full_angle = Angle.from_string("-360d0.0")
        print ("star_gha.str")
        print (star_gha.str)
        if longitude.hour_degree > 360:
            longitude = Angle.add(longitude, full_angle)
        if longitude.hour_degree == 360 and longitude.minute_degree > 0:
            longitude = Angle.add(longitude, full_angle)
        print ("star_gha.str")
        print (longitude.str)
        self.original['lat'] = lat.str
        self.original['long'] = longitude.str
        return self.original
