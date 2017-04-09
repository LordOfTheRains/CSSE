

class Angle:
    
    def __init__(self, hour_degree, minute_degree):
        """
        
        :param hour_degree:
        :param minute_degree:
        :returns: angle instance
        """
        pass
    
    @staticmethod
    def add(angle1=None, angle2=None):
        """
        angle1-angle2
        :param angle1: of angle instance
        :param angle2: '''
        :return: result angle
        """
        pass
    
    @staticmethod
    def multiply(angle1=None, num=None):
        """
        angle1*num(float
        :param angle1: angle
        :param num: float
        :return: result angle
        """
        pass
    
    @classmethod
    def from_string(cls, string=None):
        """
        returns angle converted form string
        :return:
        """
        validated = True
        error =[]
        angle_string = re.match('^[0-9]+d[0-9]+.\d$', string)
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
                    error.append('Observation minute must be float between GE 0.0 and LT 60.0.')
                if (int(x) == 360 or int(x) == -360) and float(y) > 0.0:
                    validated = False
                    error.append('Observation degree must be between -360d0.0 and 360d0.0')
            else:
                validated = False
                error.append('Invalid angle string')
            
        if not validated:
            raise ValueError(error)
    
    @classmethod
    def from_decimal(cls, decimal=None):
        """
        returns angle converted form decimal
        :return:
        """
        pass

