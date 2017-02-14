import unittest
import convertString2Dictionary as converter

class TestConvertString2Dictionary(unittest.TestCase):

    def test_convertString2Dictionary(self):

        s1 = "abc%3D123"
        d1 = {'abc':'123'}
        s2 = "function%3D%20calculatePosition%2C%20sighting%3DBetelgeuse"
        d2 = {'function':'calculatePosition', 'sighting':'Betelgeuse'}
        s3 = "function%3D%20calc11latePosition%2C%20si123141ting%3DB123"
        d3 = {'function':'calc11latePosition', 'si123141ting':'B123'}

        self.assertEqual(d1,converter.convertString2Dictionary(s1))
        self.assertEqual(d2,converter.convertString2Dictionary(s2))
        self.assertEqual(d3,converter.convertString2Dictionary(s3))

        #negative cases
        invalid = ['key%3Dvalue%2C%20key%3Dvalue',
                    'key%3Dkey%3Dkey%3D',
                     'function%20%3D%20get_stars',
                    'value',
                    '1key%3Dvalue',
                    '1key%3D%3Dvalue',
                    'k%20e%20y%20%3D%20value',
                    'k%20%20y%20%3D%20va%3D%3Dlue',
                    '',
                    'key1%3Dvalue%3B%20key2%3Dvalue']

        error = converter.error_dict()
        for s in invalid:
            self.assertEqual(error,converter.convertString2Dictionary(s),
             s+':'+ str(converter.convertString2Dictionary(s)))

    def test_is_valid_key(self):
        valid = ['a1223','asd23q']
        invalid = ['hello world',
                    'asd!@# sadsa',
                    '000a90ad',
                    '.asdc9',
                    '88j asd']

        for key in valid:
            self.assertTrue(converter.is_valid_key(key),'['+key+ ']')

        for key in invalid:
            self.assertFalse(converter.is_valid_key(key),'['+key+ ']')

    def test_is_valid_value(self):
        valid = ['123ahsuds',
                'asd112',
                'a2s12s',
                'keyasd',
                'as1da']
        invalid = ['hela lo world',
                    '==asdsads+!@#a',
                    '00% 0a90ad',
                    '.asdc9',
                    '88j asd']

        for value in valid:
            self.assertTrue(converter.is_valid_value(value),'['+value+']')

        for value in invalid:
            self.assertFalse(converter.is_valid_value(value),value)

if __name__ == '__main__':
    unittest.main()
