from __future__ import absolute_import

import unittest
from softwareprocess.operations import *
from softwareprocess import dispatch as dispatcher


class DispatchTest(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    # Acceptance tests
    
    def test_dispatch_valid_adjust(self):
        input_dict = {'observation': '30d1.5', 'height': '19.0',
                      'pressure': '1000', 'horizon': 'artificial',
                      'op': 'adjust', 'temperature': '85'}
        expected = {'altitude': '29d59.9', 'observation': '30d1.5',
                    'height': '19.0', 'pressure': '1000',
                    'horizon': 'artificial', 'op': 'adjust',
                    'temperature': '85'}
        result = dispatcher.dispatch(input_dict)
        self.assertEqual(result, expected)
        
        input_dict = {'observation': '45d15.2', 'height': '6',
                      'pressure': '1010', 'horizon': 'natural',
                      'op': 'adjust', 'temperature': '71'}
        expected = {'altitude': '45d11.9', 'observation': '45d15.2',
                    'height': '6', 'pressure': '1010',
                    'horizon': 'natural', 'op': 'adjust',
                    'temperature': '71'}
        
        result = dispatcher.dispatch(input_dict)
        self.assertEqual(result, expected)
        
        input_dict = {'observation': '42d0.0', 'op': 'adjust'}
        expected = {'altitude': '41d59.0', 'observation': '42d0.0', 'op': 'adjust'}
        result = dispatcher.dispatch(input_dict)
        self.assertEqual(result, expected)
        
        input_dict = {'observation': '42d0.0', 'op': 'adjust', 'extraKey': 'ignore'}
        expected = {'altitude': '41d59.0', 'observation': '42d0.0', 'op': 'adjust', 'extraKey': 'ignore'}
        result = dispatcher.dispatch(input_dict)
        self.assertEqual(result, expected)
    
    def test_dispatch_invalid_adjust(self):
        input_dict = {'op': 'adjust'}
        
        result = dispatcher.dispatch(input_dict)
        self.assertTrue("error" in result)
        
        input_dict = {'observation': '101d15.2',
                      'height': '6', 'pressure': '1010',
                      'horizon': 'natural', 'op': 'adjust',
                      'temperature': '71'}
        
        result = dispatcher.dispatch(input_dict)
        self.assertTrue("error" in result)
        
        input_dict = {'observation': '45d15.2', 'height': 'a',
                      'pressure': '1010', 'horizon': 'natural',
                      'op': 'adjust', 'temperature': '71'}
        
        result = dispatcher.dispatch(input_dict)
        self.assertTrue("error" in result)
        
        input_dict = {'observation': '45d15.2',
                      'height': '6', 'horizon': '   ',
                      'pressure': '1010', 'op': 'adjust',
                      'temperature': '71'}
        
        result = dispatcher.dispatch(input_dict)
        self.assertTrue("error" in result)
    
    # Predict Test
    def test_dispatch_valid_predict(self):
        input_dict = {'body': 'BetelGeuse', 'date': '2016-01-17',
              'time': '03:15:42', 'op': 'predict'}
        expected = {'op': 'predict', 'body': 'BetelGeuse',
            'date': '2016-01-17', 'time': '03:15:42',
            'long': '75d53.6', 'lat': '7d24.3'}
        result = dispatcher.dispatch(input_dict)
        self.assertEqual(result, expected)
        
        input_dict = {'name': 'BetelGeuse', 'time': '03:15:42', 'op': 'predict'}
        expected = {'op': 'predict', 'body': 'BetelGeuse', 'time': '03:15:42',
            'long': '75d53.6', 'lat': '7d24.3'}
        result = dispatcher.dispatch(input_dict)
        self.assertEqual(result, expected)
        
        input_dict = {'name': 'BetelGeuse', 'date': '2016-01-17', 'op': 'predict'}
        expected = {'op': 'predict', 'body': 'BetelGeuse', 'date': '2016-01-17',
            'long': '75d53.6', 'lat': '7d24.3'}
        result = dispatcher.dispatch(input_dict)
        self.assertEqual(result, expected)
        
    def test_dispatch_invalid_predict(self):
        input_dict = {'op': 'predict'}
        
        result = dispatcher.dispatch(input_dict)
        self.assertTrue("error" in result)
        
        input_dict = {'op': 'predict',
                      'body': 'unknow', 'date': '2016-01-17',
                      'time': '03:15:42', 'op': 'predict',
                      }
        
        result = dispatcher.dispatch(input_dict)
        self.assertTrue("error" in result)
        
        input_dict = {'op': 'predict',
                      'body': 'unknown', 'date': '2016-99-17',
                      'time': '03:15:42', 'op': 'predict',
                      }
        
        result = dispatcher.dispatch(input_dict)
        self.assertTrue("error" in result)
        
        input_dict = {'op': 'predict',
                      'body': 'unknown', 'date': '2016-01-17',
                      'time': '03:15:99', 'op': 'predict',
                      }
        
        result = dispatcher.dispatch(input_dict)
        self.assertTrue("error" in result)
        
        input_dict = {'op': 'predict', 'lat':"asdsad", 'long':"adsa",
                      'body': 'unknown', 'date': '2016-01-17',
                      'time': '03:15:99', 'op': 'predict',
                      }
        
        result = dispatcher.dispatch(input_dict)
        self.assertTrue("error" in result)
        
    def test_dispatch_valid_correct(self):
        
        
        
        input_dict = {'op': 'correct', 'long': "154d5.4", 'lat': "89d20.1",
                      'assumedLat': '35d59.7', 'assumedLong': '74d35.3',
                      'altitude': '37d17.4'}
        expected = {'op': 'correct', 'long': "154d5.4", 'lat': "89d20.1",
                    'assumedLat': '35d59.7', 'assumedLong': '74d35.3',
                    'altitude': '37d17.4', 'correctedDistance': '104',
                    'correctedAzimuth': '0d36.8'}
        result = dispatcher.dispatch(input_dict)
        self.assertEqual(expected, result, result)
        
        input_dict = {'op': 'correct', 'long': "95d41.6", 'lat': "16d32.3",
                      'assumedLat': '-53d38.4', 'assumedLong': '74d35.3',
                      'altitude': '13d42.3'}
        expected = {'op': 'correct', 'long': "95d41.6", 'lat': "16d32.3",
                    'assumedLat': '-53d38.4', 'assumedLong': '74d35.3',
                    'altitude': '13d42.3', 'correctedDistance': '-3950',
                    'correctedAzimuth': '164d43.1'}
        result = dispatcher.dispatch(input_dict)
        self.assertEqual(expected, result, result)
        
    def test_dispatch_invalid_correct(self):
        input_dict = {'op': 'correct'}
        
        result = dispatcher.dispatch(input_dict)
        self.assertTrue("error" in result, result)
        
        input_dict = {'op': 'correct', 'long': "95d41.6", 'lat': "16d32.3",
                      'assumedLat': '-53d38.4', 'assumedLong': '74d35.3',
                      'altitude': '13d42.3'}
        result = dispatcher.dispatch(input_dict)
        self.assertEqual(expected, result, result)
