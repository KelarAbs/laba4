# задание 1

while True:
    N = int(input("Введите число больше нуля: "))
    if N<0:
        print("Введено отрицальное число!")
        continue
    break
while N>0:
    print(N%10)
    N//=10


# Задание 2
from math import cos,sin
while True:
    x0,x,dx = float(input("Введине стартовое значение: ")),float(input("Введине конечное значение: ")),float(input("Введине значение шага: "))
    if (x>x0 and dx<0) or (x0>x and dx>0):
        print("Некорректный ввод шага!")
        continue
    if dx==0:
        print("Шаг не может быть равен нулю!")
        continue
    break

if x0<=x:
    while x0<=x:
        if x0<0:
            z = (x0)**2
            print(z)
            x0=x0+dx
        elif (x0>0) and (x0<=1):
            z = sin(x0)
            print(z)
            x0=x0+dx
        elif x>1:
            z = cos(x0)
            print(z)
            x0=x0+dx
else:
    while x0>=x:
        if x0<0:
            z = (x0)**2
            print(z)
            x0=x0+dx
        elif (x0>0) and (x0<=1):
            z = sin(x0)
            print(z)
            x0=x0+dx
        elif x>1:
            z = cos(x0)
            print(z)
            x0=x0+dx


# Задание 3

while True:
    x,y = int(input("Введите x: ")), int(input("Введите y: "))
    if x<0 or y<0:
        print("Введено отрицательное число!")
        continue
    break

def NOD(x,y):
    while y != 0:
        x,y=y , x%y
    return x   
            

res = NOD(x,y)
print(res)