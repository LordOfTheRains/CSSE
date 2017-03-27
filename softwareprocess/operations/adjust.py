from operation import Operation


class Adjust(Operation):
    
    def __init__(self, observation):
        Operation.__init__(self)
        
        self.observation = observation
        pass
    
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
        
        if "observation" not in param_dict:
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
            horizon = param_dict['horizon']
            if horizon != "natural" or horizon != "artificial":
                error.append("Not A Valid  Horizon  Value, Must be 'artificial' or 'natural'")
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
        return {}
