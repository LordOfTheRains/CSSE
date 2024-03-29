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
        angle1 = Angle.from_string("100d4.8")
        print("********")
        print(angle1.decimal)
        angle2 = Angle.from_string("64d49.7")
        print(angle2.decimal)
        result = Angle.add(angle1, angle2)
        print(result.decimal)
        self.assertEqual(result.str, "164d54.5")
        
        angle1 = Angle.from_string("100d4.8")
        angle2 = Angle.from_string("-1d0.0")
        result = Angle.add(angle1, angle2)
        self.assertEqual(result.str, "99d4.8")
        
        angle1 = Angle.from_string("100d4.8")
        angle2 = Angle.from_string("-0d1.0")
        result = Angle.add(angle1, angle2)
        self.assertEqual(result.str, "100d3.7")
        
        angle1 = Angle.from_string("-100d4.8")
        angle2 = Angle.from_string("-64d49.7")
        result = Angle.add(angle1, angle2)
        self.assertEqual(result.str, "-164d54.5")
    
    def test_multiply(self):
        
        angle = Angle.from_string("0d59.0")
        result = Angle.multiply(angle, 3)
        self.assertEqual(result.str, "2d56.9")
        
        angle = Angle.from_string("-0d59.0")
        result = Angle.multiply(angle, -3)
        self.assertEqual(result.str, "2d56.9")
        
        angle = Angle.from_string("-1d0.0")
        result = Angle.multiply(angle, 3)
        self.assertEqual(result.str, "-2d59.9")
        
        angle = Angle.from_string("-0d59.0")
        result = Angle.multiply(angle, -3)
        self.assertEqual(result.str, "2d56.9")
        
    def test_get_angle_from_decimal(self):
        """
        internal and not validated, mandatory
        returns angle isntance from the decimal
        :return:
        """
        angle = Angle.from_decimal(16.180079)
        self.assertEqual(angle.hour_degree, 64)
        self.assertEqual(angle.minute_degree, 49.7)
        
        angle = Angle.from_decimal(-16.180079)
        self.assertEqual(angle.hour_degree, -64)
        self.assertEqual(angle.minute_degree, 49.7)
        
        pass
    
    def test_get_angle_from_string(self):
        """
        internal and not validated, mandatory
        returns angle isntance from the string
        :return:
        """
        
        angle = Angle.from_string("164d54.5")
        self.assertEqual(angle.hour_degree, 164)
        self.assertEqual(angle.minute_degree, 54.5)
        self.assertAlmostEqual(angle.decimal, 0.458, places=3)
        
        angle = Angle.from_string("64d49.7")
        self.assertEqual(angle.hour_degree, 64)
        self.assertEqual(angle.minute_degree, 49.7)
        self.assertAlmostEqual(angle.decimal, 0.180, places=3)
        
        angle = Angle.from_string("-64d49.7")
        self.assertEqual(angle.hour_degree, -64)
        self.assertEqual(angle.minute_degree, 49.7)
        self.assertAlmostEqual(angle.decimal, -0.180, places=3)
        pass
