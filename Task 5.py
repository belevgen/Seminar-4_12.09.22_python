# 5 Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


f = open("Seminar 4-1.txt", "r")
first = s.sympify(f.read())
f.close()
f = open('Seminar 4-2.txt', 'r')
second = s.sympify(f.read())
f.close()
print(first)
print(second)
print(first + second)
