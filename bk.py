a= 1
b= 5
c= 6

"""calculo do delta"""
delta= b**2 - 4*a*c
print("O valor do delta é:", delta)

"""calculo da formula de bhaskara"""
x1= (-b + (delta)**(1/2)) / (2*a)
x2= (-b - (delta)**(1/2)) / (2*a)

"""calculo das raizes"""
print("x1 =", x1)
print("x2=", x2)

if delta >= 0:
 print("duas raizes reais diferentes")

if delta < 0:
 print("não existe raiz real")    









