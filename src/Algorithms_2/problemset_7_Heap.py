class Heap:

    def __init__(self):
        self.HeapArray = [] # хранит неотрицательные числа-ключи

    def MakeHeap(self, list_of_keys, depth):
    # создаём массив кучи HeapArray из заданного
    # размер массива выбираем на основе глубины depth
        heap_size = 2 ** (depth + 1) - 1
        self.HeapArray = [None] * heap_size

        for key in list_of_keys:
            self.Add(key)

    def GetMax(self):

        if len(self.HeapArray) == 0 or self.HeapArray[0] is None:
            return -1 # если куча пуста

        # вычисляем последний элемент
        last_index = len(self.HeapArray) - 1
        while last_index > 0 and self.HeapArray[last_index] is None:
            if self.HeapArray[last_index] is None:
                last_index -= 1

        max_value = self.HeapArray[0]
        if last_index == 0:
            self.HeapArray[0] = None
            return max_value

        self.HeapArray[0] = self.HeapArray[last_index]
        self.HeapArray[last_index] = None

        self.change_with_bigger_child(0)
        return max_value


    def change_with_bigger_child(self, index):

        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        index_of_max_elem = index

        if (left_child_index < len(self.HeapArray)
            and self.HeapArray[left_child_index] is not None
            and self.HeapArray[left_child_index] > self.HeapArray[index_of_max_elem]):
            index_of_max_elem = left_child_index

        if (right_child_index < len(self.HeapArray)
            and self.HeapArray[right_child_index] is not None
            and self.HeapArray[right_child_index] > self.HeapArray[index_of_max_elem]):
            index_of_max_elem = right_child_index

        if index_of_max_elem != index:
            self.HeapArray[index_of_max_elem], self.HeapArray[index] = self.HeapArray[index], self.HeapArray[index_of_max_elem]
            self.change_with_bigger_child(index_of_max_elem)


    def Add(self, key):
        # добавляем новый элемент key в кучу и перестраиваем её

        # проверяем, есть и в куче место
        if None not in self.HeapArray:
            return False

        index_of_free_slot = self.HeapArray.index(None)
        self.HeapArray[index_of_free_slot] = key

        while index_of_free_slot > 0:
            parent_index = (index_of_free_slot - 1) // 2
            if self.HeapArray[index_of_free_slot] > self.HeapArray[parent_index]:
                self.HeapArray[index_of_free_slot], self.HeapArray[parent_index] = self.HeapArray[parent_index], self.HeapArray[index_of_free_slot]
                index_of_free_slot = parent_index
                continue
            break

        return True
