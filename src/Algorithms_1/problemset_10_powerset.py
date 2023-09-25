class PowerSet:

    def __init__(self):
        self.slots = {}

    def size(self):
        return len(self.slots)

    def put(self, value):

        if value not in self.slots.keys():
            self.slots[value] = None
        return None

    def get(self, value):

        # возвращает True если value имеется в множестве,
        # иначе False

        if value in self.slots.keys():
            return True
        return False

    def remove(self, value):

        if value in self.slots.keys():
            self.slots.pop(value)
            return True
        return False

    def intersection(self, set2):

        intersect = PowerSet()
        for element in set2.slots.keys():
            if element in self.slots.keys():
                intersect.put(element)
        return intersect

    def union(self, set2):
        # объединение текущего множества и set2
        unionset = PowerSet()
        for element in self.slots.keys():
            unionset.put(element)

        for element in set2.slots.keys():
            if element not in self.slots.keys():
                unionset.put(element)
        return unionset

    def difference(self, set2):
        # разница текущего множества и set2
        diffset = PowerSet()
        for element in self.slots.keys():
            diffset.put(element)

        for element in set2.slots.keys():
            if element in self.slots.keys():
                diffset.remove(element)
        return diffset
    
    def issubset(self, set2):
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        for element in set2.slots.keys():
            if element not in self.slots.keys():
                return False
        return True
