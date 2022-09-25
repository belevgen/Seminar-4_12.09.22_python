# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.


up = 10
down = -10
k = rnd.randint(1, 101)


def non_zero_int(lower, upper):
    lower, upper = min(lower, upper), max(lower, upper)
    if lower == (upper - 1):
        return lower
    number = 0
    while number == 0:
        number = rnd.randint(lower, upper)
    return number


def get_random_equation(k):
    equation = '0'
    new_element = 0
    if k == 0:
        return equation
    elif k == 1:
        return str(non_zero_int(down, up))
    else:
        equation = f'{non_zero_int(down, up)}x^{k - 1} '
        for i in range(k - 1):
            new_element = rnd.randint(down, up)
            if new_element > 0:
                equation += f'+{new_element}x^{k - 2 - i} '
            elif new_element < 0:
                equation += f'{new_element}x^{k - 2 - i} '
    equation = equation.replace("x^1", 'x')
    equation = equation.replace('x^0', '')
    if equation[0] == '+':
        equation = equation[1:]
    return equation


x = s.symbols('x')
expr = non_zero_int(down, up) * x ** (k - 1)
for i in range(k - 1):
    expr += rnd.randint(down, up) * x ** (k - 2 - i)
os.remove('33.txt')
f = open("33.txt", "x")
f.writelines(get_random_equation(k) + '\n')
f.writelines(str(expr))
f.close()