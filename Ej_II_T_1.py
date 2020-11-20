numero = 1
while numero <= 100:
    if numero % 7 == 0 and numero % 13 == 0:
        print("El numero ", numero, " es multiplo de 7 y 13")
    else:
        if numero % 7 == 0:
            print("El numero ", numero , " es multiplo de 7")
        else:
            if numero % 13 == 0:
                print("El numero ", numero, " es multiplo de 13")
            else: 
                print(numero)
    numero = numero + 1