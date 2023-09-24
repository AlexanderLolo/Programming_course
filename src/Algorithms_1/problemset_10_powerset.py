class PowerSet:

    def __init__(self):
        self.slots = {}

    def size(self):
        return len(self.slots)

    def put(self, value):

        if value not in self.slots.keys():
            self.slots[value] = None
        return None

    def remove(self, value):

        if value in self.slots.keys():
            self.slots.pop(value)
        return None

    def intersection(self, set2):

        intersect = {}
        for element in set2.slots.keys():
            if element in self.slots.keys():
                intersect[element] = None
        self.slots = intersect
        return None

    def union(self, set2):
        # объединение текущего множества и set2
        for element in set2.slots.keys():
            if element not in self.slots.keys():
                self.slots[element] = None
        return None

    def difference(self, set2):
        # разница текущего множества и set2
        for element in set2.slots.keys():
            if element in self.slots.keys():
                self.slots.pop(element)
        return None
    
    def issubset(self, set2):
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        for element in set2.slots.keys():
            if element not in self.slots.keys():
                return False
        return True
