# from linkedlist import LinkedList
class SetSet:
    def __init__(self, elements=None):
        self.size = 0
        self.elements = list()
        
        if elements is not None:
            for element in elements:
                self.add(element)
    
    def __contains__(self, element):
        return True if element in self.elements else False
    
    def __add__(self, element):
        if not self.contains(element):
            self.elements.append(element)
            self.size += 1

    def __remove__(self, element):
        if self.contains(element):
            self.elements.remove(element)
            self.size -= 1
        else:
            raise KeyError('element not found')

    def __union__(other_set):
        pass
    
    def __intersection__(other_set):
        pass
    
    def __difference__(other_set):
        pass
    
    def __is_subset__(other_set):
        pass
    

