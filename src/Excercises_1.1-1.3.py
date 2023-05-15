# Задание 1.1

# Яндекс навигатор
# 
# 1)	Классы соответствующие физическим объектам: жилым домам, заправкам, ресторанам, магазинам, аптекам, банкоматам и т.д. 
# Атрибуты(географическое расположение, название, коммерческий объект или нет, тип коммерческого объекта и т.д.
# Сецифические атрибуты: отзывы, рейтинг, часы работы.
# 
# 2)	Классы соответствующие типу пользователя(например, автомобилист, пешеход, велосипедист), 
# для каждого из которых помимо атрибутов, сответствующих собираемой яндексом персональной информации, 
# определены функции, например, функция возможного проложения маршрута(пешеход сможет пройти там, 
# где автомобилист не проедет, и возможно наоборот), 
# функции пользования дополнительными сервисами навигатора, такие как оплата, музыка и т.д
# 
# Microsoft word
# 
# 1)	Класс для документа c атрибутами: тип шрифта, величина шрифта, другие параметры, 
# связанные с форматированием, такие как отступы, фон, цвет и тд. 
# Функции по изменению, удалению, сохранению документов
# 
# 2)	Классы соответствующие объектам, которые используются в документе Microsoft Word, 
# например, диаграммы, картинки, иконки,комментарии, таблицы с соответствующими атрибутами 
# (например, для таблицы это может быть ее размер, положение на странице, оформление - толщина линий, цвет и тд.) 
# с функциями по их созданию, изменению и интеграции в документ.


# Задание 1.2

class Droid:
    generation = 2
    recovery_nominal = 20 # восстанавливаемые единицы корпуса за ход
    upgrade = 1.00 # улучшения в % от номинала
    tech_condition = 100 # уменьшается со временем, может быть замедлена соответствующим навыком technician_skill

class PirateSpaceship:
    race = 5 # пиратская раса
    armor = 10 # защита в единицах
    load_capacity = 800 # грузоподъемность
    weapon_slots = 5
    droid_slot = Droid()
    damage = 100 # повреждения корпуса от 100 до 0. Могут быть восстановлены дройдом. Повреждения зависят от мощности оружия, damage_accuracy рейнджера и armor корпуса
    
class Ranger:
    name = "Alex"
    race = 6 # раса моолоков
    wealth = 10000 # наличные в кредитах
    nod_account = 300 # количество нодов на счету
    damage_accuracy = 0.80 # наносимая мощность в % от мощности корабля
    technician_skill = 1.15 # уменьшение износа оборудования
    klissan_kills = 0 # количество уничтоженных клиссан
    spaceship = PirateSpaceship()

#создаем объекты    
new_droid = Droid()
new_spaceship = PirateSpaceship()
new_player = Ranger()

#изменяем объекты  
new_droid.upgrade = 1.1
new_droid.tech_condition = 100 - 15

new_spaceship.droid_slot = new_droid
new_spaceship.damage = 100 - 20

new_player.name = "lololo"
new_player.klissan_kills = new_player.klissan_kills + 2
new_player.spaceship = new_spaceship

#выводим объекты    
print("объект дройд:",
    "generation", new_droid.generation,
    ", recovery", new_droid.recovery_nominal,
    ", upgrade", new_droid.upgrade,
    ", tech_condition", new_droid.tech_condition)
    
print("объект пиратский корабль:",
    "race", new_spaceship.race,
    ", armor", new_spaceship.armor,
    ", load_capacity", new_spaceship.load_capacity,
    ", weapon_slots", new_spaceship.weapon_slots,
    ", droid_recovery", new_spaceship.droid_slot.recovery_nominal * new_spaceship.droid_slot.upgrade , # Решил вывести атрибут вложенного объекта, а не объект полностью
    ", damage", new_spaceship.damage)
    
    
print("игрок:",
    "name", new_player.name,
    ", race", new_player.race,
    ", wealth", new_player.wealth,
    ", nod_account", new_player.nod_account,
    ", damage_accuracy", new_player.damage_accuracy,
    ", technician_skill", new_player.technician_skill,
    ", klissan_kills", new_player.klissan_kills,
    ", spaceship", new_player.spaceship)    


# Задание 1.2

new_droid3 = Droid()
new_droid2 = new_droid

print(new_droid3.generation == new_droid2.generation) # True
new_droid.generation = 3
print(new_droid3.generation == new_droid2.generation) # False