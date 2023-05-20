# Рефлексия
# 1. Если нет новых методов, то необходимо вызыват def __init__, чтобы происходило наследование.
# class Elf(Warrior):
#     def __init__(self, nam):
        # super().__init__(nam)
# А вот если бы был метод, тогда можно было бы так реализовать это
# class Elf(Warrior): # эльф
    # def Do_smth(self, work):
        # self.start_work(new_work)        

# 2. Возникают вопросы по реализации ad hoc полиморфизма. Питон не позволил создать две функции с одинаковыми именами. Последняя из них переопределяла первую. Поэтому пришлось вставлять конструкцию if,
# чтобы обечпечить ad hoc полиморфизм. Интересно, как это можно сделать автоматически без if

# 3. Убрал Задание имени и расы в подкласы. Аналогично эталонному решению.

# Задание 4.1 работа с объектами в строках 310-329
# Задание 4.2. работа с объектами в строках 331-342
# Задание 4.3. 345-364

import random

class Equipment:

    def __init__(self, s, p):
        self._size = s
        self._tech_condition = 100 # уменьшается со временем, может быть замедлена соответствующим навыком technician_skill
        self._price = p
        self._aging_speed = 10

    def Resize(self, coefficient): # изменение размера
        self._size *= coefficient

    def Aging(self, ranger): 
        self._tech_condition -= self._aging_speed / ranger.get_tech_skill() # вставлен метод по возвращениею скилла

    def get_tech_condition(self):
        return self._tech_condition
    
    def foo(self):
        self._price /= 2
        print("тип equipment", self._price)

class Droid(Equipment):

    def __init__(self, r, s, p):
        super().__init__(s, p)
        self.__recovery_nominal = r 
        
    def Upgrade(self, coeff):
        self.__recovery_nominal *= coeff

    def get_recovery(self):
        return self.__recovery_nominal
    
    def foo(self):
        self._price *= 2
        print("тип дройд", self._price)
        
# Dr = Droid(15, 100, 10000)

class Engine(Equipment):

    def __init__(self, spd, lp, s , p):
        super().__init__(s, p)
        self.__speed = spd
        self.__leep = lp
        self.__forsazh = False

    def ForsazhOn(self):
        self.__forsaz = True
        self.__speed *= 2
        self._aging_speed *= 2

    def ForsazhOff(self):
        self.__forsazh = False
        self.__speed /= 2
        self._aging_speed /= 2
        
    def Upgrade(self, spd, lp):
        self.__speed += spd
        self.__leep += lp

    def foo(self):
        self._price *= 4
        print("тип двигатель", self._price)


class Gun(Equipment):
    def __init__(self, dmg, dst, s, p):
        super().__init__(s, p)
        self.__damage = dmg
        self.__distance = dst
    
    def Upgrade(self, dmg_coeff, dst_coeff):
        self.__damage *= dmg_coeff
        self.__distance *= dst_coeff

    def get_damage(self):
        return self.__damage


# Класс космический корабль
class Spaceship:

    def __init__(self, arm, lc, pr):
        self._armor = arm # 0 защита в единицах
        self._load_capacity = lc # 800 # грузоподъемность
        self._structure = 100 # повреждения корпуса от 100 до 0. Могут быть восстановлены дройдом. Повреждения зависят от мощности оружия, damage_accuracy рейнджера и armor корпуса
        self._weapon_slot_count = 1
        self._droid_slot_flag = False
        self._droid_slot = None
        self._price = pr # 10000
        self._engine_slot = None     

    def Upgrade(self, capacity, arm): ## два метода с одинаковыми названиями
        self._load_capacity += capacity
        self._armor += arm

    def FullRecover(self):
        self._structure = 100
        
    def Repair(self):
        self._structure += self._droid_slot.get_recovery() # чиним тем дройдом, который установлен в слот !!!!!!!!!!!!!!!!!!

    def GetDamage(self, damage):
        self._structure -= (damage - self._armor)

    def ActiWepSlot(self):
        self._weapon_slots_count += 1
        
    def ActiDroidSlot(self): # Активирование слота для дройда
            self._droid_slot_flag = True
    
    def Set(self, equip):

        if isinstance(equip, Droid):
            self._droid_slot = equip # Создается ссылка на объект дройд
            return
        elif isinstance(equip, Engine):
            self._engine_slot = equip
            return
        
        print("некорректные параметры")
        return

# Например, нам надо постоянно выводить различную информацию о корабле на экран.  Неужели для этого необходимо создавать геттеры для каждого параметра? А если их очень много и они вложенные?
    def get_price(self):
        return self._price
    
    def get_structure(self):
        return self._structure
    
    def get_droid_slot_flag(self):
        return self._droid_slot_flag
    
    def get_armor(self):
        return self._armor

    def get_load_capacity(self):
        return self._load_capacity


class MoolokSP(Spaceship): #  для моолоков
    def __init__(self, arm, lc, pr):
        super().__init__(arm, lc, pr)
        self.__chipflag = False
        self.__race = "Moolok"

    def ChipOn(self):  # полиморфизм подтипов
        self.__chipflag = True
        self._armor += 5
        self._load_capacity -= 400

    def ChipOff(self):
        self.__chipflag = False
        self._armor -= 5
        self._load_capacity += 400

    def get_chipflag(self): 
        return self.__chipflag 
        
# mo = MoolokSP(2, 0, 800, 10000)
     
class HumanSP(Spaceship): #  для моолоков
    def __init__(self, arm, lc, pr):
        super().__init__(arm, lc, pr)
        self.__chipflag = False
        self.__race = "Human"

    def ChipOn(self):
        self.__chipflag = True
        self._armor -= 5
        self._load_capacity += 400

    def ChipOff(self):
        self.__chipflag = False
        self._armor += 5
        self._load_capacity -= 400

    def get_chipflag(self): 
        return self.__chipflag 

# hu = HumanSP(1, 0, 800, 10000)


# Класс рейнджер 
class Ranger:

    def __init__(self, spaceship):
        self._wealth = 100000 # наличные в кредитах
        self._damage_accuracy = 0.50 # наносимая мощность в % от мощности корабля
        self._technician_skill = 1.0 # уменьшение износа оборудования
        self._spaceship = spaceship # тот корабль, на котором сейчас летаем. Их может быть несколько

    def DamageUpgrade(self, coeff):
        self._damage_accuracy *= coeff

    def TechUpgrade(self, coeff): 
        self._technician_skill *= coeff

    def Payment(self, money):
        self._wealth -= money

    def SpaceshipRecovery(self):
        self.Payment(self._spaceship.get_price() * (100 - self._spaceship.get_structure() ) // 10)
        self._spaceship.FullRecover()

    def ChipOn(self):
        self._spaceship.ChipOn()

    def ChipOff(self):
        self._spaceship.ChipOff()

    def get_tech_skill(self):
        return self._technician_skill
    
    def get_wealth(self):
        return self._wealth
    
    def get_damage_accuracy(self):
        return self._damage_accuracy
 
class Human(Ranger):

    def __init__(self, name, spaceship):
        super().__init__(spaceship)
        self.__illflag = False
        self.__name = name
        self.__race = "Человек"

    # def Mask(self, name, race):
    #     self.__name = name
    #     self.__race = race

    def Illness(self, coeff): 
        if self.__illflag:
            return
        self.__illcoeff = coeff
        self._damage_accuracy *= coeff
        self._technician_skill *= coeff
        self.__illflag = True

    def GetWell(self): 
        if not self.__illflag:
            return 
        self._damage_accuracy /= self.__illcoeff
        self._technician_skill /= self.__illcoeff
        self.__illflag = False

    def get_illflag(self): 
        return self.__illflag


class Moolok(Ranger):

    def __init__(self, name, spaceship):
        super().__init__(spaceship)
        self.__bersflag = False
        self.__name = name
        self.__race = "Моолок"

    def BerserkOn(self): 
        if self.__bersflag:
            return
        self._damage_accuracy *= 2
        self._technician_skill /= 2
        self.__bersflag = True

    def BerserkOff(self): 
        if not self.__bersflag:
            return
        self._damage_accuracy /= 2
        self._technician_skill *= 2
        self.__bersflag = False

    def get_bersflag(self): 
        return self.__bersflag

# Создаем объекты    
new_droid = Droid(15, 100, 10000)
new_engine = Engine(1000, 40, 40, 10000)

new_spaceship = MoolokSP(0, 800, 10000)
new_spaceship1 = HumanSP(0, 800, 10000)

new_player = Human("Alex", new_spaceship) # Посадили человека на корабль моолока
new_player1 = Moolok("Bob", new_spaceship1) # Посадили моолока на корабль человека
new_player._spaceship.ActiDroidSlot()

# ad hoc полиморфизм. Метод Set для разного типа оборудования
new_player._spaceship.Set(new_droid)
new_player._spaceship.Set(new_engine)

# Еще один пример полиморфизма. Параметров у функций нет, но они неявно применяются к разным типам(моолокскому и человеческому кораблям)
# Активируем и диактивируем чип на моолокском корабле. 
new_player.ChipOn()
print(new_spaceship.get_armor(), 
      new_spaceship.get_chipflag())
new_spaceship.ChipOff()
print(new_spaceship.get_armor(), 
      new_spaceship.get_chipflag())

# Активируем чип на человеческом корабле и обратно
new_player1.ChipOn()
print(new_spaceship1.get_load_capacity(),
      new_spaceship1.get_chipflag())
new_spaceship1.ChipOff()
print(new_spaceship1.get_load_capacity(),
      new_spaceship1.get_chipflag())

# Задание 4.2. Результат достигается из-за полиморфизма подтипов

lobj = []

for i in range(500):
    if random.randint(0, 1) == 1:
        lobj.append(Engine(1000, 40, 40, 10000))
    else:
        lobj.append(Droid(15, 100, 10000))

for ani in lobj:
    ani.foo()


# Задание 4.3. Питон не позволил создать две функции с одинаковыми именами. Последняя из них переопределяла первую. Поэтому пришлось вставлять конструкцию if,
# чтобы обечпечить ad hoc полиморфизм. Интересно, как это можно сделать автоматически без if
def summ(a, b):
    if isinstance(a, int) and isinstance(b, int):
         return a + b
    elif isinstance(a, str) and isinstance(b, str):
        s1list = list(a)
    
        for i in range(len(b)):
            s1list.append(b[i])

        return "".join(s1list)
    
    print("некорректные параметры")
    return None


print(summ(4, 5) )
print(summ("4", "5"))
print(summ(4, "5"))


