# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
from tkinter import N


def GetNumber(x):
    number = [0] * x
    for i in range(x):
        smt = False
        while not smt:
            try:
                number = float(input(f"Введите номер четверти: "))
                smt = True
                if  number < 1 or number > 4:
                    smt = False
                    print("Число должно быть от 1 до 4 ")
            except ValueError:
                print("Вводить надо числа!")
    return number

def QuaterIdentify(n):
    quater = n
    if n == 1:
        print("x > 0, y > 0")
    elif n == 2:
        print("x < 0, y > 0")
    elif n == 3:
        print("x < 0, y < 0")
    else:
        print("x > 0, y < 0")

n = GetNumber(1)
QuaterIdentify(n)