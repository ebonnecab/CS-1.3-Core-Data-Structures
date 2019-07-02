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

    def test_union(self):
        set_one = SetSet([1,100,2,45])
        assert set_one.size == 4
        set_two = SetSet([20,4,3])
        set_one.__union__(set_two)
        assert set_one.size == 7
        assert set_one.__contains__(4)
        set_three = SetSet([5,2,25,1,122])
        set_one.__union__(set_three)
        assert set_one.size == 10
        assert set_three.__contains__(2)
    
    def test_intersection(self):
        set_one = SetSet([5, 100, 2])
        set_two = SetSet([5,4,2,3,200])
        set_set = SetSet(set_one.__intersection__(set_two))
        assert set_set.__contains__(5)
        assert set_set.size == 2
        set_1 = SetSet(['E', 'B', 'O'])
        set_2 = SetSet(['A','E','C'])
        set_set2 = SetSet(set_1.__intersection__(set_2))
        assert set_set2.__contains__('E')
        assert set_set2.size == 1

    def test_difference(self):
        set_one = SetSet(['A','B', 'Z'])
        set_two = SetSet(['C', 'A', 'E', 'B', 'F', 'R'])
        set_set = set_one.__difference__(set_two)
        assert set_set.__contains__('R')
        assert set_set.elements == ['C', 'E', 'F', 'R']
        set_1 = SetSet([1,2,4,100])
        set_2 = SetSet([1,2,4,25,100])
        set_set2 = set_1.__difference__(set_2)
        assert set_set2.__contains__(25)
        assert set_set2.elements == [25] 

if __name__ == '__main__':
    unittest.main()