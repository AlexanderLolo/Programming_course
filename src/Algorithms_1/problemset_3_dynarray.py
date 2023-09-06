import ctypes


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def get_capacity(self):
        return self.capacity

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, pos):
        if pos < 0 or pos >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[pos]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for el in range(self.count):
            new_array[el] = self.array[el]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, pos, itm):
        # Complexity O(n)
        if pos < 0 or pos > self.count:
            raise IndexError('Index is out of bounds')

        if self.count == self.capacity:
            self.resize(2*self.capacity)
        for el in range(self.count, pos, -1):
            self.array[el] = self.array[el-1]
        self.array[pos] = itm
        self.count += 1

    def delete(self, pos):
        # Complexity O(n). Instead of using resize method once element is deleted(creates two consecutive cycles),
        # the algorithm allows to create new array with one cycle
        if pos < 0 or pos >= self.count:
            raise IndexError('Index is out of bounds')

        new_capacity = self.capacity
        if (self.count - 1) * 2 < self.capacity:
            if int(self.capacity / 1.5) > 16:
                new_capacity = int(self.capacity / 1.5)
            else:
                new_capacity = 16

        new_array = self.make_array(new_capacity)
        for el in range(pos):
            new_array[el] = self.array[el]
        for el in range(pos + 1, self.count):
            new_array[el-1] = self.array[el]

        self.array = new_array
        self.capacity = new_capacity
        self.count -= 1
