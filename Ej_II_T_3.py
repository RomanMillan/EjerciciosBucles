numeroDeNumeros = input("How many numbers do you want input? ")
while int(numeroDeNumeros) <= 0:
    if int(numeroDeNumeros) ==0:
        print("Enter one number greater than 0")
    else:
        print("The number is not valid, it should be greater than 0")
    numeroDeNumeros = input("How many numbers do you want input ")
while int(numeroDeNumeros) > 0:
    numero = input("input number: ")
    while int(numero) <0:
        print("El numero debe ser positivo")
        numero = input("input number: ")
    if int(numero) % 2 == 0:
        print("The number ", numero , " is odd")
    else:
        print("The number ", numero , " is even")
    int(numeroDeNumeros) += 1