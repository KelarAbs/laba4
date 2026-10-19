# # задание 1

# while True:
#     N = int(input("Введите число больше нуля: "))
#     if N<0:
#         print("Введено отрицальное число!")
#         break
#     elif N>0:
#         break
# while N>0:
#     print(N%10)
#     N//=10


# # Задание 2
# from math import cos,sin

# x0,x,dx = float(input("Введине стартовое значение: ")),float(input("Введине конечное значение: ")),float(input("Введине значение шага: "))

# while x0<=x:
#     if x0<0:
#         z = (x0)**2
#         print(z)
#         x0=x0+dx
#     elif (x0>0) and (x0<=1):
#         z = sin(x0)
#         print(z)
#         x0=x0+dx
#     elif x>1:
#         z = cos(x0)
#         print(z)
#         x0=x0+dx


# Задание 3

while True:
    x,y = int(input("Введите x: ")), int(input("Введите y: "))
    if x<0 or y<0:
        print("Введено отрицательное число!")
        break
    else:
        break

def NOD(x,y):
    if y !=0:
        if (x>y) :
            while (x%y!=0):
                y = x-y
            return y
        elif (x<y):
            while (y%x==0):
                x=y-x
            return y
            



res = NOD(x,y)
print(res)