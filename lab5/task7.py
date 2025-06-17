x = float(input("введите координату X точки: "))
y = float(input("введите координату Y точки: "))
radius = float(input("радиус круга: "))
print("точка в круге" if x * x + y * y < radius * radius else "точка вне круга")