from __future__ import absolute_import

import unittest
from softwareprocess.operations.adjust import Adjust


class SampleTest(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_validate_parameter_dictionary_exist(self):
        # observation: mandatory, unvalidated
        # string: xdy.y
        
        # Happy path
        # observation is in the form of xdy.y
        # 0 <= x < 90
        # 0.0 <= y < 60
        self.assertRaises(TypeError, Adjust.validate_parameter())
        pass
    
    def test_validate_parameter_observation(self):
        # observation: mandatory, unvalidated
        # string: xdy.y
        
        # Happy path
        # observation is in the form of xdy.y
        # 0 <= x < 90
        # 0.0 <= y < 60
        //self.assertRaises(TypeError, Adjust.validate_parameter())
        pass
    
    def test_validate_parameter_height(self):
        pass
