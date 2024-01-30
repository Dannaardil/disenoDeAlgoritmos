n = input("cuantos numeros ingresara? : ")
nr = int(input(f"ingrese los {n} numeros enteros: "))

lista = []
lista_2= 0

for num in range(nr):
    nr = int(input(f"n1 = "))
    lista.append(num)

    
for m in lista:
    lista_2 += 1/m

resultado =  nr/lista_2
print(f"H = {resultado}")