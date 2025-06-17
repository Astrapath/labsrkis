import  ast
arr = ast.literal_eval(input("Введите числа (в квадратных скобках): "))
for i in range(len(arr)):
    arr[i] *= -1
print(f'инвертированный массив: {arr}')
