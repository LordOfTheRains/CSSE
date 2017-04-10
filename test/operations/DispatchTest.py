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
        input_dict = {'name': 'BetelGeuse', 'date': '2016-01-17',
              'time': '03:15:42', 'op': 'predict'}
        expected = {'op': 'predict', 'body': 'Betelgeuse',
            'date': '2016-01-17', 'time': '03:15:42',
            'long': '75d53.6', 'lat': '7d24.3'}
        result = dispatcher.dispatch(input_dict)
        self.assertEqual(result, expected)
