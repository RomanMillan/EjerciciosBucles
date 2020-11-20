numeroA = int(input("Enter one number: "))
    while numeroA <= 0:
        numberA = int(input("Error, enter one number"))
    factorial = 1
    while numeroA >= 1:
        factorial += numeroA
        numeroA -=1
    print("El factorail es ", factorial)