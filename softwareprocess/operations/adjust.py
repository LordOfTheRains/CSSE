from operation import Operation
import re
import math


class Adjust(Operation):
    
    DEFAULT_TEMP = 72
    DEFAULT_PRESSURE = 1010
    DEFAULT_HEIGHT = 0
    DEFAULT_HORIZON = "natural"
    
    def __init__(self, param_dict):
        Operation.__init__(self)
        self.original = param_dict
        observation = param_dict['observation']
        x, y = observation.split("d")
        y = y.lstrip("0")
        self.observation_degree = int(x)
        self.observation_minute = float(y)
        
        if "height" in param_dict:
            self.height = float(param_dict['height'])
        else:
            self.height = self.DEFAULT_HEIGHT
        
        if "pressure" in param_dict:
            self.pressure = int(param_dict['pressure'])
        else:
            self.pressure = self.DEFAULT_PRESSURE
        
        if "temperature" in param_dict:
            self.temperature = int(param_dict['temperature'])
        else:
            self.temperature = self.DEFAULT_TEMP
            
        if "horizon" in param_dict:
            self.horizon = param_dict['horizon']
        else:
            self.horizon = self.DEFAULT_HORIZON
    
    @staticmethod
    def validate_parameter(param_dict=None):
        """
        this method will validate each input parameter. the validation includes type check and range check
        all appropriate errors shall be thrown within the implementation
        :return: boolean indicating success/failure
        """
        validated = True
        error = []
        if param_dict is None or not isinstance(param_dict, dict):
            error.append('No Valid Dictionary Provided')
            return ';'.join([str(x) for x in error])
        
        if "observation" in param_dict:
            observation = param_dict['observation']
            observation = re.match('^[0-9]+d[0-9]+.\d$', observation)
            if observation:
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
        else:
            validated = False
            error.append('Missing Observation Value in Dictionary')
            
        if "height" in param_dict:
            height = param_dict['height']
            try:
                height = float(height)
            except ValueError:
                error.append("Height Value Must Be A Floating Number")
                validated = False
            if height < 0:
                error.append("Height Value Must Be A Positive Floating Number")
                validated = False
                
        if "pressure" in param_dict:
            pressure = param_dict['pressure']
            try:
                pressure = int(pressure)
            except ValueError:
                error.append("Pressure Value Must Be A Integer")
                validated = False
            if pressure < 100:
                error.append("Pressure Value is Below the Threshold of 100 mbar")
                validated = False
            if not pressure < 1100:
                error.append("Pressure Value Exceed Threshold of 1100 mbar")
                validated = False
        
        if "temperature" in param_dict:
            temperature = param_dict['temperature']
            try:
                temperature = int(temperature)
            except ValueError:
                error.append("Temperature Value Must Be A Integer")
                validated = False
            if temperature < 20:
                error.append("Temperature Value is Below the Threshold of 20")
                validated = False
            if not temperature < 120:
                error.append("Temperature Value Exceed Threshold of 120")
                validated = False
        
        if "horizon" in param_dict:
            horizon = param_dict['horizon'].lower()
            if horizon != "natural" and horizon != "artificial":
                error.append("Not A Valid  Horizon  Value, Must be 'artificial' or 'natural'")
                validated = False
                
        if "altitude" in param_dict:
            error.append("Input Dictionary Contains Forbidden Parameter: altitude")
            validated = False
            
        if validated:
            return True
        else:
            return ';'.join([str(x) for x in error])
        
    def perform(self):
        """
        this method will perform the calculation for designated operation
        and attach the result as a key value pair to the original input dictionary
        :return: original dictionary + result key-value pair
        """
        if self.horizon.lower() == "natural":
            dip = (-0.97 * math.sqrt(self.height))/60
        else:
            dip = 0
        observed = self.observation_degree + self.observation_minute/60
        observed_radian = observed * math.pi/180
        refraction = ((-0.00452*self.pressure)/(273+(self.temperature-32)*5/9))/math.tan(observed_radian)
        adjusted = observed + dip + refraction
        degree = int(adjusted)
        minute = (adjusted - degree) * 60
        minute = round(minute, 1)
        if len(str(minute)) == 3:
            minute = "0" + str(minute)
        else:
            minute = str(minute)
        altitude = str(degree) + "d" + minute
        self.original['altitude'] = altitude
        return self.original
