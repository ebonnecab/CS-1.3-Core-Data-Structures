from sets import SetSet
import unittest

class SetSetTest(unittest.TestCase):

    def test_init(self):
        array_set = SetSet()
        assert array_set.size == 0

if __name__ == '__main__':
    unittest.main()