total = 0
acum = 0
numero = input("Enter one number: ")
numero2 = input("Enter one number: ")
while total < int(numero):
    acum = acum + int(numero2)
    total += 1
print("The product is ", str(acum))