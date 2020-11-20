acum = 0
contador = 0
print("Enter one number greater than 0")
numero = input("How many numbers do you want input? ")
while int(numero) < 0:
    print("The number is not valid, it should be greater than 0")
    numero = input("How many numbers do you want input? ")
while int(numero) != 0:
    acum += int(numero)
    contador += 1
    numero = input("How many numbers do you want input? ")
print("The medium is ", acum / contador)