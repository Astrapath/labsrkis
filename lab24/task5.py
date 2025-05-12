import json
import random

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Делить на ноль нельзя")
try:
    print(open('hello.txt').readline())
except FileNotFoundError:
    print("файл не был найден")

try:
    x = int(input("введите число: "))
except ValueError:
    print("это не число")