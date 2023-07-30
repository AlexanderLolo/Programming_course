import unittest
from problemset_28 import Keymaker


def N_devider(N):
    count = 0
    for i in range(1, N // 2 + 1):
        if N % i == 0:
            count += 1
    return count + 1


def Provefunction(N):
    return "".join(map(str, [N_devider(i) % 2 for i in range(1, N + 1)]))


class Problem28_test(unittest.TestCase):

    def test_regression(self):

        for i in range(1, 100):
            self.assertEqual(Provefunction(i), Keymaker(i))


if __name__ == "__main__":
    unittest.main()
