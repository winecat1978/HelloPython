# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
def GetDots(n, mess):
    a = [0] * n
    for i in range(n):
        smt = False
        while not smt:
            try:
                number = float(input(f"Введите {i+1} координату точки {mess}: "))
                a[i] = number
                smt = True
            except ValueError:
                print("Ты ошибся. Вводить надо числа!")
    return a

def LengthCount(Dot_A, Dot_b):
    first_step_res = (Dot_A[0]-Dot_B[0])**2 + (Dot_A[1]-Dot_B[1])**2
    second_step_res = pow(first_step_res, 0.5)
    return second_step_res


Dot_A = GetDots(2, "A")
Dot_B = GetDots(2, "B")
result = LengthCount(Dot_A, Dot_B)
print(result)