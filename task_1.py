# 1. В списке целых, заполненном случайными числами вычислить:
#
# ■ Сумму отрицательных чисел;
#
# ■ Сумму четных чисел;
#
# ■ Сумму нечетных чисел;
#
# ■ Произведение элементов с индексами кратными 3;
#
# ■ Произведение элементов между минимальным и максимальным элементом;
#
# ■ Сумму элементов, находящихся между первым и последним положительными элементами.

import random

minus_num = 0
even_num = 0 #чет
odd_num = 0 #нечет
prod_three = 1
prod_minmax = 1
sum_fl = 0
ind_list = []
try:
    LIST_SIZE = int(input("Enter list size: "))

    if LIST_SIZE < 1:
        raise Exception("Enter 1 or more")

    user_list = []
    START = int(input("Enter first number: "))
    END = int(input("Enter last number: "))

    if START > END:
        START, END = END, START

    for i in range(LIST_SIZE):
        user_list.append(random.randint(START, END))

    print(user_list)

    for i in user_list:
        if i < 0:
            minus_num += i

    for i in user_list:
        if i%2 == 0:
            even_num +=i
        elif i%2 != 0:
            odd_num += i

    for i in range(0, len(user_list), 3):  # шаг 3 для индексов, в данном случае 0 входит.
        prod_three *= user_list[i]

    min_value = min(user_list)
    max_value = max(user_list)

    min_ind = user_list.index(min_value)
    max_ind = user_list.index(max_value)

    if min_ind < max_ind:
        for i in range(min_ind + 1, max_ind):
            prod_minmax *= user_list[i]
    else:
        for i in range(max_ind + 1, min_ind):
            prod_minmax *= user_list[i]

    for i in user_list:
        if i > 0:
            ind_list.append(user_list.index(i))

    first_pos = ind_list[0]  # indexes
    last_pos = ind_list[-1]

    for i in range(first_pos + 1, last_pos):
        sum_fl += user_list[i]

    print(f"Sum of minus number: {minus_num}")
    print(f"Sum of even number: {even_num}")
    print(f"Sum of odd number: {odd_num} ")
    print(f"The product of elements with an index divisible by three: {prod_three}")
    print(f"Product between min and max: {prod_minmax}")
    print(f"Sum between first and last positive element: {sum_fl}")

except ValueError as error:
    print(error)
except Exception as error:
    print(error)