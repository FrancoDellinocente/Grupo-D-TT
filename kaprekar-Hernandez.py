

#Validacion de ingreso
while True:
    ingreso=int(input("ingrese numero: "))
    if ingreso == 1111 or ingreso == 2222 or ingreso == 3333 or ingreso == 4444 or ingreso == 5555 or ingreso == 6666 or ingreso == 7777 or ingreso == 8888 or ingreso == 9999 or ingreso == 0:
        print("Tienen que haber dos diferentes")
    else:
        if ingreso > 9999: #si contiene mas de 4 digitos no cumple con los requisitos
            print ("No tiene que contener mas de 4 digitos")
        else:
            print("Ingreso valido")
            break
#Rellenar con 0 en el caso de que se haya ingresado un numero de menos de 4 digitos

ingreso=str(ingreso)
dig=len(ingreso)
while len(ingreso)<4:
    ingreso+="0"

resultado=ingreso
contador=0
asc=""
des=""
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
    print(resultado)
    print("Vuelta: "+str(contador))

