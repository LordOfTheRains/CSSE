from abc import ABCMeta, abstractmethod


class Operation:
    __metaclass__ = ABCMeta
    
    original = {}
    
    def __init__(self):
        pass
    
    @staticmethod
    def validate_parameter(self):
        """
        this method will validate each input parameter. the validation includes type check and range check
        all appropriate errors shall be thrown within the implementation
        :return: boolean indicating success/failure
        """
        raise NotImplemented

    @abstractmethod
    def perform(self):
        """
        this method will perform the calculation for designated operation
        and attach the result as a key value pair to the original input dictionary
        :return: original dictionary + result key-value pair
        """
        raise NotImplemented

    @staticmethod
    def check_mandatory_param(input_dict, mandatory_param):
        for param in mandatory_param:
            if param not in input_dict:
                return False
        return True
