from __future__ import absolute_import

import unittest
from softwareprocess.operations.adjust import Adjust


class AdjustTest(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_validate_parameter_dictionary_exist(self):
        # parameter must exist or  is dictionary
        expected_string = "No Valid Dictionary Provided"
        with self.assertRaises(TypeError) as context:
            Adjust.validate_parameter()
        self.assertEquals(expected_string, context.exception.args[0][0:len(expected_string)])
        with self.assertRaises(TypeError) as context:
            Adjust.validate_parameter("asdad")
        self.assertEquals(expected_string, context.exception.args[0][0:len(expected_string)])
        # Happy path
        # parameter is a dictionary
        type_error_not_raised = False
        try:
            Adjust.validate_parameter({'op': 'predict'})
        except Exception as exc:
            if exc is TypeError:
                type_error_not_raised = True
        self.assertFalse(type_error_not_raised, "valid dictionary should not raise type error")
        
    def test_validate_parameter_observation(self):
        # observation: mandatory, unvalidated
        # string: xdy.y
        
        # Sad Path
        # missing key in the dictionary
        # observation is not in the form of xdy.y
        # x is out of range for these: 0 <= x < 90
        # y is out of range for these: 0.0 <= y < 60
        
        # missing key in the dictionary
        expected_string = "Missing Observation Value in Dictionary"
        with self.assertRaises(ValueError) as context:
            Adjust.validate_parameter({'asd': '15d04.9', 'height': '6.0',
                                       'pressure': '1010', 'horizon': 'artificial',
                                       'op': 'adjust', 'temperature': '72'})
        self.assertEquals(expected_string, context.exception.args[0][0:len(expected_string)])
        
        # Happy path
        # observation key exist
        # observation is in the form of xdy.y
        # 0 <= x < 90
        # 0.0 <= y < 60
        
        # observation key exist
        self.assertTrue(Adjust.validate_parameter({'observation': '15d04.9', 'height': '6.0',
                                                   'pressure': '1010', 'horizon': 'artificial',
                                                   'op': 'adjust', 'temperature': '72'}))
        
    def test_validate_parameter_height(self):
        # height: mandatory, unvalidated
        # string: xdy.y
        
        # Sad Path
        # missing key in the dictionary
        # observation is not in the form of xdy.y
        # x is out of range for these: 0 <= x < 90
        # y is out of range for these: 0.0 <= y < 60
        
        # missing key in the dictionary
        expected_string = "Missing Height Value in Dictionary"
        with self.assertRaises(ValueError) as context:
            Adjust.validate_parameter({'observation': '15d04.9', 'heisdght': '6.0',
                                       'pressure': '1010', 'horizon': 'artificial',
                                       'op': 'adjust', 'temperature': '72'})
        self.assertEquals(expected_string, context.exception.args[0][0:len(expected_string)])
        
        # Happy path
        # height key exist
        # observation is in the form of xdy.y
        # 0 <= x < 90
        # 0.0 <= y < 60
        
        # height key exist
        self.assertTrue(Adjust.validate_parameter({'observation': '15d04.9', 'height': '6.0',
                                                   'pressure': '1010', 'horizon': 'artificial',
                                                   'op': 'adjust', 'temperature': '72'}))
        pass
    
    def test_validate_parameter_pressure(self):
        pass
