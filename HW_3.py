#
# # 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# # Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# # in
# # 5
# #
# # out
# # [10, 2, 3, 8, 9]
# # # 22
#
from random import sample
# def list_random_num (count: int):
#     list_num = sample(range(1, count*2), count)
#     return list_num
#
# def sum_odd_position(list_num: list):
#     sum_num = 0
#     for i in range(0, len(list_num)):
#         if list_num[i] % 2 ==1:
#             sum_num += list_num[i]
#     return sum_num
#
# all_list = list_random_num(int(input(': ')))
# print(all_list)
# print(sum_odd_position(all_list))

# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# def list_random_num (count: int):
#      list_num = sample(range(0, count*2), count)
#      return list_num
#
# def product_pairs_numbers(list_num: list):
#     multiplication = 0
#     res_list = []
#     len_list = len(list_num)
#     for i in range(len_list // 2):
#         res_list.append(list_num[i] * list_num[len_list - i - 1])
#
#     if len_list % 2:
#         res_list.append(list_num[len_list // 2])
#     return res_list
#
# new_list = list_random_num(int(input(':' )))
# print(new_list)
# print(product_pairs_numbers(new_list))


#  Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.

# def transformation_num(num: int):
#     list_num = []
#     while num > 0:
#         list_num.insert(0, num % 2)
#         num //= 2
#     print(*list_num, sep='')
#
# transformation_num(int(input()))


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fibonacci(n):
    a, b = -1, -1
    for i in range(n):
        yield a
        a, b = b, a + b

data = list(fibonacci(int(input())))
print(data)