import ast
import math
def sumandprod(arr):
    psitivsum = 0
    for x in arr:
        if x > 0:
            psitivsum += x
    minindx = 0
    minval = arr[0]
    maxindx = 0
    maxval = arr[0]
    for i in range(1, len(arr)):
        currentval = arr[i]
        if currentval < minval:
            minindx = i
            minval = currentval
        if currentval < maxval:
            maxindx = i
            maxval = currentval
    if minindx < maxindx:
        numbetwminmax = arr[minindx + 1:maxindx]
    else:
        numbetwminmax = arr [maxindx + 1:minindx]
    prodbetween = math.prod(numbetwminmax)
    return psitivsum, prodbetween
arr = ast.literal_eval(input("введите числа(в квадратных скобках): "))
result = sumandprod(arr)
print(f"Сумма положительных:{result[0]}")
print(f"Сумма чисел между минимальным и максимальным:{result[1]}")
