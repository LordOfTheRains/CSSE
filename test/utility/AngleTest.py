from __future__ import absolute_import

import unittest
from softwareprocess.utility.angle import Angle


class AriesTest(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_constructor(self):
        """
        test correct constructor with usable fields
        :return:
        """
        
        pass
    
    def test_add(self):
        """
        test angle addition
        :return:
        """
        pass
    
    def test_get_angle_from_decimal(self):
        """
        internal and not validated, mandatory
        returns angle isntance from the decimal
        :return:
        """
        angle = Angle.from_decimal(16.180079)
        self.assertEqual(angle.hour_degree, 64)
        self.assertEqual(angle.minute_degree, 49.7)
        pass
    
    def test_get_angle_from_string(self):
        """
        internal and not validated, mandatory
        returns angle isntance from the string
        :return:
        """
        
        angle = Angle.from_string("164d54.5")
        self.assertEqual(angle.intger_part, "164")
        self.assertEqual(angle.decimal_part, "54.5")
        self.assertEqual(angle.decimal, )
        pass
