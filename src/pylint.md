## 1.
`Consider using enumerate instead of iterating with range and len`
```
>    for i in range(len(list)):
>
>        if list[i] in dict.keys():
>           dict[list[i]] += 1
>        else:
>            dict[list[i]] = 1
```
исправлено на 
```
>   for i in list:
>        if i in dict.keys():
>            dict[i] += 1
>        else:
>            dict[i] = 1
```
## 2.	
`Consider iterating the dictionary directly instead of calling .keys()`
Исправлено на 
```
>   for i in list:
>        if i in dict:
>            dict[i] += 1
>        else:
>            dict[i] = 1
```
## 3.
`Redefining built-in 'dict', “list”`
Исправлено на `“dict_”, “list_”`

## 4.	
`Unused variable 'i'`
 ```
>list = []
>    for i in range(100):
>        list.append(random.randint(1,10))
```
исправлено на
```
>list = [random.randint(1, 10) for i in range(100)]
```

## 5.
`Argument name "n" doesn't conform to snake_case naming style`
```
>def second_excersise_funct(list_, n):
```
Исправлено на 
```
>def second_excersise_funct(list_, num):
```

## 6.
`Missing function or method docstring`
Исправлено на 

```
>def second_excersise_funct(list_, num):
>    '''returns list's values which number is more than num '''
```
## 7.	
`Missing module docstring`
Поместил в начало всего модуля описание


