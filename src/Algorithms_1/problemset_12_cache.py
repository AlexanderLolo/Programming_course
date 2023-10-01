class NativeCache:
    def __init__(self, sz, stp=None):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        if stp is None:
            self.step = 3
        self.hits = [0] * self.size
        self.fulfilment = 0

    def hash_fun(self, value):

        randnum = 17
        result = 0
        for c in value:
            code = ord(c)
            result = (result * randnum + code) % self.size
        return result

    def find(self, value):

        pos = self.hash_fun(value)

        if self.slots[pos] is None:
            return None

        if self.slots[pos] == value:
            return pos

        newpos = (pos + self.step) % self.size
        while newpos != pos and self.slots[newpos] is not None:
            if self.slots[newpos] == value:
                return newpos
            newpos = (newpos + self.step) % self.size
        return None

    def is_key(self, key):

        return self.find(key) is not None

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

        if self.fulfilment == self.size:
            slot = self.hits.index(min(self.hits))
            self.slots[slot] = key
            self.values[slot] = value
            self.hits[slot] = 0
            return None
            # зачем реализовывать схемой разрешния коллизий

        slot = self.seek_slot(key)
        self.values[slot] = value
        self.slots[slot] = key
        self.fulfilment += 1
        return None

    def get(self, key):
        if not self.is_key(key):
            return None

        pos = self.find(key)
        self.hits[pos] += 1
        return self.values[pos]
