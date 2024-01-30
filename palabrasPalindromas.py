palabra = input("ingrese la palabra: ")
palabra_in = palabra[::-1]

if palabra == palabra_in:
    print(f"{palabra} es palindromo")
    
else: 
    print(f"{palabra} no es palindromo")