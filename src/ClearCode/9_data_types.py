# 1
def Power(N: int, M: int) -> int:
    if M == 0:
        return 1
    if N == 0:
        return 0
    if M > 0:
        return N * Power(N, M - 1)
    return 1 / N * Power(N, M + 1)

##### вводим повышенную точность для случая,если показатель степени отрицательный
from decimal import Decimal

def Power(N: int, M: int) -> int:
    if M == 0:
        return 1
    if N == 0:
        return 0
    if M > 0:
        return N * Power(N, M - 1)
    
    return Decimal(1) / Decimal(N) * Power(N, M + 1)

# 2,3
def GetWell(self): 
    if not self.__illflag:
        return
    
    # для предупреждения ошибки деления на ноль вставил в метод следующий код
    if self.__illcoeff == 0:
        raise ValueError("Coefficient cannot be zero.")
    
    self._damage_accuracy //= self.__illcoeff # использовал целочисленное деление вместо обыкновенного
    self._technician_skill //= self.__illcoeff
    self.__illflag = False

# 4 для предупреждения ошибки деления на ноль вставил в метод следующий код
    def ForsazhOff(self, coeff):
        if coeff == 0:
            raise ValueError("Coefficient cannot be zero.")

        self.__forsazh = False
        self.__speed /= coeff
        self._aging_speed /= coeff

# 5 использовал целочисленное деление вместо обыкновенного
def SpaceshipRecovery(self):
    self.Payment(self._spaceship.get_price() * (100 - self._spaceship.get_structure() ) // 10)
    self._spaceship.FullRecover()


# 6,7,8,9
def MassVote(N: int, votes: list) -> str:

    vmax = max(votes)

    if votes.count(vmax) > 1:
        return "no winner"

    if round(vmax / sum(votes), 3) <= 0.5:
        return "minority winner {}".format(votes.index(vmax)+1)

    return "majority winner {}".format(votes.index(vmax)+1)

# 6 исключаю деление на ноль или ситуацию с пустым списком
    total_votes = sum(votes)
    if len(votes) == 0 or sum(votes) == 0:
        return "Division by zero or empty list"
    
# 7 активнее использую логические переменные
    empty_list = len(votes) == 0
    is_no_votes = sum(votes) == 0
    if len(votes) == 0 or sum(votes) == 0:
        return "Division by zero or empty list"

# 8 использовал целые числа вместо вещественных
def MassVote(N: int, votes: list) -> str:

    SCALER = 10 ** 9
    vmax = max(votes)
    if votes.count(vmax) > 1:
        return "no winner"

    if int((vmax / sum(votes)) * SCALER) <= int(0.5 * SCALER):
        return "minority winner {}".format(votes.index(vmax)+1)

    return "majority winner {}".format(votes.index(vmax)+1) 

# 9 обошелся без преобразования типов. Сравнил без преобразовнаия во float
def MassVote(N: int, votes: list) -> str:

    if vmax * 2 <= sum(votes):
        return "minority winner {}".format(votes.index(vmax)+1)

# 10
from decimal import Decimal

def TheRabbitsFoot(str1: str, encode: bool) -> str:

    string1 = str1.rstrip().replace(" ", "")

    if len(string1) == 0:
        return ""

    leng = len(string1)
    leng_sqrt = int(leng ** (1/2))

    if leng_sqrt == leng / 2: ##### избавляюсь от сравнения на равенство вещественных чисел leng_sqrt ** 2 == leng
        n_rows = leng_sqrt
        n_colomns = leng_sqrt

    elif leng_sqrt * (leng_sqrt + 1) >= leng:
        n_rows = leng_sqrt
        n_colomns = leng_sqrt + 1
    else:
        n_rows = leng_sqrt + 1
        n_colomns = leng_sqrt + 1

# 11 избавляюсь от сравнения чисел разных типов (придуманный пример)
from decimal import Decimal

leng = Decimal(2)
leng_sqrt = leng ** 2

if leng_sqrt * 2 >= leng:

# 12 использую строковые константы, а не магические строки
def PrintingCosts(str1: str) -> int:

    TONER_CONSUMP_TEMPL = """(пробел) 0   !   9        "   6        #  24        $  29        %  22 """ 

    dict1 = {}
    row_list = TONER_CONSUMP_TEMPL.split()
    for i in range(0, len(row_list), 2):
        dict1[row_list[i]] = int(row_list[i+1])
    dict1[" "] = dict1.pop("(пробел)", 11)
