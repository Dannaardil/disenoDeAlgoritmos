rol = input("ingrese el rol: ")

rol_in= rol[::-1]

secuencia = [2,3, 4, 5, 6, 7]
resultado = 0

for i, digito in enumerate(rol_in):
    multiplicador = secuencia[i%len(secuencia)]
    #print(i%len(secuencia))
    resultado += int(digito)*multiplicador
modulo = resultado%11
resta= 11-modulo
final= int(rol)-resta 

print(f"el digito verificador es {final}")
