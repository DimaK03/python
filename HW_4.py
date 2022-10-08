# Вычислить число c заданной точностью d
from decimal import Decimal


# def accuracy(num, accu):
#     number = Decimal(f'{num}')
#     return number.quantize(Decimal(f'{accu}'))
# print(accuracy(float(input('enter number:')),float(input('enter accuracy 0.0001: '))))


# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# def multipliers_numbers(num):
#     i = 2
#     lst = []
#     while i <= num:
#         if num % i == 0:
#             lst.append(i)
#             num //= i
#             i = 2
#         else:
#             i += 1
#     print(f"Простые множители числа  приведены в списке: {lst}")
#     return num
#
# print(multipliers_numbers(int(input())))

# . Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# from random import randrange
# def list_rand(count: int):
#
#     list_nums = []
#     for i in range(count):
#         list_nums.append(randrange(count))
#
#     return list_nums
#
#
# def multi_num(list_nums: list):
#     result = []
#     my_dict = {}.fromkeys(list_nums, 0)
#
#     for i in list_nums:
#         my_dict[i] += i
#
#     for j in my_dict:
#         if my_dict[j] == 1:
#             result.append(j)
#
#     return result
# list = list_rand(int(input(': ')))
# print(list)
# print(multi_num(list))

