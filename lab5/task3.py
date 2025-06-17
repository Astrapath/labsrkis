import random
length = int(input("Длинна массива: "))
arr = []
prevnum = 0
for i in range(length):
    prevnum = random.randint(prevnum + 1, prevnum + 50)
    arr.append(prevnum)
print(f'возрастающий массив из случайных четных чисел: {arr}')