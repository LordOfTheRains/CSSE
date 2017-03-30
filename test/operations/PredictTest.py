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
        # Body: mandatory, dictionary type checked. value unvalidated
        # string of star name, must be
        # present in stars list
        
        # Sad Path
        
        # star not in dictionary
        expected_string = 'Missing Star Name in Dictionary'
        validated = Predict.validate_parameter({'nameee': 'Betelgeuse', 'date': '2016-01-17',
                                               'time': '03:15:42', 'op': 'predict'})
        self.assertTrue((expected_string in validated))
        
        # star not in star list
        
        expected_string = 'Star Not Found on Star List'
        validated = Predict.validate_parameter({'name': 'Be--telgeuse', 'date': '2016-01-17',
                                               'time': '03:15:42', 'op': 'predict'})
        self.assertTrue((expected_string in validated))
        
        # Happy path
        
        # key exist
        validated = Predict.validate_parameter({'name': 'Betelgeuse', 'date': '2016-01-17',
                                               'time': '03:15:42', 'op': 'predict'})
        self.assertTrue(validated)
        
        # case insensitive
        validated = Predict.validate_parameter({'name': 'BetelGeuse', 'date': '2016-01-17',
                                               'time': '03:15:42', 'op': 'predict'})
        self.assertTrue(validated)
        
    def test_validate_parameter_date(self):
        # Date: optional,  unvalidated
        # date string in format: yyyy-mm-dd
        # yyyy > = 2001
        # default to 2001-01-01
        
        # Sad Path
        
        # incorrect date format
        expected_string = 'Incorrect Date Format: Must be yyyy-mm-dd'
        validated = Predict.validate_parameter({'nameee': 'Betelgeuse', 'date': '2016-1-17',
                                               'time': '03:15:42', 'op': 'predict'})
        self.assertTrue((expected_string in validated))
        
        # date below minimum of 2001
        
        expected_string = 'Date Out of Range: Date Must be at least 2001'
        validated = Predict.validate_parameter({'name': 'Be--telgeuse', 'date': '2000-01-17',
                                               'time': '03:15:42', 'op': 'predict'})
        self.assertTrue((expected_string in validated))
        
        # not leap year
        
        expected_string = 'Date Out of Range: Date Must be at least 2001'
        validated = Predict.validate_parameter({'name': 'Be--telgeuse', 'date': '2001-02-30',
                                               'time': '03:15:42', 'op': 'predict'})
        self.assertTrue((expected_string in validated))
        
        # Happy path
        
        # valid date
        validated = Predict.validate_parameter({'name': 'Betelgeuse', 'date': '2016-01-17',
                                               'time': '03:15:42', 'op': 'predict'})
        self.assertTrue(validated)
        
        # case insensitive
        validated = Predict.validate_parameter({'name': 'BetelGeuse', 'date': '2016-01-17',
                                               'time': '03:15:42', 'op': 'predict'})
        self.assertTrue(validated)
        
        # default value
        validated = Predict.validate_parameter({'name': 'BetelGeuse', 'dsadate': '2016-01-17',
                                               'time': '03:15:42', 'op': 'predict'})
        self.assertTrue(validated)
