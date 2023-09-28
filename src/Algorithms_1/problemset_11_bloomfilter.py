class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = 0
        # создаём битовый массив длиной f_len ...

    def hash1(self, str1):
        randnum = 17
        result = 0
        for c in str1:
            code = ord(c)
            result = (result * randnum + code) % self.filter_len
        return 2 ** result

    def hash2(self, str1):
        randnum = 223
        result = 0
        for c in str1:
            code = ord(c)
            result = (result * randnum + code) % self.filter_len
        return 2 ** result

    def add(self, str1):

        self.filter = self.filter | self.hash1(str1) | self.hash2(str1)
        return None

    def is_value(self, str1):
        if (self.hash1(str1) & self.filter) and (self.hash2(str1) & self.filter) != 0:
            return True
        return False
