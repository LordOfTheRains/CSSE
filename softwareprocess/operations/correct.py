from operation import Operation
from predict import Predict as predict
from adjust import  Adjust as adjust

import re
from datetime import date

class Correct(Operation):
    
    MANDATORY_PARAMS = ['body']
    
    def __init__(self, param_dict):
        pass
    
    @staticmethod
    def validate_parameter(param_dict=None):
        
        
        pass
    
    def perform(self):
        pass
