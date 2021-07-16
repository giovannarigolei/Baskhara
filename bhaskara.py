import math

a = (float(input("Digite o valor de A da função quadrática: ")))

b = (float(input("Digite o valor de B da função quadrática: ")))

c = (float(input("Digite o valor de C da função quadrática: ")))
 
delta= b**2-4*a*c

if delta > 0:
     X = (-(b) - math.sqrt (delta))/(2*a)
     Y = (-(b) + math.sqrt (delta))/(2*a)

if delta > 0 and X > Y:
       print("As raízes da equação são", Y, "e", X)
         
if delta > 0 and Y > X: 
        print("As raízes da equação são", X, "e", Y)

if delta == 0:
        X = (-(b))/2*a
        print("A raiz desta equação é", X)


if delta < 0:
        print("Esta equação não possui raízes reais")

