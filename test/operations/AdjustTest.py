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
        expected_string = 'No Valid Dictionary Provided'
        validated = Adjust.validate_parameter()
        self.assertTrue((expected_string in validated))
        
        validated = Adjust.validate_parameter("asdad")
        self.assertTrue((expected_string in validated))
        
        # Happy path
        # parameter is a dictionary
        
        validated = Adjust.validate_parameter({'sss': '15d04.9', 'add': '6.0',
                                               'pressure': '1010', 'horizon': 'artificial',
                                               'op': 'adjust', 'temperature': '72'})
        self.assertFalse((expected_string in validated))
        
    def test_validate_parameter_observation(self):
        # observation: mandatory, unvalidated
        # string: xdy.y
        
        # Sad Path
        # missing key in the dictionary
        # observation is not in the form of xdy.y
        # x is out of range for these: 0 <= x < 90
        # y is out of range for these: 0.0 <= y < 60
        
        # missing key in the dictionary
        
        expected_string = 'Missing Observation Value in Dictionary'
        validated = Adjust.validate_parameter({'asd': '15d04.9', 'height': '6.0',
                                               'pressure': '1010', 'horizon': 'artificial',
                                               'op': 'adjust', 'temperature': '72'})
        self.assertTrue((expected_string in validated))
        
        # Happy path
        # observation key exist
        # observation is in the form of xdy.y
        # 0 <= x < 90
        # 0.0 <= y < 60
        
        # observation key exist
        validated = Adjust.validate_parameter({'observation': '15d04.9', 'height': '6.0',
                                               'pressure': '1010', 'horizon': 'artificial',
                                               'op': 'adjust', 'temperature': '72'})
        self.assertFalse((expected_string in validated))
        
    def test_validate_parameter_height(self):
        # height: optional, unvalidated
        # string in Float: default 0
        # >= 0
        
        # Sad Path
        
        # negative height
        
        expected_string = "Height Value Must Be A Positive Floating Number"
        with self.assertRaises(ValueError) as context:
            Adjust.validate_parameter({'observation': '15d04.9', 'height': '-123',
                                       'pressure': '1010', 'horizon': 'artificial',
                                       'op': 'adjust', 'temperature': '72'})
        self.assertEquals(expected_string, context.exception.args[0][0:len(expected_string)])
        #  height not a number
        expected_string = "Height Value Must Be A Floating Number"
        with self.assertRaises(ValueError) as context:
            Adjust.validate_parameter({'observation': '15d04.9', 'height': 'asdad',
                                       'pressure': '1010', 'horizon': 'artificial',
                                       'op': 'adjust', 'temperature': '72'})
        self.assertEquals(expected_string, context.exception.args[0][0:len(expected_string)])
        
        # Happy path
        
        # key exist
        self.assertTrue(Adjust.validate_parameter({'observation': '15d04.9', 'height': '6.0',
                                                   'pressure': '1010', 'horizon': 'artificial',
                                                   'op': 'adjust', 'temperature': '72'}))
    
    def test_validate_parameter_pressure(self):
        # pressure: optional, unvalidated
        # string in Integer: default 1100
        # >= 100, < 1100
        
        # Sad Path
        
        # pressure not an integer
        expected_string = "Pressure Value Must Be A Integer"
        with self.assertRaises(ValueError) as context:
            Adjust.validate_parameter({'observation': '15d04.9', 'height': '6.0',
                                       'pressure': '1010', 'horizon': 'artificial',
                                       'op': 'adjust', 'temperature': '72'})
        self.assertEquals(expected_string, context.exception.args[0][0:len(expected_string)])
        # pressure not an integer but a floating number
        expected_string = "Pressure Value Must Be A Integer"
        with self.assertRaises(ValueError) as context:
            Adjust.validate_parameter({'observation': '15d04.9', 'height': '6.0',
                                       'pressure': '1010.5', 'horizon': 'artificial',
                                       'op': 'adjust', 'temperature': '72'})
        self.assertEquals(expected_string, context.exception.args[0][0:len(expected_string)])
        # pressure not GE 100
        expected_string = "Pressure Value Is Under Threshold of 100 mbar"
        with self.assertRaises(ValueError) as context:
            Adjust.validate_parameter({'observation': '15d04.9', 'height': '6.0',
                                       'pressure': '80', 'horizon': 'artificial',
                                       'op': 'adjust', 'temperature': '72'})
        self.assertEquals(expected_string, context.exception.args[0][0:len(expected_string)])
        
        # pressure not less than 1100
        expected_string = "Pressure Value Exceed Threshold of 1100 mbar"
        with self.assertRaises(ValueError) as context:
            Adjust.validate_parameter({'observation': '15d04.9', 'height': '6.0',
                                       'pressure': '80000', 'horizon': 'artificial',
                                       'op': 'adjust', 'temperature': '72'})
        self.assertEquals(expected_string, context.exception.args[0][0:len(expected_string)])
        # Happy path
        
        # key exist
        self.assertTrue(Adjust.validate_parameter({'observation': '15d04.9', 'height': '6.0',
                                                   'pressure': '150', 'horizon': 'artificial',
                                                   'op': 'adjust', 'temperature': '72'}))
        
    def test_validate_parameter_temperature(self):
        # Temperature: optional, unvalidated
        # string in Integer: default 72
        # >= 20, < 120
        
        # Sad Path
        
        # missing key in the dictionary
        expected_string = "Missing Temperature Value in Dictionary"
        with self.assertRaises(ValueError) as context:
            Adjust.validate_parameter({'observation': '15d04.9', 'height': '6.0',
                                       'pressure': '1010', 'horizon': 'artificial',
                                       'op': 'adjust', 'temssssperature': '72'})
        self.assertEquals(expected_string, context.exception.args[0][0:len(expected_string)])
        
        # Happy path
        
        # key exist
        self.assertTrue(Adjust.validate_parameter({'observation': '15d04.9', 'height': '6.0',
                                                   'pressure': '1010', 'horizon': 'artificial',
                                                   'op': 'adjust', 'temperature': '72'}))
        
    def test_validate_parameter_horizon(self):
        # Horizon: optional, unvalidated
        # string, case sensitive: default 'natural'
        #  "artificial" or "natural".
        
        # Sad Path
        
        # missing key in the dictionary
        expected_string = "Missing Horizon Value in Dictionary"
        with self.assertRaises(ValueError) as context:
            Adjust.validate_parameter({'observation': '15d04.9', 'height': '6.0',
                                       'pressure': '1010', 'horisszon': 'artificial',
                                       'op': 'adjust', 'temperature': '72'})
        self.assertEquals(expected_string, context.exception.args[0][0:len(expected_string)])
        
        # Happy path
        
        # key exist
        self.assertTrue(Adjust.validate_parameter({'observation': '15d04.9', 'height': '6.0',
                                                   'pressure': '1010', 'horizon': 'artificial',
                                                   'op': 'adjust', 'temperature': '72'}))
