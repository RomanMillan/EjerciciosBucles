multiplicador = 0
resultado = 0
numero = input("Introduce un numero entre el 0 y el 10 = ")
if int(numero) < 0 or int(numero) > 10:
    print("Error, Introduce un numero entre el 0 y el 10 = ")
else:
    while multiplicador <= 10:        
        resultado = int(numero) * multiplicador
        print(numero , "*" , multiplicador , "=" ,  resultado)
        multiplicador = multiplicador + 1