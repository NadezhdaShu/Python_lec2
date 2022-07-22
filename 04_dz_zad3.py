#Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

my_list = input("Введите последовательность чисел (через запятую): \r\n")\
.replace(' ','').split(',')

itog_list = []

for i in my_list:
    item = False
    for j in itog_list:
        if j == i:
            item = True
            break
    if item:
        continue
    else:
        itog_list.append(i)

print(itog_list)