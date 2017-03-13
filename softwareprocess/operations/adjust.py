from operation import Operation


class Adjust(Operation):
    
    def __init__(self, observation):
        Operation.__init__(self)
        
        self.observation = observation
        pass
    
    def validate_parameter(self):
        """
        this method will validate each input parameter. the validation includes type check and range check
        all appropriate errors shall be thrown within the implementation
        :return: boolean indicating success/failure
        """
        return True
    
    def perform(self):
        """
        this method will perform the calculation for designated operation
        and attach the result as a key value pair to the original input dictionary
        :return: original dictionary + result key-value pair
        """
        return {}
