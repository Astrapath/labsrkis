def calcformula(a,b):
    return  (a + 4 + b) * (a - 3 * b) + a * 2
a  = float(input('Число А: '))
b  = float(input('Число Б: '))
print(f"Результат: {calcformula(a, b)}")