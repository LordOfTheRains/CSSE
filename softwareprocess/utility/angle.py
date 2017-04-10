import re
import math

class Angle:
    
    def __init__(self, hour_degree, minute_degree):
        """
        
        :param hour_degree:
        :param minute_degree:
        :returns: angle instance
        """
        if minute_degree < 0:
            raise ValueError("minute Degree has to be positive")
        
        self.hour_degree = int(hour_degree)
        self.minute_degree = float(minute_degree)
        self.str = str(hour_degree) + "d" + str(minute_degree)
        if '-' in str(hour_degree):
            self.is_negative = True
            self.decimal = (self.hour_degree - self.minute_degree/60)/360
            
        else:
            self.decimal = (self.hour_degree + self.minute_degree/60)/360
        
    @staticmethod
    def add(angle1=None, angle2=None):
        """
        angle1-angle2
        :param angle1: of angle instance
        :param angle2: '''
        :return: result angle
        """
        return Angle.from_decimal(angle1.decimal + angle2.decimal)
    
    @staticmethod
    def multiply(angle=None, num=None):
        """
        angle1*num(float
        :param angle: angle
        :param num: float
        :return: result angle
        """
        rounded = round(angle.decimal, 3)
        print("adsadasdsa")
        print(angle.decimal)
        print(rounded)
        return Angle.from_decimal(rounded * num)
    
    @classmethod
    def from_string(cls, string=None):
        """
        returns angle converted form string
        :return:
        """
        validated = True
        error = []
        hr_degree = 0
        minute_degree = 0
        angle_string = re.match('^[-]?[0-9]+d[0-9]+.[0-9]+$', string)
        if angle_string:
                observation = angle_string.group()
                x, y = observation.split("d")
                if int(x) < -360 or int(x) > 360:
                    validated = False
                    error.append('Observation degree must be between -360 and 360')
                    
                # trim leading 0
                y = y.lstrip("0")
                if float(y) < 0.0 or not float(y) < 60:
                    validated = False
                    error.append('angle minute must be float between GE 0.0 and LT 60.0.')
                if (int(x) == 360 or int(x) == -360) and float(y) > 0.0:
                    validated = False
                    error.append('Observation degree must be between -360d0.0 and 360d0.0')
                if validated:
                    hr_degree = x
                    minute_degree = y
        else:
            validated = False
            error.append('Invalid angle string')
                
        if not validated:
            raise ValueError(error)
        else:
            return Angle(hr_degree, minute_degree)
    
    @classmethod
    def from_decimal(cls, decimal=None):
        """
        returns angle converted form decimal
        :return:
        """
        floated = float(decimal)
        
        (left, right) = str(decimal).split(".")
        
        hrs = int(math.floor(float(right)*360.0))
        
        (left, right) = str(float(hrs)).split(".")
        
        minute_part = round(float(right)*60, 1) # keep decimal part
        return Angle(hrs, minute_part)

