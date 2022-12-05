'''Задайте последовательность чисел. Напишите программу, 
которая выведет список неповторяющихся элементов исходной последовательности.'''

lst = [1, 2, 1, 5, 2, 3, 4, 2, 1]

# Короткое решение
# lst2 = {x for x in lst if lst.count(x) == 1}
# print(lst2)

# Решение через циклы
lst2 = []
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] == lst[j]:
            lst2.append(lst[i])
for i in range(len(lst2)):
    lst.remove(lst2[i])
print(lst)