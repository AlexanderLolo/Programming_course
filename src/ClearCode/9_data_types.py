
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


# 4 использовал целочисленное деление вместо обыкновенного
def SpaceshipRecovery(self):
    self.Payment(self._spaceship.get_price() * (100 - self._spaceship.get_structure() ) // 10)
    self._spaceship.FullRecover()


# 5,6,7,8
def MassVote(N: int, votes: list) -> str:

    vmax = max(votes)

    if votes.count(vmax) > 1:
        return "no winner"

    if round(vmax / sum(votes), 3) <= 0.5:
        return "minority winner {}".format(votes.index(vmax)+1)

    return "majority winner {}".format(votes.index(vmax)+1)

# 5 исключаю деление на ноль или ситуацию с пустым списком
    total_votes = sum(votes)
    if len(votes) == 0 or sum(votes) == 0:
        return "Division by zero or empty list"
    
# 6 активнее использую логические переменные
    empty_list = len(votes) == 0
    is_no_votes = sum(votes) == 0
    if len(votes) == 0 or sum(votes) == 0:
        return "Division by zero or empty list"

# 7 использовал целые числа вместо вещественных
def MassVote(N: int, votes: list) -> str:

    SCALER = 10 ** 9
    vmax = max(votes)
    if votes.count(vmax) > 1:
        return "no winner"

    if int((vmax / sum(votes)) * SCALER) <= int(0.5 * SCALER):
        return "minority winner {}".format(votes.index(vmax)+1)

    return "majority winner {}".format(votes.index(vmax)+1) 

# 8 обошелся без преобразования типов. Сравнил без преобразовнаия во float
def MassVote(N: int, votes: list) -> str:

    if vmax * 2 <= sum(votes):
        return "minority winner {}".format(votes.index(vmax)+1)

