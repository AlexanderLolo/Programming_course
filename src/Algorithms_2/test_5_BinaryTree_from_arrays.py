import unittest
from problemset_5_BinaryTreeArray_from_arrays import GenerateBBSTArray


class BinaryTree_test(unittest.TestCase):

    def test_array(self):

        input_array = [i for i in range(14,-1,-1)]
        self.assertEqual(GenerateBBSTArray(input_array), [7,3,11,1,5,9,13,0,2,4,6,8,10,12,14])
        self.assertEqual([1], [1])
        self.assertEqual([], [])


if __name__ == "__main__":
    unittest.main()
