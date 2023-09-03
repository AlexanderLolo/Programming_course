import unittest
from problemset_2_linkedlists2 import LinkedList2, Node


class LinkedList_test(unittest.TestCase):

    def test_regression_del_1(self):
        s_list = LinkedList2()
        a = Node(11)
        b = Node(12)
        c = Node(128)
        s_list.add_in_tail(a)
        s_list.add_in_tail(b)
        s_list.add_in_tail(c)

        s_list.delete(11)
        self.assertIs(s_list.head, b)
        self.assertIs(s_list.tail, c)
        self.assertIs(s_list.head.next, c)
        self.assertIs(s_list.head.prev, None)

        s_list.delete(128)
        self.assertIs(s_list.head, b)
        self.assertIs(s_list.tail, b)

        s_list.delete(12)
        self.assertIs(s_list.head, None)
        self.assertIs(s_list.tail, None)

        s_list.delete(12)
        self.assertIs(s_list.head, None)
        self.assertIs(s_list.tail, None)

    def test_regression_del_many_1(self):
        s_list = LinkedList2()
        a = Node(11)
        b = Node(11)
        c = Node(128)
        s_list.add_in_tail(a)
        s_list.add_in_tail(b)
        s_list.add_in_tail(c)
        s_list.delete(11, True)

        self.assertIs(s_list.head, c)
        self.assertIs(s_list.tail, c)
        self.assertIs(s_list.head.next, None)
        self.assertIs(s_list.head.prev, None)

        s_list = LinkedList2()
        a = Node(11)
        b = Node(11)
        s_list.add_in_tail(a)
        s_list.add_in_tail(b)
        s_list.delete(11, True)

        self.assertIs(s_list.head, None)
        self.assertIs(s_list.tail, None)

        a = Node(128)
        b = Node(11)
        c = Node(11)
        s_list.add_in_tail(a)
        s_list.add_in_tail(b)
        s_list.add_in_tail(c)
        s_list.delete(11, True)

        self.assertIs(s_list.head, a)
        self.assertIs(s_list.tail, a)
        self.assertIs(s_list.head.next, None)
        self.assertIs(s_list.head.prev, None)

    def test_regression_insert(self):
        s_list = LinkedList2()
        a = Node(11)
        b = Node(12)
        c = Node(128)
        s_list.insert(None, a)
        self.assertIs(s_list.head, a)
        self.assertIs(s_list.tail, a)
        self.assertIs(s_list.head.next, None)
        self.assertIs(s_list.head.prev, None)

        s_list.insert(None, b)
        self.assertIs(s_list.head, a)
        self.assertIs(s_list.tail, b)
        self.assertIs(s_list.tail.next, None)
        self.assertIs(s_list.head.prev, None)

        s_list.insert(a, c)
        self.assertIs(s_list.head, a)
        self.assertIs(s_list.tail, b)
        self.assertIs(s_list.head.next, c)
        self.assertIs(s_list.tail.prev, c)


    def test_add_in_head(self):
        s_list = LinkedList2()
        a = Node(11)
        b = Node(11)
        s_list.add_in_head(a)
        self.assertIs(s_list.head, a)
        self.assertIs(s_list.tail, a)
        self.assertIs(s_list.head.next, None)
        self.assertIs(s_list.head.prev, None)

        s_list.add_in_head(b)
        self.assertIs(s_list.head, b)
        self.assertIs(s_list.tail, a)
        self.assertIs(s_list.head.next, a)
        self.assertIs(s_list.tail.prev, b)


    def test_regression_del_clean(self):

        s_list = LinkedList2()
        a = Node(11)
        b = Node(11)
        c = Node(128)
        s_list.add_in_tail(a)
        s_list.add_in_tail(b)
        s_list.add_in_tail(c)
        s_list.clean()

        self.assertIs(s_list.head, None)
        self.assertIs(s_list.tail, None)

    def test_regression_find_all(self):

        s_list = LinkedList2()
        s_list.add_in_tail(Node(11))
        s_list.add_in_tail(Node(11))
        s_list.add_in_tail(Node(128))
        d = s_list.find_all(11)
        self.assertEqual([d[0].value, d[1].value], [11, 11])

        s_list = LinkedList2()
        s_list.add_in_tail(Node(11))
        s_list.add_in_tail(Node(11))
        s_list.add_in_tail(Node(128))
        d = s_list.find_all(10)
        self.assertEqual(d, [])

        s_list = LinkedList2()
        d = s_list.find_all(10)
        self.assertEqual(d, [])

    def test_regression_len(self):

        s_list = LinkedList2()
        s_list.add_in_tail(Node(11))
        s_list.add_in_tail(Node(11))
        s_list.add_in_tail(Node(128))
        self.assertEqual(s_list.len(), 3)
        s_list.delete(11, True)
        self.assertEqual(s_list.len(), 1)
        s_list.delete(128, True)
        self.assertEqual(s_list.len(), 0)


if __name__ == "__main__":
    unittest.main()
