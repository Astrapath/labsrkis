nums = [-1, -2, -3, -4 ,-5, 1, 2, 3, 4, 5]
firstpositiv = 1
lastnegativ = 0
for num in nums:
    if num > 0 and num < firstpositiv == 1:
        firstpositiv = num
    if num < 0:
        lastnegativ = num
print(f'первый положительный: {firstpositiv}')
print(f'последний отрицательный: {lastnegativ}')