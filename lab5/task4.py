str = input("Введите строку: ")
if str.startswith('abc'):
    str = 'www' + str[3:]
else:
    str += "zzz"
print(f'новая строка: {str}')