from operation import Operation
import re
import math


class Predict(Operation):
    
    DEFAULT_DATE = '2001-01-01'
    DEFAULT_TIME = "00:00:00"
    
    def __init__(self, param_dict):
        Operation.__init__(self)
        
    @staticmethod
    def validate_parameter(param_dict=None):
        pass
    
    def perform(self):
        pass
