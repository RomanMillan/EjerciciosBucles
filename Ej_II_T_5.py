numeroT = 0
numero = input("Enter a number: ")
while int(numero) > 0:
    numeroT = numeroT + 1
    numero = input("Enter a number: ")
print("You have entered ", str(numeroT) , " positive numbers.")