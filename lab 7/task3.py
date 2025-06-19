arr = [-2, 10, -10, 22, 17, 77, 89, -1]
arr2 = []
for i in arr:
    if i > 0 and 10 <= i <= 99:
        arr2.append(i)
arr2.sort()
print(arr)
print(arr2)