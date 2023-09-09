import unittest
from problemset_4_stack import Stack, Stack_old, balance_parenthesis, postfix


class Stack_test(unittest.TestCase):

    def test_regression_operations_stack_old(self):
        stack = Stack_old()
        stack.push(1)
        stack.push("2")
        self.assertEqual(stack.peek(), "2")
        self.assertEqual(stack.peek(), "2")

        stack.push(3.14)
        self.assertEqual(stack.size(), 3)

        while stack.size() > 0:
            self.assertEqual(stack.pop(), 3.14)
            self.assertEqual(stack.pop(), "2")
            self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.size(), 0)
        self.assertEqual(stack.pop(), None)
        self.assertEqual(stack.peek(), None)

        # with self.assertRaises(EmptyStackException) as cm:
        #     stack.pop()
        # self.assertEqual(cm.exception.args[0], '''Stack is empty.Cant produce 'pop' ''')
    
    def test_regression_operations_stack(self):
        stack = Stack()
        stack.push(1)
        stack.push("2")
        self.assertEqual(stack.peek(), "2")
        self.assertEqual(stack.peek(), "2")

        stack.push(3.14)
        self.assertEqual(stack.size(), 3)

        while stack.size() > 0:
            self.assertEqual(stack.pop(), 3.14)
            self.assertEqual(stack.pop(), "2")
            self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.size(), 0)
        self.assertEqual(stack.pop(), None)
        self.assertEqual(stack.peek(), None)

    def test_regression_operations_balance(self):

        self.assertEqual(balance_parenthesis("(())"), True)
        self.assertEqual(balance_parenthesis("))(("), False)
        self.assertEqual(balance_parenthesis("(()"), False)

    def test_regression_operations_postfix(self):

        self.assertEqual(postfix("11 2 + 3 * ="), 39)
        self.assertEqual(postfix("8 2 + 5 * 9 + ="), 59)


if __name__ == "__main__":
    unittest.main()
