# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

def GetNumber(x):
    a = [0] * x
    for i in range(x):
        smt = False
        while not smt:
            try:
                number = float(input(f"Введите {i+1} координату: "))
                a[i] = number
                smt = True
                if a[i] == 0:
                    smt = False
                    print("Координата не должно быть равна 0 ")
            except ValueError:
                print("Ты ошибся. Вводить надо числа!")
    return a


def Quaters(xy):
    answer = 4
    if xy[0] > 0 and xy[1] > 0:
        text = 1
    elif xy[0] < 0 and xy[1] > 0:
        text = 2
    elif xy[0] < 0 and xy[1] < 0:
        text = 3
    print(f"Точка находится в {text} четверти")


koordinate = GetNumber(2)
Quaters(koordinate)    
