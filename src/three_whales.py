# Не смотря на то, что Git удобная система контроля версий, пользуюсь я ей из командной строки, что создает определенные неудобства, когда просматриваю именения, которые сделал.
# Так как к каждому заданию я пишу рефлексию и изменения порой  это полностью переписанный код, то пока решил выкладывать новый версии файлов. Если все задания необходимо делать в одном, то перейду на такую систему.


# Рефлексия
# 1. Атрибуты можно определять внутри методов, помимо объявления в начале в методе __init__. Или в методе __init__ запускать другие определенные методы, как это было сделано в эталонном решении
# 2. Можно было использовать условные операторы для определения нескольких сущностей относящихся к одному классу, как в эталонном решении (ответ на мой вопрос). Имеет смысл, если нет отичающихся методов и наследование не нужно
# 3. Имя передавамемого параметра в эталонном решении отличается от имени атрибута. Буду придерживаться, хотя ессли имена совпадают, то тоже все работает
# def __init__(self, knd)
    # self.kind = knd # 

# Рефлексия ниже относится к работе с функциями и атрибутами классов текущего задания. Пример приведен после определения всех классов в программе ниже.
# Вопрос, который пока остался из предыдущего занятия. В примерах ниже я намеренно обращаюсь к методам корабля через ссылку на игрока. Это неправильно, так как я сделал все атрибуты приватными.
# Правильно было бы или обращаться напрямую(new_spaceship.SetDroid() вместо new_player._spaceship.SetDroid()) или через набор геттеров.
# Но представим ситуацию, когда именно так необходимо. Например,у игрока очень много вещей и искать какие из них сейчас на игроке, а какие на складе в коде неудобно. Удобнее отталкиваться от игрока.
# Если реализовывать через геттеры, то их надо иметь не просто много, а очень много, да еще и вложенных, например, для случая, когда мы хотим узнать размер дройда, 
# который вмонтирован в корабль, которым на данный момент владеет игрок.
# Если обращаться напрямую, то можно запутаться во множестве объектов.

# Такая же ситуация, если мы вызываем метод, вложенного объекта(например, new_player._spaceship._droid_slot.Aging(new_player)).
# Вложенность здесь, означает логическую вложенность. Двигатель в машине. Или космический корабль, который принадлежит игроку.
# Как же поступить?



# Задание. Объединил 5.1 и 5.2
# из-за довольно длинного кода, чтобы не смещать акценты, в функциях я не прописывал проверки на корректность вычисляемых данных. Это,безусловно, надо сделать позже

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

class Droid(Equipment):

    def __init__(self, r, s, p):
        super().__init__(s, p)
        self.__recovery_nominal = r #  восстанавливаемые единицы корпуса за ход (15) уникальный для дройда
        
    def Upgrade(self, coeff): # или лучше назвать set_recovery?
        self.__recovery_nominal *= coeff

    def get_recovery(self):
        return self.__recovery_nominal
        
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


class Gun(Equipment):
    def __init__(self, dmg, dst, s, p):
        super().__init__(s, p)
        self.__damage = dmg
        self.__distance = dst
    
    def Upgrade(self, dmg_coeff, dst_coeff):
        self.__damage *= dmg_coeff
        self.__distance *= dst_coeff

    def get_damage(self):  # может заменить на Fire?
        return self.__damage


# Класс космический корабль
class Spaceship:

    def __init__(self, rc, arm, lc, pr):
        self._race = rc # человек 1, моолок 2
        self._armor = arm # 0 защита в единицах
        self._load_capacity = lc # 800 # грузоподъемность
        self._structure = 100 # повреждения корпуса от 100 до 0. Могут быть восстановлены дройдом. Повреждения зависят от мощности оружия, damage_accuracy рейнджера и armor корпуса
        self._weapon_slot_count = 1
        self._droid_slot_flag = False
        self._droid_slot = None
        self._price = pr # 10000     

    def Upgarde(self, capacity, arm):
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
    
    def SetDroid(self, droid): # Установка дройда в слот(может быть в трюме)
        self._droid_slot = droid # Создается ссылка на объект дройд

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
    def __init__(self, rc, arm, lc, pr):
        super().__init__(rc, arm, lc, pr)
        self.__chipflag = False

    def ArmChipOn(self):
        self.__chipflag = True
        self._armor += 5
        self._load_capacity -= 400

    def ArmChipOff(self):
        self.__chipflag = False
        self._armor -= 5
        self._load_capacity += 400

    def get_chipflag(self): 
        return self.__chipflag 
        
# mo = MoolokSP(2, 0, 800, 10000)
     
class HumanSP(Spaceship): #  для моолоков
    def __init__(self, rc, arm, lc, pr):
        super().__init__(rc, arm, lc, pr)
        self.__chipflag = False

    def LoadChipOn(self):
        self.__chipflag = True
        self._armor -= 5
        self._load_capacity += 400

    def LoadChipOff(self):
        self.__chipflag = False
        self._armor += 5
        self._load_capacity -= 400

    def get_chipflag(self): 
        return self.__chipflag 

# hu = HumanSP(1, 0, 800, 10000)


# Класс рейнджер 
class Ranger:

    def __init__(self, name, race, spaceship):
        self._name = name
        self._race = race
        self._wealth = 100000 # наличные в кредитах
        self._damage_accuracy = 0.50 # наносимая мощность в % от мощности корабля
        self._technician_skill = 1.0 # уменьшение износа оборудования
        self._spaceship = spaceship # тот корабль, на котором сейчас летаем. Их может быть несколько

    def Mask(self, name, race):
        self._name = name
        self._race = race

    def DamageUpgrade(self, coeff):
        self._damage_accuracy *= coeff

    def TechUpgrade(self, coeff): 
        self._technician_skill *= coeff

    def Payment(self, money):
        self._wealth -= money

    def SpaceshipRecovery(self):
        self.Payment(self._spaceship.get_price() * (100 - self._spaceship.get_structure() ) // 10)
        self._spaceship.FullRecover()

    def get_tech_skill(self):
        return self._technician_skill
    
    def get_wealth(self):
        return self._wealth
    
    def get_damage_accuracy(self):
        return self._damage_accuracy
 


class Human(Ranger):

    def __init__(self, name, race, spaceship):
        super().__init__(name, race, spaceship)
        self.__illflag = False

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

    def __init__(self, name, race, spaceship):
        super().__init__(name, race, spaceship)
        self.__bersflag = False

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
new_spaceship = MoolokSP(2, 0, 800, 10000)
new_spaceship1 = HumanSP(2, 0, 800, 10000)

new_player = Human("Alex", 2, new_spaceship) # Посадили человека на корабль моолока
new_player1 = Moolok("Bob", 1, new_spaceship1) # Посадили моолока на корабль человека

# Вопрос, который пока остался из предыдущего занятия. В примерах ниже я намеренно обращаюсь к методам корабля через ссылку на игрока. Это неправильно, так как я сделал все атрибуты приватными.
# Правльно было бы или обращаться напрямую(new_spaceship.SetDroid() вместо new_player._spaceship.SetDroid()) или через набор геттеров.
# Но представим ситуацию, когда именно так необходимо. Например,у игрока очень много вещей и искать какие из них сейчас на игроке, а какие на складе в коде неудобно. Удобнее отталкиваться от игрока.
# Если реализовывать через геттеры, то их надо иметь не просто много, а очень много, да еще и вложенных, например, для случая, когда мы хотим узнать размер дройда, 
# который вмонтирован в корабль, которым на данный момент владеет игрок.
# Если обращаться напрямую, то можно запутаться во множестве объектов.

# Такая же ситуация, если мы вызываем метод, вложенного объекта. Вложенность здесь, означает логическую вложенность. Двигатель в машине. Или космический корабль, который принадлежит игроку.
# Как же поступить?

# В коде ниже, я намеренно организовал доступ к приватным параметрам не через геттеры и не напрямую, чтобы акцентирвоать внимание на вопросе. 
# Конечно, если бы параметры были бы не обозначены как приватные, а полноценно приватными, то ничего не получилось бы


# Активируем слот для дройда. Программа сработает и без этого, так как не усложнял код условиями. Но считаем, что если неактивирован, то установить дройда нельзя
new_player._spaceship.ActiDroidSlot() # если создать специальный методвставить специальный метод !!!!!!!!!!!!!!!!!!!!!!!!
print(new_player._spaceship.get_droid_slot_flag()) # True

# Устанавливаем дройда, наносим кораблю повреждения и чиним дройдом корабль



# Также мы можем рассматривать восстановление корпуса дройдом, как действие, которое совершается над Spaceship и реализовать метод в классе Spaceship(как у меня и сделано)
# или мы можем рассматривать восстановление, как действие, которое совершает рейнджер, и реализовать этот метод в классе Ranger. Как же лучше?
new_player._spaceship.SetDroid(new_droid)
new_player._spaceship.GetDamage(20)
new_player._spaceship.Repair() # восстановили на 15 # вообще, хорошо бы проверить что дройд установлен, но для упрощения не делаю
print(new_player._spaceship.get_structure()) # 95%, уменьшилось в итоге на 5

# платим деньги и восстанавливаем полностью корабль
print(new_player.get_wealth()) # 100 000
new_player.SpaceshipRecovery()
print(new_player.get_wealth()) # 95 000
print(new_player._spaceship.get_structure()) # 100%

# Заболеваем и выздоравливаем, мы можем это сделать раз мы человек
new_player.Illness(0.5)
print(new_player.get_damage_accuracy(), new_player.get_illflag())
new_player.GetWell()
print(new_player.get_damage_accuracy(), new_player.get_illflag())

# Становимся берсерком и обратно раз мы моолок
new_player1.BerserkOn()
print(new_player1.get_damage_accuracy(), new_player1.get_bersflag())
new_player1.BerserkOff()
print(new_player1.get_damage_accuracy(), new_player1.get_bersflag())

# Активируем чип на моолокском корабле и обратно
new_player._spaceship.ArmChipOn()
print(new_player._spaceship.get_armor(), new_player._spaceship.get_chipflag())
new_player._spaceship.ArmChipOff()
print(new_player._spaceship.get_armor(), new_player._spaceship.get_chipflag())

# Активируем чип на человеческом корабле и обратно
new_player1._spaceship.LoadChipOn()
print(new_player1._spaceship.get_load_capacity(), new_player1._spaceship.get_chipflag())
new_player1._spaceship.LoadChipOff()
print(new_player1._spaceship.get_load_capacity(), new_player1._spaceship.get_chipflag())

# Старим дройда
new_player._spaceship._droid_slot.Aging(new_player) # если упрощать и делать в каждом классе методы, которые будут вызывать другие методы из вложенных классов, то сколько же методов будет...
print(new_player._spaceship._droid_slot.get_tech_condition()) # 100 -> 90 !

# апгрейдим навык техника и еще раз старим дройда
new_player.TechUpgrade(2)
new_player._spaceship._droid_slot.Aging(new_player)
print(new_player._spaceship._droid_slot.get_tech_condition()) # 90 -> 85 стареет в два раза медленнее


