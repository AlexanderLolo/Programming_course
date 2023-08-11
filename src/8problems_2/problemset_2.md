# Текущее задание
[ссылка на .py файл](problemset_2.py)

# Рефлексия
Принципиальных отличий нет. Но есть по стилю.
1. В моем решении можно было сначала возвращать False и обойтись без continue в конструкции:

        if char.isdigit() and summ + int(char) == 10:
            summ = int(char)
            flag = True
            if count == 3:
                count = 0
                continue
            return False
   
3. стремился избежать вложенных конструкций if. Возможно получилось менее наглядно
        elif char.isdigit():
            summ = int(char)
            count = 0



