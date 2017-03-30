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
        validated = Predict.validate_parameter({'name': 'Betelgeuse', 'date': '2016-01-17',
                                               'pressure': '80000', 'horizon': 'artificial',
                                               'op': 'predict', 'temperature': '9asdc'})
        self.assertTrue((expected_string in validated))
        
        # star not in star list
        
        # Happy path
        
        # key exist
        validated = Predict.validate_parameter({'observation': '15d04.9', 'height': '6.0',
                                               'pressure': '1010', 'horizon': 'artificial',
                                               'op': 'adjust', 'temperature': '72'})
        self.assertTrue(validated)
