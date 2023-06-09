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
prod_minmax = 0
sum_fl = 0
try:
    LIST_SIZE = int(input("Enter list size: "))

    if LIST_SIZE < 1:
        raise Exception("Enter 1 or more")

    user_list = []
    START = int(input("Enter first number: "))
    END = int(input("Enter last number: "))

    # if START < END:
    #     raise ValueError("End should be more than start")

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

    for i in user_list:
        if user_list.index(i) % 3 == 0:
            prod_three = prod_three * i

    min_value = min(user_list)
    max_value = max(user_list)

    min_ind = user_list.index(min_value)
    max_ind = user_list.index(max_value)

    if min_ind < max_ind:
        print(user_list[min_ind:max_ind])
    else:
        print(user_list[max_ind + 1:min_ind])

    print(f"Sum of minus number: {minus_num}")
    print(f"Sum of even number: {even_num}")
    print(f"Sum of odd number: {odd_num} ")
    print(f"The product of elements with an index divisible by three: {prod_three}")

except ValueError as error:
    print(error)
except Exception as error:
    print(error)