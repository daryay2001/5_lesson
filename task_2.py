# 2. Есть список целых, заполненный случайными числами. На основании данных этого массива нужно:
#
# ■ Создать список целых, содержащий только четные числа из первого списка;
#
# ■ Создать список целых, содержащий только нечетные числа из первого списка;
#
# ■ Создать список целых, содержащий только отрицательные числа из первого списка;
#
# ■ Создать список целых, содержащий только положительные числа из первого списка.

import random

NUMS_SIZE = 10
nums_list = []
FIRST = -10
LAST = 10
list_2 = []
list_3 = []
list_4 = []
list_5 = []


for i in range(NUMS_SIZE):
    nums_list.append(random.randint(FIRST, LAST))

for i in nums_list:
    if i % 2 == 0:
        list_2.append(i)
    if i % 2 != 0:
        list_3.append(i)
    if i < 0:
        list_4.append(i)
    if i > 0:
        list_5.append(i)
print(nums_list)
print(list_2)
print(list_3)
print(list_4)
print(list_5)


