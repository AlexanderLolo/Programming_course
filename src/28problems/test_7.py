import unittest
from problemset_7 import StringSplit, WordSearch

class Problem6_test(unittest.TestCase):
# слова длинной более заданного значения мы всегда начинаем с новой строчки
    def test_regression(self):
        self.assertEqual(StringSplit(2,"1234567"), ["12","34","56","7"])
        self.assertEqual(StringSplit(2,"123456"), ["12","34","56"])
        self.assertEqual(StringSplit(2,"1 123456"), ["1","12","34","56"])
        self.assertEqual(StringSplit(2,"11 123456"), ["11","12","34","56"])
        self.assertEqual(StringSplit(2,"11 123 45 6"), ["11","12","3","45","6"])
        self.assertEqual(StringSplit(3,"11 1234 4 6"), ["11","123","4 4","6"])
        self.assertEqual(StringSplit(3,"1234 1 4"), ["123","4 1","4"])
        self.assertEqual(StringSplit(3,"1234 1234"), ["123","4","123", "4"])
        self.assertEqual(StringSplit(2,""), [])
        self.assertEqual(StringSplit(12,"1) строка разбивается на набор строк через выравнивание по заданной ширине."), ["1) строка", "разбивается","на набор","строк через","выравнивание","по заданной","ширине."])

        self.assertEqual(WordSearch(12, "1) строка разбивается на набор строк через выравнивание по заданной ширине.", "строк"), [0,0,0,1,0,0,0])
        self.assertEqual(WordSearch(12, "", "строк"), [])
        self.assertEqual(WordSearch(0, "", ""), [])
        self.assertEqual(WordSearch(2, "aaa", "aa"), [1,0])

if __name__ == "__main__":
    unittest.main()
    