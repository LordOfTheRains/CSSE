from __future__ import absolute_import

import unittest
from softwareprocess.operations.adjust import Adjust


class AdjustTest(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_validate_parameter_dictionary_exist(self):
        # observation: mandatory, unvalidated
        # string: xdy.y
        expected_string = "No Valid Dictionary Provided"
        with self.assertRaises(TypeError) as context:
            Adjust.validate_parameter()
        self.assertEquals(expected_string, context.exception.args[0][0:len(expected_string)])
        with self.assertRaises(TypeError) as context:
            Adjust.validate_parameter("asdad")
        self.assertEquals(expected_string, context.exception.args[0][0:len(expected_string)])
        # Happy path
        # observation is in the form of xdy.y
        # 0 <= x < 90
        # 0.0 <= y < 60
        try:
            Adjust.validate_parameter({'op': 'predict'})
        except TypeError:
            self.fail("valid dictionary should not raise type error")
            
    def test_validate_parameter_observation(self):
        # observation: mandatory, unvalidated
        # string: xdy.y
        
        # Happy path
        # observation is in the form of xdy.y
        # 0 <= x < 90
        # 0.0 <= y < 60
        self.assertTrue(Adjust.validate_parameter({'observation': '15d04.9', 'height': '6.0',
                                                   'pressure': '1010', 'horizon': 'artificial',
                                                   'op': 'adjust', 'temperature': '72'}))
        
        # Sad Path
        # missing key in the dictionary
        # observation is in the form of xdy.y
        # 0 <= x < 90
        # 0.0 <= y < 60
    
    def test_validate_parameter_height(self):
        pass
    
    def test_validate_parameter_pressure(self):
        pass
