from __future__ import absolute_import

import unittest
from softwareprocess.operations.adjust import Adjust


class SampleTest(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_validate_parameter_observation(self):
        # observation: mandatory, unvalidated
        # string: xdy.y
        
        # Happy path
        # observation is in the form of xdy.y
        # 0 <= x < 90
        # 0.0 <= y < 60
        adjust = Adjust()
        self.assertTrue(adjust.validate_parameter(), "invalid input")
        pass
    
    def test_validate_parameter_height(self):
        pass
