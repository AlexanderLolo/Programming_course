import unittest
from problemset_5_queue import Queue, Two_stack_Queue, rotate_queue, LinkedList, Node, sum_if_len_equal


class Queue_test(unittest.TestCase):

    def test_regression_operations_queue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue("2")
        self.assertEqual(queue.dequeue(), 1)
        queue.enqueue(3.14)
        self.assertEqual(queue.size(), 2)

        while queue.size() > 0:
            self.assertEqual(queue.dequeue(), "2")
            self.assertEqual(queue.dequeue(), 3.14)
        self.assertEqual(queue.size(), 0)
        self.assertEqual(queue.dequeue(), None)


class Two_stack_Queue_test(unittest.TestCase):

    def test_regression_operations_queue(self):
        queue = Two_stack_Queue()
        queue.enqueue(1)
        queue.enqueue("2")
        self.assertEqual(queue.dequeue(), 1)
        queue.enqueue(3.14)
        self.assertEqual(queue.size(), 2)

        while queue.size() > 0:
            self.assertEqual(queue.dequeue(), "2")
            self.assertEqual(queue.dequeue(), 3.14)
        self.assertEqual(queue.size(), 0)
        self.assertEqual(queue.dequeue(), None)
    
class rotate_queue_test(unittest.TestCase):

    def test_regression_operations_two_stack_queue(self):
        queue = Two_stack_Queue()
        queue.enqueue(1)
        queue.enqueue("2")
        queue.enqueue(3.14)
        rotate_queue(queue, 2)

        self.assertEqual(queue.dequeue(), 3.14)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), "2")
        self.assertEqual(queue.size(), 0)
        rotate_queue(queue, 5)
        self.assertEqual(queue.dequeue(), None)
        self.assertEqual(queue.size(), 0)

    def test_regression_operations_queue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue("2")
        queue.enqueue(3.14)
        rotate_queue(queue, 2)

        self.assertEqual(queue.dequeue(), 3.14)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), "2")
        self.assertEqual(queue.size(), 0)
        rotate_queue(queue, 5)
        self.assertEqual(queue.dequeue(), None)
        self.assertEqual(queue.size(), 0)

class LinkedList_test(unittest.TestCase):

    def test_regression_sum_if_len_equal(self):
        list1 = LinkedList()
        list2 = LinkedList()
        list4 = LinkedList()

        list1.add_in_tail(Node(11))
        list1.add_in_tail(Node(12))
        list1.add_in_tail(Node(13))

        list2.add_in_tail(Node(1))
        list2.add_in_tail(Node(2))
        list2.add_in_tail(Node(3))

        list3 = sum_if_len_equal(list1, list2)
        self.assertEqual(list3.head.value, 12)
        self.assertEqual(list3.head.next.value, 14)
        self.assertEqual(list3.head.next.next.value, 16)

        list4.add_in_tail(Node(2))
        list3 = sum_if_len_equal(list1, list4)
        self.assertEqual(list3, None)


if __name__ == "__main__":
    unittest.main()
