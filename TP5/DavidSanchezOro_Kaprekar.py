def comprobarNumero(numero):
    if str.__len__(numero) == 4:
        for i in range(str.__len__(numero) -1):
            if numero[i] != numero[i+1]:
                return True
    elif str.__len__(numero) < 4:
        for i in range(str.__len__(numero)):
            if numero[i] != '0':
                return True
    return False

def completarNumero(numero):
    while str.__len__(numero) < 4:
        numero = '0'+numero    
    return numero

def rutinaKaprekar(numero):      
    contador = 0      
    while numero != "6174":
        contador += 1
        numero = completarNumero(numero)
        aux0 = sorted(numero, key=None, reverse=False)
        aux1 = sorted(numero, key=None, reverse=True)
        numero = ""
        numeroRev = ""          
        for i in range(len(aux0)):
            numero += aux0[i]
            numeroRev += aux1[i]
        if int(numero) > int(numeroRev):
            numero = str(int(numero) - int(numeroRev))
        else:
            numero = str(int(numeroRev) - int(numero))
    return contador       

numero = str(input("Ingrese un numero: "))
if comprobarNumero(numero) and str.isdecimal(numero):
    print("Se llego a la constante de Kaprekar en "+str(rutinaKaprekar(numero))+" iteraciones")