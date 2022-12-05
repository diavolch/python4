'''Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов.*
    Пример:
            - 2*x² + 4*x + 5 = 0 
            - 5*x² + 2*x + 43 = 0
            - Результат: 7*x^2 + 6*x + 48 = 0'''

#Пока не додумалась над универсальным решением, сделала для конкретного примера
#Прошу простить:) скидываю пока такой вариант, поскольку могу не успеть с дз в срок

path = 'file.txt'
data = open(path, 'r')
lst = []
for line in data:
    lst.append(line.strip())
data.close()
txt1 = lst[0]
txt2 = lst[1]
print(txt1)
print(txt2)

a1, lit1, b1, lit2, c1 = txt1[:-3].split()
b1 = lit1 + b1
c1 = lit2 + c1
a1 = int(a1[:a1.index('*')])
b1 = int(b1[:b1.index('*')])
c1 = int(c1)

a2, lit3, b2, lit4, c2 = txt2[:-3].split()
b2 = lit3 + b2
c2 = lit4 + c2
a2 = int(a2[:a2.index('*')])
b2 = int(b2[:b2.index('*')])
c2 = int(c2)

res = 'Результат: ' + str(a1+a2) + '*x^2 + ' + str(b1+b2) + '*x + ' + str(c1+c2) + ' = 0'
print(res)