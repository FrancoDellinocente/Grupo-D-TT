#Validacion de ingreso
repDigits=True
while True:
    ingreso=int(input("ingrese numero: "))
    if ingreso > 9999: #si contiene mas de 4 digitos no cumple con los requisitos
            print ("No tiene que contener mas de 4 digitos")
    else:
        
        print("Ingreso valido")
        break

#Comprobar si son repdigits
dig=str(ingreso)
dig=dig[0]
for a in str(ingreso):
    if a != dig:
        repDigits=False
    dig=a
#Rellenar con 0 en el caso de que se haya ingresado un numero de menos de 4 digitos
ingreso=str(ingreso)
dig=len(ingreso)
while len(ingreso)<4:
    ingreso+="0"

resultado=ingreso
contador=0
asc=""
des=""
#en este bucle se hace el proceso
#la iteracion termina cuando se cumpla la constante
while resultado != "6174":
    contador+=1
    #a esta ordenado de forma ascendente y b de forma descendente
    a=sorted(resultado)
    b=sorted(a, reverse=True)
    #juntar todo
    #asc y des se limpian
    asc=""
    des=""
    for i in a:
        asc=asc+i
    for i in b:
        des=des+i
    resultado=str(int(des)-int(asc)) 
    if len(resultado) < 4:
        resultado+="0"   
#Salida
#Para los números repdigits la salida será 8
if repDigits:
    print("8")
else:
    print(str(contador)) 
