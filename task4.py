'''Задана натуральная степень k. Сформировать случайным образом 
список коэффициентов (значения от 0 до 100) многочлена 
и записать в файл многочлен степени k(до 6 степени).*

        *Пример:* 
        - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0'''

import random
k = 6
lst = [random.randint(0,5) for x in range(k+1)]
print(lst)
string = ''
lst2 = []
for i in range(len(lst)):
        if k == 1 and lst[i] != 0 and lst[i] != 1:
                lst2.append(str(lst[i]) + '*x')
        elif k == 0 and lst[i] != 0:
                lst2.append(str(lst[i]))
        elif lst[i] == 0:
                pass
        elif lst[i] == 1 and k != 0 and k != 1:
                lst2.append('x^' + str(k))
        elif lst[i] == 1 and k == 1:
                lst2.append('x')
        else:
                lst2.append(str(lst[i]) + '*x^' + str(k))
        k -= 1
print(lst2)
string = ' + '.join(lst2)
string = string + ' = 0'
print(string)

my_file = open("file.txt", "a")
my_file.write(string + '\n')
my_file.close()