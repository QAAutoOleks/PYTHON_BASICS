value1_1 = input("Введіть перший елемент першої множини ")
value1_2 = input("Введіть другий елемент першої множини ")
value1_3 = input("Введіть третій елемент першої множини ")
value1_4 = input("Введіть четвертий елемент першої множини ")
value1_5 = input("Введіть п'ятий елемент першої множини ")

value2_1 = input("Введіть перший елемент другої множини ")
value2_2 = input("Введіть другий елемент другої множини ")
value2_3 = input("Введіть третій елемент другої множини ")
value2_4 = input("Введіть четвертий елемент другої множини ")
value2_5 = input("Введіть п'ятий елемент другої множини ")


# your code goes here
set1 = {value1_1, value1_2, value1_3, value1_4, value1_5}
set2 = {value2_1, value2_2, value2_3, value2_4, value2_5}
set12 = set1 - set2
set21 = set2 - set1
if len(set12) > 0 or len(set21) > 0:
    set3 = set12 | set21
    print(set3)
else:
    set3 = {}
    print(set3)
