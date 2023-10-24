# 3.1.1
class Spaceship:

    def __init__(self, load_capacity, price):
        self._load_capacity = load_capacity
        self._price = price

class MoolokSpaceship(Spaceship):

    def __init__(self, load_capacity, price, armor=10):
        super().__init__(load_capacity, price)
        self._race = "Moolok"
        self._armor = armor


class HumanSpaceship(Spaceship):

    def __init__(self, load_capacity, price, armor=5):
        super().__init__(load_capacity, price)
        self._race = "Human"
        self._armor = armor

class SpaceshipFactory:
    
    def create_spaceship(self, race, load_capacity, price):
        if race == "Human":
            return HumanSpaceship(load_capacity, price)
        elif race == "Moolok":
            return MoolokSpaceship(load_capacity, price)
        else:
            raise ValueError("not correct race")
        
spaceship_factory = SpaceshipFactory()
human_spaceship = spaceship_factory.create_spaceship("Human", 100, 10000)


# 3.2.2

class Ranger:

    def __init__(self, name):
        self._name = name


class Human(Ranger):

    def __init__(self, name, spaceship=spaceship_factory.create_spaceship("Human", 100, 10000)):
        super().__init__(name)
        self._race = "Human"
        self._spaceship = spaceship

class Moolok(Ranger):

    def __init__(self, name, spaceship=spaceship_factory.create_spaceship("Moolok", 90, 10000)):
        super().__init__(name)
        self._race = "Moolok"
        self._spaceship = spaceship

class RangerFactory:
    
    def create_ranger(self, name, race):
        if race == "Human":
            return Human(name)
        elif race == "Moolok":
            return Moolok(name)
        else:
            raise ValueError("not correct race")
        
ranger_factory = RangerFactory()
human_ranger = ranger_factory.create_ranger("Alexander", "Human")

# 3.3.3

class Equipment:

    def __init__(self, s, p):
        self._size = s
        self._tech_condition = 100 # уменьшается со временем, может быть замедлена соответствующим навыком technician_skill
        self._price = p
        self._aging_speed = 10


class Droid(Equipment):

    def __init__(self, r, s, p):
        super().__init__(s, p)
        self.__recovery_nominal = r #  восстанавливаемые единицы корпуса за ход (15) уникальный для дройда
        

class Engine(Equipment):

    def __init__(self, spd, lp, s , p):
        super().__init__(s, p)
        self.__speed = spd
        self.__leep = lp
        self.__forsazh = False


class Gun(Equipment):
    def __init__(self, dmg, dst, s, p):
        super().__init__(s, p)
        self.__damage = dmg
        self.__distance = dst
    

class EquipmentFactory:

    def create_equipment(self, equipment_type, *args):
        if equipment_type == "droid":
            return Droid(*args)
        elif equipment_type == "engine":
            return Engine(*args)
        elif equipment_type == "gun":
            return Gun(*args)
        else:
            raise ValueError("not correct equipment type")
        
equipment_factory = EquipmentFactory()

new_droid = equipment_factory.create_equipment("droid", 15, 100, 10000)
new_engine = equipment_factory.create_equipment("engine", 150, 20, 200, 50000)
new_gun = equipment_factory.create_equipment("gun", 50, 300, 50, 8000)
