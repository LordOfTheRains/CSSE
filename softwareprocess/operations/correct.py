from operation import Operation
from predict import Predict as predict
from adjust import  Adjust as adjust

import re
from datetime import date

class Correct(Operation):
    
    MANDATORY_PARAMS = ['lat', 'long', 'altitude', 'assumedLat', 'assumedLong']
    
    def __init__(self, param_dict):
        pass
    
    @staticmethod
    def validate_parameter(param_dict=None):
        validated = True
        error = []
        
        if not Operation.check_mandatory_param(param_dict, Correct.MANDATORY_PARAMS):
            return "mandatory information is missing"
        
        if validated:
            return True
        else:
            return error
    
    def perform(self):
        pass
