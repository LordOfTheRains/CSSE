import unittest
import convertString2DictionaryTest

suite = unittest.TestLoader().loadTestsFromTestCase(TestConvertString2Dictionary)
TextTestRunner(verbosity=2).run(suite)
