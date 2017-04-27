from __future__ import absolute_import

import unittest
from softwareprocess.operations.correct import Correct


class AriesTest(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_validate_parameter_mandatory_information(self):
        # tests following mandatory parameter presence
        # lat xdyy.y
        # long xdyy.y
        # altitude xdyy.y
        # assumedLat xdyy.y
        # assumedLong xdyy.y
        expected = "mandatory information is missing"
        
        # happy path
        # all parameter present
        input_dict = {'op': 'correct', 'lat': "asdsad", 'long': "adsa",
                      'assumedLat': 'unknown', 'assumedLong': '2016-01-17',
                      'altitude': '03:15:99'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue(expected not in result)
        
        # sad path
        # missing lat
        
        input_dict = {'op': 'correct', 'lat1': "asdsad", 'long': "adsa",
                      'assumedLat': 'unknown', 'assumedLong': '2016-01-17',
                      'altitude': '03:15:99'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue(expected in result)

        # missing long
        input_dict = {'op': 'correct', 'lat': "asdsad", 'long1': "adsa",
                      'assumedLat': 'unknown', 'assumedLong': '2016-01-17',
                      'altitude': '03:15:99'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue(expected in result)
        
        # missing altitude
        input_dict = {'op': 'correct', 'lat': "asdsad", 'long': "adsa",
                      'assumedLat': 'unknown', 'assumedLong': '2016-01-17',
                      'altitude1': '03:15:99'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue(expected in result)
        
        # missing assumedLat
        input_dict = {'op': 'correct', 'lat': "asdsad", 'long': "adsa",
                      'assumed1Lat': 'unknown', 'assumedLong': '2016-01-17',
                      'altitude': '03:15:99'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue(expected in result)
        
        # missing assumedLong
        input_dict = {'op': 'correct', 'lat': "asdsad", 'long': "adsa",
                      'assumedLat': 'unknown', 'assumed1Long': '2016-01-17',
                      'altitude': '03:15:99'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue(expected in result)
