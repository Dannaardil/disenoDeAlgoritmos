a = int(input("ingrese el a: "))
b = int(input("ingrese b: "))


# solucion = (-b/a)

if a !=0 :
    print("tiene solucion unica =", (-b/a))
elif a == 0 and b != 0 :
    print("la ecuacion no tiene soluciones")
elif a == 0 and b == 0:
    print("La ecuacion tiene soluciones infinitas")
else: 
    print("ERROR")