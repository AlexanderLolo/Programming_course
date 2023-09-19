class Hashtable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):

        return len(value.encode("utf-8")) % self.size

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

    def put(self, value):

        pos = self.seek_slot(value)
        if pos is None:
            return None
        self.slots[pos] = value
        return pos

    def find(self, value):

        pos = self.hash_fun(value)
        if self.slots[pos] == value:
            return pos

        newpos = pos + self.step
        while newpos % self.size != pos and self.slots[newpos] is not None:
            if self.slots[newpos] == value:
                return newpos
            newpos = (newpos + self.step) % self.size
        return None
