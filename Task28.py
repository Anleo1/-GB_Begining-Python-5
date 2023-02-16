def sum(a,b):
    if(b>1):
        return sum(a,b-1)+1
    return (a+1)
    
a = int(input("Введите 1oe число: "))
b = int(input("Введите 2oe число: "))
print(a,"+",b,"=",sum(a,b))