def f(a,b):
    if(b>2):
       return (f(a,b-1)*a)
    return (a**2)

a = int(input("Введите число: "))
b = int(input("Введите степень: "))
print(a,"в степени",b,"=",f(a,b))