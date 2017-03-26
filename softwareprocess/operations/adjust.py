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
        if param_dict is None or not isinstance(param_dict, dict):
            raise TypeError("No Valid Dictionary Provided")
        
        if "observation" not in param_dict:
            raise ValueError("Missing Observation Value in Dictionary")
        
        if "height" in param_dict:
            height = param_dict['height']
            try:
                height = float(height)
            except ValueError:
                raise ValueError("Height Value Must Be A Floating Number")
            if height < 0:
                raise ValueError("Height Value Must Be A Positive Floating Number")
                
        if "pressure" not in param_dict:
            raise ValueError("Missing Pressure Value in Dictionary")
        
        if "temperature" not in param_dict:
            raise ValueError("Missing Temperature Value in Dictionary")
        
        if "horizon" not in param_dict:
            raise ValueError("Missing Horizon Value in Dictionary")
        
        observation = param_dict['observation']
        #height = param_dict['height']
        #temperature = param_dict['temperature']
        #pressure = param_dict['pressure']
        #horizon = param_dict['horizon']
        
        return True
    
    def perform(self):
        """
        this method will perform the calculation for designated operation
        and attach the result as a key value pair to the original input dictionary
        :return: original dictionary + result key-value pair
        """
        return {}
