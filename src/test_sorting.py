import unittest
import random
from Sorting import NotOptomizedSorting as sorting

class Sortingtests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(sorting( [9, 8, 7, 6, 9] ), [6, 7, 8, 9, 9] )
        self.assertEqual(sorting( [9, 9, 2, 2, 2] ), [2, 2, 2, 9, 9] )
        self.assertEqual(sorting( [-1, -9] ), [-9, -1] )
        self.assertEqual(sorting( [9] ), [9] )
        self.assertEqual(sorting( [] ), [] )

    def test_random(self):
        list1 = []
        for i in range(100):
            list1.append(random.randint(-50,50))
        sorting(list1) # тестируемая функция изменяет изначальный список

        for i in range(100-1):
            self.assertLessEqual(list1[i], list1[i+1])

    def test_minmax(self):
        self.assertEqual(sorting( [1287634863458634856374865743659843988, 1287634863458634856374865743659843987] ), [1287634863458634856374865743659843987, 1287634863458634856374865743659843988] )
        self.assertEqual(sorting( [-1287634863458634856374865743659843987, -1287634863458634856374865743659843988] ), [-1287634863458634856374865743659843988, -1287634863458634856374865743659843987] )
    
    def test_sameobj(self):
        list = [9, 8, 7]
        self.assertIs(list, sorting(list)) # Проверяем, что функция действительно изменяет входные данные, а не создает другой список

    def test_excep_str(self):
        with self.assertRaises(TypeError) as e:
            sorting( ["a", "b"] )
        self.assertEqual(e.exception.args[0], "Элементами списка могут быть только целые числа")

    def test_excep_float(self):
        with self.assertRaises(TypeError) as e:        
            sorting( [4.0, 5] )
        self.assertEqual(e.exception.args[0], "Элементами списка могут быть только целые числа")

    def test_excep_obj(self):
        with self.assertRaises(TypeError) as e:        
            sorting( "5" )
        self.assertEqual(e.exception.args[0], "В функцию можно передать только список")
      
if __name__ == "__main__":
    unittest.main()
