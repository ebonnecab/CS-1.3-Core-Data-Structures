# from linkedlist import LinkedList
class SetSet:
    def __init__(self, elements=None):
        self.size = 0
        self.elements = list()
        
        if elements is not None:
            for element in elements:
                self.__add__(element)
    
    def __contains__(self, element):
        return True if element in self.elements else False
    
    def __add__(self, element):
        if not self.__contains__(element):
            self.elements.append(element)
            self.size += 1

    def __remove__(self, element):
        if self.__contains__(element):
            self.elements.remove(element)
            self.size -= 1
        else:
            raise KeyError('element not found')

    def __union__(self, other_set):
        for element in other_set.elements:
            if element not in self.elements:
                self.__add__(element)
        
        return self
    
    def __intersection__(self,other_set):
        new_array = []
        for element in self.elements:
            for element in other_set.elements:
                if element in self.elements and element in other_set.elements:
                    new_array.append(element)
        
        return new_array

                
    
    def __difference__(self, other_set):
        for element in self.elements:
            if element in other_set.elements:
                other_set.__remove__(element)
        
        return other_set
    
    def __is_subset__(other_set):
        pass
    

