class NativeDictionary:
    def __init__(self, sz, stp=None):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        if stp is None:
            self.step = 3

    def hash_fun(self, value):

        return len(value.encode("utf-8")) % self.size

    def find(self, value):

        pos = self.hash_fun(value)

        if self.slots[pos] is None:
            return None

        if self.slots[pos] == value:
            return pos

        newpos = pos + self.step
        while newpos % self.size != pos and self.slots[newpos] is not None:
            if self.slots[newpos] == value:
                return newpos
            newpos = (newpos + self.step) % self.size
        return None

    def is_key(self, key):

        if self.find(key) is None:
            return False
        return True

    def seek_slot(self, value):

        pos = self.hash_fun(value)
        if self.slots[pos] is None:
            return pos

        if self.slots[pos] == value:
            return None

        newpos = pos + self.step
        while newpos % self.size != pos:
            if self.slots[newpos] is None:
                return newpos
            newpos = (newpos + self.step) % self.size
        return None

    def put(self, key, value):

        slot = self.find(key)
        if slot is not None:
            self.values[slot] = value
            return None

        slot = self.seek_slot(key)
        if slot is not None:
            self.values[slot] = value
            self.slots[slot] = key
        return None


    def get(self, key):

        if not self.is_key(key):
            return None
        return self.values[self.find(key)]
