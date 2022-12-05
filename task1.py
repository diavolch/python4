'''Вычислить число ПИ c заданной точностью d
    *Пример:* 

    - при d = 0.0001, π = 3.1415.    10^-1 ≤ d ≤ 10^-10'''

import math

d = 0.0001
num_pi = str(math.pi)
count = 0
while d < 1:
    d *= 10
    count += 1
    
print(num_pi[:(2+count)])