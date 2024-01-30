n = int(input("cuantos numeros ingresara? : "))
h = 0
for num in range (n):
    m  = int(input(f"{num+1}= ")) 
    h += 1/m
    resultado = n/h 
print(f"H = {resultado}")