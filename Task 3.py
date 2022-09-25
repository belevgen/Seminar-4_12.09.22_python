# 3 Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

list_inp = [33, 57, 12, 33, 75, 100, 19, 75, 12, 75, 25]

res_list = []

for item in list_inp:
    if item not in res_list:
        res_list.append(item)

print("Уникальные элементы списка: ")
for item in res_list:
    print(item)