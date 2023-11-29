class aBST:


    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        self.tree_size = 2 ** (depth + 1) - 1
        self.Tree = [None] * self.tree_size # массив ключей

    def FindKeyIndex(self, key):
        # ищем в массиве индекс ключа
        index = 0
        while index <= self.tree_size:
            if self.Tree[index] is None: # если элемент отсутствует и его можно добавить то вазвращаем отрицательный индес
                return -1 * index

            if self.Tree[index] == key:
                return index

            if key < self.Tree[index]:
                index = 2 * index + 1
                continue

            if key > self.Tree[index]:
                index = 2 * index + 2
                continue
        return None # элемент не найден и его нельзя добавить так как массив уже полон

    def AddKey(self, key):
        # если весь массив уже полони элемиент в нем отсутствует
        inverted_index = self.FindKeyIndex(key)
        if inverted_index is None:
            return -1

        index_to_add_with = inverted_index * -1

        # если в массив можно добавить элемент и он в нем отсутствует
        if index_to_add_with > 0:
            self.Tree[index_to_add_with] = key
            return index_to_add_with

        # если в массиве уже присутствует этот элемент
        if index_to_add_with < 0:
            return -1 * index_to_add_with

        # индекс может быть только “0”. Отдельно обрабатываем случай корня, так как неясно отсутствует элемент или нет
        if self.Tree[index_to_add_with] is None:
            self.Tree[index_to_add_with] = key
        return index_to_add_with
    