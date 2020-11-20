BAN = True
RESP = "N"
PREG = ""
ACUM = 0
COMP = 0
MENOR = 0
RES = 999
while PREG != RESP:
    numero = input("Enter one number: ")
    ACUM += int(numero)
    if COMP > int(numero):
        MENOR = ACUM
        if MENOR > RES:
            MENOR = RES
        RES = MENOR
        COMP -= COMP
        BAN = False
    else:
        COMP -= COMP
    COMP += ACUM
    ACUM -= ACUM   
    PREG = input("Do you want to enter more number (Y/N)?")
if BAN == False:
    print("The smallest number is: ", str(RES))
else:
    print("The smallest number is ", numero)