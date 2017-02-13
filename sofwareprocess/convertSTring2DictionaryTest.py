import unittest


class TestConvertString2Dictionary(unittest.TestCase):


    def test_validateInput(self):
        s1 = "aksjdlakjdlka"
		self.assertTrue(s1, isValidInput())
'''
    def test_validateInput(self):
        #s2 = "function%3D%20calculatePosition%2C%20sighting%3DBetelgeuse"
		#s3 = "abc%3D123"
		#self.assertTrue(s2, isValidInput())
		#self.assertTrue(s3, isValidInput())
		#bad inputs
		s4 = "key%3Dvalue%2C%20key%3Dvalue"
		s5 = "key%3D"
		s6 = "value"

		self.assertTrue(s4, isValidInput())
		self.assertTrue(s5, isValidInput())
		self.assertTrue(s6, isValidInput())
'''


    def test_convertString2Dictionary(self):
        pass


if __name__ == '__main__':
    unittest.main()
