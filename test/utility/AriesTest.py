from __future__ import absolute_import

import unittest
from datetime import datetime as Time
from softwareprocess.utility.aries import Aries


class AriesTest(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_get_greenwich_hour_angle(self):
        """
        internal and validated inputs
        :return:
        """
        gha = Aries.get_greenwich_hour_angle(2016, 1, 17,
                                             3, 15, 42)
        self.assertEqual(gha, "164d54.5")
        pass
