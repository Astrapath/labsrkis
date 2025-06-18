c = input("введите C(латинский символ): ")
a = ['day', 'night', 'gray', 'sus', 'wow', 'huh', 'path', 'crow', 'death', 'home', 'magic', 'yeet']
count = 0
for i in a:
    if len(i) > 1 and i.startswith(c) and i.endswith(c):
        count += 1
print(a)
print(f'слова с символом С, начинаются на него и заканчиваются: {count}')