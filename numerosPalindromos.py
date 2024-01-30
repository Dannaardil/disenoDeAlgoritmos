numero = input("ingrese el numero: ")

numero_in = numero[::-1]

if numero == numero_in:
    print(f"{numero} es palindromo")
else : 
    print(f"{numero} no es palindromo")