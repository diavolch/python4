'''Задайте натуральное число N. Напишите программу, 
которая составит список простых множителей числа N.'''

import math

def find_mult(num):
    mult = []
    div = 2
    while num > 1:
        while num % div == 0:
            mult.append(div)
            num //= div
        div += 1
    return mult

a = 48
print(find_mult(a))