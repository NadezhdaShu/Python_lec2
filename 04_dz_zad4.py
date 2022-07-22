# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def coeficint(k):
    result = ""
    for i in range(k, -1, -1):
        if i == 0:
            result += str(random.randint(0, 100))
        else:
            result += f"{random.randint(0, 100)}x^{i} + "
    return(result)

k = int(input("Введите степень k = "))

result = coeficint(k)

print(result)

with open('file.txt', 'a') as data:
    data.write(result)
