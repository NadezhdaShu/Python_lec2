# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# !!!! Не работает, а почему не могу понять.... :((( Help me!

def Udal(inpt: str):
    ind = inpt.find("x")
    if(ind == -1):
        return inpt
    else:
        return inpt[:ind]


path_file1 = "file_1.txt" # этом файле такой многочлен взяла 97x^6 + 4x^5 + 88x^4 + 1x^3 + 9x^2 + 25x^1 + 22
path_file2 = "file_1.txt" # а тут такой 39x^3 + 49x^2 + 91x^1 + 66

with open(path_file1, 'r') as data:
    data_file1 = data.read()

with open(path_file2, 'r') as data:
    data_file2 = data.read()

list1 = data_file1.split(" + ")[::-1]
list2 = data_file2.split(" + ")[::-1]

if len(list1) > len(list2):
    for i in range(len(list1) - len(list2)):
        list2.append('0')
else:
    for i in range((len(list2) - len(list1))):
        list1.append('0')

for i in range(len(list1)):
    list1[i] = Udal(str(list1[i]))
    list2[i] = Udal((list2[i]))
    
summ_list = [0] * len(list1)

for i in range(len(list1)):
    summ_list[i] = int(list1[i]) + int(list2[i])

print(f"Сумма многочленов: \r\n{summ_list}") # не работает у меня....(((
