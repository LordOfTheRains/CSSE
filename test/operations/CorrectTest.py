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
        # altititude xdyy.y
        # assumedLat xdyy.y
        # assumedLong xdyy.y
        expected = "mandatory information is missing"
        
        input_dict = {'op': 'correct', 'lat':"asdsad", 'long':"adsa",
                      'assumedLat': 'unknown', 'assumedLong': '2016-01-17',
                      'altitude': '03:15:99'}
        result = Correct.validate_parameter(input_dict)
        self.assertTrue(expected not in result)
