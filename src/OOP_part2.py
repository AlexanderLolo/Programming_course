# Рефлексия
# При описании классов столкнулся со следующими ограничениями и необходимостями, которые пока не ясно было как преодолевать:
# 1)	Вывести сразу и просто все атрибута класса командой принт не получилось. Пришлось выводить поатрибутно
# 2)	Захотелось задать ограничения для возможных значений атрибутов в классе. В эталонном решении, это например workId,
#       который может принимать только четыре значения.
# 
# Задавался вопросом, стоит ли сначала создать объекты всех классов, а потом с ними работать(как реализовано у меня) 
# или лучше создавать объект и сразу, если есть необходимость работать с атрибутами(как в эталонном решении).


# Задание

class Droid:

    def __init__(self):
        self.recovery_nominal = 15 # восстанавливаемые единицы корпуса за ход
        self.size = 100
        self.tech_condition = 100 # уменьшается со временем, может быть замедлена соответствующим навыком technician_skill
        self.price = 1000

    def Resize(self, coefficient): # изменение размера дройда
        self.size *= coefficient

    def Upgrade(self, coefficient):
        self.recovery_nominal *= coefficient

# В методе ниже ссылаемся на объект класса Ranger, так как буду использовать его технические навыки в расчетах. 
# Он должен быть определен, перед вызовом метода. Конечно,можно было бы в классе рейнджер создать отдельный метод.
# Какой подход правильнее?

    def Aging(self, ranger): 
        self.tech_condition -= 10 / ranger.technician_skill # как замедлить соответствующим навыком?

# Класс космический корабль
class Spaceship:

    def __init__(self, race):
        self.race = race # пиратская раса
        self.armor = 0 # защита в единицах
        self.load_capacity = 800 # грузоподъемность
        self.structure = 100 # повреждения корпуса от 100 до 0. Могут быть восстановлены дройдом. Повреждения зависят от мощности оружия, damage_accuracy рейнджера и armor корпуса
        self.weapon_slot_count = 1
        self.droid_slot_flag = False
        self.droid_slot = None
        self.price = 10000     

    def Upgarde(self, capacity, armor):
        self.load_capacity += capacity
        self.armor += armor

    def FullRecover(self):
        self.structure = 100
        
    def Repair(self):
        self.structure += self.droid_slot.recovery_nominal # чиним тем дройдом, который установлен в слот

    def GetDamage(self, damage):
        self.structure -= (damage - self.armor)

    def ActiWepSlot(self): # Интересно, стоило ли активирование слотов под разное оборудование реализовыавать одной функцией? Различные бы слоты активировались в зависимоси от параметров передаваемых в функцию
        self.weapon_slots_count += 1
        
    def ActiDroidSlot(self): # Активирование слота для дройда
            self.droid_slot_flag = True
    
    def SetDroid(self, droid): # Установка дройда в слот(может быть в трюме)
        self.droid_slot = droid # Создается ссылка на объект дройд

# Класс рейнджер 
class Ranger:

    def __init__(self, name, race, spaceship):
        self.name = name
        self.race = race
        self.wealth = 100000 # наличные в кредитах
        self.damage_accuracy = 0.50 # наносимая мощность в % от мощности корабля
        self.technician_skill = 1.0 # уменьшение износа оборудования
        self.spaceship = spaceship # тот корабль, на котором сейчас летаем. Их может быть несколько

    def Mask(self, name, race):
        self.name = name
        self.race = race

    def Illness(self, reduction):
        self.damage_accuracy *= reduction
        self.technician_skill *= reduction

    def DamageUpgrade(self, coefficient):
        self.damage_accuracy *= coefficient
        
    def TechUpgrade(self, coefficient):
        self.technician_skill *= coefficient

    def Payment(self, money):
        self.wealth -= money

    def SpaceshipRecovery(self):
        self.Payment(self.spaceship.price * (100 - self.spaceship.structure ) // 10)
        self.spaceship.FullRecover()

# Создаем объекты    
new_droid = Droid()
new_spaceship = Spaceship(1)
new_player = Ranger("Alex", 2, new_spaceship)

# Активируем слот для дройда. Программа сработает и без этого, так как не усложнял код условиями. Но считаем, что если неактивирован, то установить дройда нельзя
new_player.spaceship.ActiDroidSlot()
print(new_player.spaceship.droid_slot_flag) # True

# Устанавливаем дройда, наносим кораблю повреждения и чиним дройдом корабль

# обращаемся к методам корабля через ссылку на игрока, но могли бы и напрямую
# new_spaceship.GetDroid(new_droid). Реализовал так, так как предполагаю, что если код большой, то не надо будет искать название объекта.
# Но все же не уверенности когда и как лучше делать

# Также мы можем рассматривать восстановление корпуса дройдом, как действие, которое совершается над Spaceship и реализовать метод в классе Spaceship(как у меня и сделано)
# или мы можем рассматривать восстановление, как действие, которое совершает рейнджер, и реализовать этот метод в классе Ranger. Как же лучше?
new_player.spaceship.SetDroid(new_droid)
new_player.spaceship.GetDamage(20)
new_player.spaceship.Repair() # восстановили на 15 # вообще, хорошо бы проверить что дройд установлен, но для упрощения не делаю
print(new_player.spaceship.structure) # 95%, уменьшилось в итоге на 5

# платим деньги и восстанавливаем полностью корабль
print(new_player.wealth) # 100 000
new_player.SpaceshipRecovery()
print(new_player.wealth) # 95 000
print(new_player.spaceship.structure) # 100%

# Старим дройда
new_player.spaceship.droid_slot.Aging(new_player)
print(new_player.spaceship.droid_slot.tech_condition) # 100 -> 90

# апгрейдим навык техника и еще раз старим дройда
new_player.TechUpgrade(2)
new_player.spaceship.droid_slot.Aging(new_player)
print(new_player.spaceship.droid_slot.tech_condition) # 90 -> 85 стареет в два раза медленнее

# В блоке выше получился очень длинный список new_player.spaceship.droid_slot.Aging
# Стоит ли упрощать и делать в каждом классе методы, которые будут вызывать другие методы из вложенных классов?

