sumador = 1
sumador2 = 1 
total = 0
numero = input("Enter one number greater than 0 = ")
#Un while para saber obligar al usuario introducir un numero positivo#
while int(numero) <= 0:
    print("The number is not right, try again")
    numero = input("Enter one number greater than 0 = ")
#While que permite hacer la operacion#
while sumador2 < int(numero) -1:
    sumador = sumador + 1 
    sumador2 = sumador2 + 1
    total = total + sumador
print ("The sum of the " , numero ,"first numbers is ", total)