# Рефлексия
## Задание 4.1

Отметил для себя, что в эталонном решении полиморфизм использовался два раза
1. При вызове метода `self._weapon.get_damage(dist)` вызываются разные методы для разных классов оружия. Это - **полиморфизм подтипов**

2. При вызове `def attack_enemy(self, enemy, dist)` похоже используется **ad hoc полиморфизм**, так как `enemy`, грубо говоря, может быть и животным, если реализовать отдельный такой класс. Главное, чтобы был реализован метод `enemy.receive_damage`. В то же время, это не совсем полноценный ad hoc полиморфизм, так как набор передаваемых параметров в метод `receive_damage` должен быть одинаковым, иначе придется мудрить с `if`. В виду вышесказанного, данный полиморфизм также очень похож на полиморфизм подтипов, разве что `enemy` не обязательно здесь должны быть подтипами одного и того же типа.

## Задание 4.2

Вместо обычного цикла использовал новую особенность, как в обучающих материалах

```
> barsik = Cat()
> galka = Bird()
> ams = [barsik, galka]

> for ani in ams:
>     ani.Run(10)
```
# Текущее задание
[ссылка на .py файл](first.py)
![](/Images/firstimage.png)
