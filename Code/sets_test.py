from sets import SetSet
import unittest

class SetSetTest(unittest.TestCase):

    def test_init(self):
        array_set = SetSet()
        assert array_set.size == 0

    def test_init_with_list(self):
        array_set = SetSet(['A','B', 'D', 'F'])
        assert array_set.size == 4
        assert array_set.__contains__('D') is True
    
    def test_size(self):
        array_set = SetSet()
        assert array_set.size == 0
        array_set.__add__(2)
        assert array_set.size == 1
        array_set.__add__(3)
        assert array_set.size == 2
        array_set.__remove__(3)
        assert array_set.size == 1

if __name__ == '__main__':
    unittest.main()