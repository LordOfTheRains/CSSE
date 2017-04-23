from abc import ABCMeta, abstractmethod


class Operation:
    __metaclass__ = ABCMeta
    
    original = {}

    def __init__(self):
        self.remove_error_key()
    
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

    def remove_error_key(self):
        self.original.pop('error', None)
