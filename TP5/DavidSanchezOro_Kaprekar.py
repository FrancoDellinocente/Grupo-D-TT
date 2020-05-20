def comprobarNumero(numero): 
    '''Devolvera True en caso de que el numero tenga 4 o menos cifras,
     y posea al menos una cifra distinta de las demas, de caso contrario devolvera False'''
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
    """ En caso de que el numero ingresado tenga menos de 4 cifras devolvera
        el  numero ingresado completandolo con 0 a la izquierda hasta que tenga 4 cifras"""
    while str.__len__(numero) < 4:
        numero = '0'+numero    
    return numero

def rutinaKaprekar(numero):      
    """"Se ejecutara la rutina de Kaprekar con un numero resivido, independiente de su
        tamanio, se retornara un numero correspondiente a la cantidad de iteraciones realizadas
        hasta llegar a la constante de Kaprekar, "6174" """
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

numero = str(input("Ingrese un numero: ")) #Ingreso de datos para realizar la rutina de Kaprekar
if comprobarNumero(numero) and str.isdecimal(numero):
    print("Se llego a la constante de Kaprekar en "+str(rutinaKaprekar(numero))+" iteraciones")