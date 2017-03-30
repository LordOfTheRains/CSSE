from __future__ import absolute_import

import unittest
from softwareprocess.operations.predict import Predict


class PredictTest(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_constructor(self):
        pass
    
    def test_validate_parameter_body(self):
        # Body: mandatory, unvalidated
        # string of star name, must be
        # present in stars list
        
        # Sad Path
        
        # star not in dictionary
        expected_string = 'Missing Star Name in Dictionary'
        validated = Predict.validate_parameter({'nameee': 'Betelgeuse', 'date': '2016-01-17',
                                               'time': '03:15:42', 'op': 'predict'})
        self.assertTrue((expected_string in validated))
        
        # star not in star list
        expected_string = 'Star Name is Empty in Dictionary'
        validated = Predict.validate_parameter({'name': ' ', 'date': '2016-01-17',
                                               'time': '03:15:42', 'op': 'predict'})
        self.assertTrue((expected_string in validated))
        
        expected_string = 'Star Not Found on Star List'
        validated = Predict.validate_parameter({'name': 'Be--telgeuse', 'date': '2016-01-17',
                                               'time': '03:15:42', 'op': 'predict'})
        self.assertTrue((expected_string in validated))
        
        # Happy path
        
        # key exist
        validated = Predict.validate_parameter({'name': 'Betelgeuse', 'date': '2016-01-17',
                                               'time': '03:15:42', 'op': 'predict'})
        self.assertTrue(validated)
