# 1
#### класс Droid и класс Engine имеют метод foo, который они переопределяют, являясь наследниками от Engine. 
#### При вызове этих методов для объектов разных классов(Droid, Engine) выбор метода будет определен, как я понимаю, на этапе выполнения программы,
#### что называется поздним связыванием. В данном случае это выбор не мой, а способ реализации концепции полиморфизма.

class Droid(Equipment):

    def foo(self):
        self._price *= 2
        print("тип дройд", self._price)
    # pass...

class Engine(Equipment):

    def foo(self):
        self._price *= 4
        print("тип двигатель", self._price)
    # pass...

class Equipment:
    
    def foo(self):
        self._price /= 2
        print("тип equipment", self._price)
    # pass...

class Spaceship:

#### если правильно понимаю, то атрибуты экземпляра класса, несмотря на то что их значения фиксированы (self._structure = 100) 
#### все равно связываются со сзначениями только в момент создания экземпляра класса, что не является ранним связыванием.
    def __init__(self, arm, lc, pr):
        self._armor = arm
        self._load_capacity = lc
        self._structure = 100
        self._weapon_slot_count = 1
        self._droid_slot_flag = False
        self._droid_slot = None
        self._price = pr
        self._engine_slot = None     

#### в примере ниже, если не ошибаюсь, тоже происходит позднее связывание, когда после вызова метода, присваиваемое атрибуту класса
#### значение зависит от типа объекта, передаваемого в метод.
    def Set(self, equip):

        if isinstance(equip, Droid):
            self._droid_slot = equip
            return None
        if isinstance(equip, Engine):
            self._engine_slot = equip
            return None

# 2
def main():

# в обоих строчках ниже используется максимально раннее связывание со строковой константой. 
# конечно, если бы эти переменные фигурировали в коде больше, чем по одному разу, то стоило бы ввести константы и тогда связывание стало бы
# происходить на этапе компиляции.

    name = "new_arch.zip"
    name1 = "new_arch1.zip"

    arch_func(name, ".txt")
    arch_func1(name1, ".txt")


if __name__ == "__main__":
    main()

# 3
#### ниже связывание происходит в моменте выполнения программы, так как ввод от пользователся равнозначен считыванию информации из файла.
#### выбор продиктован логикой программы
x = float(input('введите первое число'))
y = float(input('введите второе число'))
z = float(input('введите третье число'))

x = x * 2
y = y - 3
z = z * z
sum = x + y + z

print("x=", x, "y=", y, "z=", z, "sum=", sum)
