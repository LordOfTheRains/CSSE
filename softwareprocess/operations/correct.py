from operation import Operation
from softwareprocess.utility.angle import Angle

import re
import math

class Correct(Operation):
    
    MANDATORY_PARAMS = ['lat', 'long', 'altitude', 'assumedLat', 'assumedLong']
    
    def __init__(self, param_dict):
        Operation.__init__(self)
        self.original = param_dict
        
        self.lat = param_dict['lat']
        self.longitude = param_dict['long']
        self.altitude = param_dict['altitude']
        self.assumed_lat = param_dict['assumedLat']
        self.assumed_long = param_dict['assumedLong']
    
    @staticmethod
    def validate_parameter(param_dict=None):
        validated = True
        error = []
        
        if not Operation.check_mandatory_param(param_dict, Correct.MANDATORY_PARAMS):
            return "mandatory information is missing"
        
        if 'correctedDistance' in param_dict or 'correctedAzimuth' in param_dict:
            return "Input Dictionary Contains Forbidden Parameter: correctAzimuth/correctedDistance"
        
        lat = param_dict['lat']
        longitude = param_dict['long']
        altitude = param_dict['altitude']
        assumed_lat = param_dict['assumedLat']
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
        
        # validate assumedLat
        if type(assumed_lat) is not str:
            validated = False
            error.append('Assumed Latitude Must be A String Value')
        else:
            assumed_lat = re.match('^[-]?[0-9]+d[0-9]{1,2}.\d$', assumed_lat)
            if assumed_lat:
                assumed_lat = assumed_lat.group()
                x, y = assumed_lat.split("d")
                if int(x) < -89 or int(x) > 89:
                    validated = False
                    error.append('Assumed Latitude Out of Range: -90.0 < assumedLat < 90.0')
                    
                # trim leading 0
                y = y.lstrip("0")
                if float(y) < 0.0 or not float(y) < 60:
                    validated = False
                    error.append('Assumed Latitude Minute Out of Range: 0 <= assumedLat < 60.0')
            else:
                validated = False
                error.append('Incorrect Assumed Latitude Format: xdyy.y')
        
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
                
        # validate altitude
        if type(altitude) is not str:
            validated = False
            error.append('Altitude Must be A String Value')
        else:
            altitude = re.match('^[-]?[0-9]+d[0-9]{1,2}.\d$', altitude)
            if altitude:
                altitude = altitude.group()
                x, y = altitude.split("d")
                if int(x) < 0 or int(x) > 89:
                    validated = False
                    error.append('Altitude Out of Range: 0.0 < altitude < 90.0')
                    
                # trim leading 0
                y = y.lstrip("0")
                if float(y) < 0.0 or not float(y) < 60:
                    validated = False
                    error.append('Altitude Minute Out of Range: 0 <= altitude < 60.0')
                    
                if int(x) == 0 and float(y) < 0.1:
                    validated = False
                    error.append('Altitude value cannot be less than 0d0.1')
            else:
                validated = False
                error.append('Incorrect Altitude Format: xdyy.y')
        
        if validated:
            return True
        else:
            return error
    
    def perform(self):
        lat = Angle.from_string(self.lat)
        longitude = Angle.from_string(self.longitude)
        assumed_lat = Angle.from_string(self.assumed_lat)
        assumed_long = Angle.from_string(self.assumed_long)
        altitude = Angle.from_string(self.altitude)
        
        lha = Angle.add(longitude, assumed_long)
        print('lha:' + lha.str)
        
        sin_lat = math.sin(math.radians(lat.decimal*360))
        cos_lat = math.cos(math.radians(lat.decimal*360))
        sin_assumed_lat = math.sin(math.radians(assumed_lat.decimal*360))
        cos_assumed_lat = math.cos(math.radians(assumed_lat.decimal*360))
        cos_lha = math.cos(math.radians(lha.decimal*360))
        inter_distance = sin_lat*sin_assumed_lat + cos_lat *cos_assumed_lat * cos_lha
        
        corrected_altitude = math.asin(inter_distance)/math.pi*180/360
        corrected_altitude = Angle.from_decimal(-corrected_altitude)
        
        corrected_distance = Angle.add(altitude, corrected_altitude)
        
        self.original['correctedDistance'] = int(corrected_distance.decimal*60*360)
        # corrected azimuth
        cos_arcsin_inter_dist = math.cos(math.radians(corrected_altitude.decimal*360))
        
        numerator = (sin_lat - (sin_assumed_lat * inter_distance))
        denom = cos_assumed_lat * cos_arcsin_inter_dist
        corrected_az = math.acos(numerator/denom) # radians
        corrected_az_degree = corrected_az/math.pi * 180 / 360
        corrected_azimuth = Angle.from_decimal(corrected_az_degree)
        print(corrected_az_degree)
