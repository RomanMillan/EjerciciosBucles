bandera=True
numero=input("Introduce un numero: ")
contador=1
acumuMedia=int(numero)
while int(numero)!=0:
    if int(numero)%2 ==0:
        bandera=False
    numero=input("introduce un numero: ")
    contador=contador +1
    acumuMedia=acumuMedia + int(numero)
contador=contador -1 #le resto uno porque cuenta el 0#
print("El numero de elementos es: " +str(contador))
if bandera!=True:
    print("Hay algun impar")
media= acumuMedia/contador
print("la media es: " +str(media))