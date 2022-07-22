# Вычислить число c заданной точностью d

# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

d = int(input('Введите точность (число от -1 до -10): '))
if d < 0:
    d *= -1

stepen = 10**(d * -1)
k = 2
char = 1
sum = 0
pi = 0.141592653589793
while (pi - sum) > stepen:
    znam = 1
    for i in range(k, k + 3):
        znam *= i
    sum += 4 * char/(znam)
    char *= -1
    k += 2

print(f'Pi = {round(3 + sum, d)}')




