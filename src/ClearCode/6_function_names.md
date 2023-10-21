# Function names
## 1. функция возвращает первую цифру факториала числа N
    def squirrel(N: int): #### def left_factorial_digit #### def calc_left_fact_digit
    трудно уложиться в 20 символов и не хотелось сокращать factorial до fact

## 2. функция возвращает полное пройденное растояние
    def odometer(oksana: list) #### def calc_total_dist_km

## 3. функция возвращает количество дней, требуемое для завоевания поля
    def ConquestCampaign(N: int, M: int, L: int, battalion: list) #### def calc_days_to_conquer

## 4.  функция возвращает массив зарплат, соответствующий массиву номеров сотрудников.
    def SynchronizingTables(N: int, ids: list, salary: list) #### def align_salaries_by_ids
    не совсем ясно из названия функция меняет ли входящий список или создает новый.

    dict_salary - salary_to_id_map
    xchange -is_swapped

## 5.  функция возвращает целое число из списка, которое равно сумме всех остальных чисел.
    def SumOfThe(N: int, data: list) #### def find_num_equal_sum_others
    довольно трудно уложиться в 20 символов и оставить имя наглядным.
    Интересно, можно ли не разделять слова "_"? 
    Другие короткие имена отражающие суть в моменте, такие как find_balance_point, могут быть сложны для понимания через некоторое время

## 6. получает исходную строку s и либо зашифровывает её (encode = true), либо расшифровывает (encode = false), только конечно без исходных пробелов.
    def TheRabbitsFoot(str1: str, encode: bool) #### def encode_dec_msg_wo_spaces
    Общая идея, что надо делать функции выполняющие одно действие ясна, но всегда будут сложне функции. Учитывать ли в названии сложных все ньюансы или учитывать их в названиях простых?

## 7. функция рассчитывает расход тонера для печати строки
    def PrintingCosts(str1: str) -> int: #### def calc_printing_costs
    def MaximumDiscount(N: int, price: list) #### def calc_max_discount

## 8. функция возвращает абсолютное значение разности -- первое число s1 минус второе число s2, в формате строки.
    def BigMinus(str1: str, str2: str) -> str: #### def calc_abs_numbers_diff
    def MinusDigit(str1: str, digit: str) -> str: #### def calc_numbers_diff

## 9. функция возвращает массив длины N, содержащий исходные числа, преобразованные в десятичную систему счисления.
    def UFO(N: int, data: list, octal: bool) -> list: #### convert_to_decimals

## 10.  функция возвращает реальное время, требуемое для преодоления дороги.
    def Unmanned(L: int, N: int, track: list) #### def calc_trip_time_hrs

## 11. функция возвращает возвращает true, если вторая карта(массив) содержится в первой(массив)
    def TankRush(H1: int, W1: int, field1: str, H2: int, W2: int, field2: str)
    #### def is_map_contained_in(..., main_map: str, ..., sub_map: str)

## 12.  функция возвращает true, если паттерны между звездочками одинаковы.
    def LineAnalysis(line: str) -> bool: #### def is_same_btw_stars
