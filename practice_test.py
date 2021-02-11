import unittest
from times_two import TimesTwo

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

class TestTimesTwo(unittest.TestCase):

    def test_times_two(self):
        test_number = TimesTwo(4)
        self.assertEqual(test_number.times_two(),8)

if __name__ == '__main__':
    unittest.main()