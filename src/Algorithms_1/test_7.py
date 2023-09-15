import unittest
from problemset_7_OrderedList import OrderedList, OrderedStringList, Node


class OrderedList_test(unittest.TestCase):

    def test_regression_add(self):
        #  ascending order
        s_list = OrderedList(True)
        s_list.add(1)
        self.assertIs(s_list.head.value, 1)
        self.assertIs(s_list.tail.value, 1)

        s_list.add(2)
        self.assertIs(s_list.head.value, 1)
        self.assertIs(s_list.tail.value, 2)

        s_list.add(3)
        self.assertIs(s_list.head.value, 1)
        self.assertIs(s_list.head.next.value, 2)
        self.assertIs(s_list.head.next.next.value, 3)
        self.assertIs(s_list.tail.value, 3)

        s_list.add(0)
        self.assertIs(s_list.head.value, 0)
        self.assertIs(s_list.head.next.value, 1)

        self.assertIs(s_list.find(1).value, 1)
        self.assertIs(s_list.find(2).value, 2)
        self.assertIs(s_list.find(-1), None)

        s_list.delete(0)
        self.assertIs(s_list.head.value, 1)
        self.assertIs(s_list.head.next.value, 2)
        self.assertIs(s_list.head.next.next.value, 3)
        self.assertIs(s_list.tail.value, 3)

        s_list.delete(2)
        self.assertIs(s_list.head.value, 1)
        self.assertIs(s_list.tail.value, 3)

        s_list.delete(3)
        self.assertIs(s_list.head.value, 1)
        self.assertIs(s_list.tail.value, 1)
        self.assertIs(s_list.head.prev, None)
        self.assertIs(s_list.tail.next, None)

        #  descending order
        s_list = OrderedList(False)
        s_list.add(1)
        self.assertIs(s_list.head.value, 1)
        self.assertIs(s_list.tail.value, 1)

        s_list.add(2)
        self.assertIs(s_list.head.value, 2)
        self.assertIs(s_list.tail.value, 1)

        s_list.add(3)
        self.assertIs(s_list.head.value, 3)
        self.assertIs(s_list.head.next.value, 2)
        self.assertIs(s_list.head.next.next.value, 1)
        self.assertIs(s_list.tail.value, 1)

        s_list.add(0)
        self.assertIs(s_list.tail.value, 0)
        self.assertIs(s_list.tail.prev.value, 1)

        self.assertIs(s_list.find(1).value, 1)
        self.assertIs(s_list.find(2).value, 2)
        self.assertIs(s_list.find(-1), None)

        s_list.delete(0)
        self.assertIs(s_list.head.value, 3)
        self.assertIs(s_list.head.next.value, 2)
        self.assertIs(s_list.head.next.next.value, 1)
        self.assertIs(s_list.tail.value, 1)

        s_list.delete(2)
        self.assertIs(s_list.head.value, 3)
        self.assertIs(s_list.tail.value, 1)

        s_list.delete(3)
        self.assertIs(s_list.head.value, 1)
        self.assertIs(s_list.tail.value, 1)


if __name__ == "__main__":
    unittest.main()
