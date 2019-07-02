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

    def test_add(self):
        array_set = SetSet()
        array_set.__add__(2)
        assert array_set.size == 1
        assert array_set.__contains__(2)
        array_set.__add__('E')
        assert array_set.size == 2
        assert array_set.__contains__('E')
        array_set.__add__(3)
        assert array_set.size == 3
        assert array_set.__contains__(3)

    def test_contains(self):
        array_set = SetSet()
        array_set.__add__('E')
        assert array_set.__contains__('E')
        array_set.__add__('F')
        assert array_set.__contains__('F')
        array_set.__remove__('E')
        assert not array_set.__contains__('E')
    
    def test_remove(self):
        array_set = SetSet()
        array_set.__add__(2)
        array_set.__add__(3)
        array_set.__add__(100)
        array_set.__remove__(100)
        assert not array_set.__contains__(100)
        assert array_set.size == 2
        array_set.__remove__(2)
        assert not array_set.__contains__(2)
        assert array_set.size == 1
        array_set.__remove__(3)
        assert not array_set.__contains__(3)
        assert array_set.size == 0
        
if __name__ == '__main__':
    unittest.main()