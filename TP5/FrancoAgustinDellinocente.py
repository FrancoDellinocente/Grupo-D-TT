def validarNumero(numero):
    num = str(numero)
    numeroCorrecto = True
    for i in num:
        codigoASCII = ord(i)
        if codigoASCII < 48 or codigoASCII > 57:
            numeroCorrecto = False
    if numeroCorrecto:
        if len(num) == 1:
            num = '000' + num
        else:
            if len(num) == 2:
                num = '00' + num
            else:
                if len(num) == 3:
                    num = '0' + num
        return numerosDiferentes(num)
    return False

def numerosDiferentes(numero):
    digito_1 = int(numero[0])
    cont = 0
    while cont < len(numero) - 1:
        cont += 1
        digito_2 = int(numero[cont])
        if digito_1 != digito_2:
            return True
    return False

def numMay(numero):
    num = str(numero)
    if len(num) == 1:
        num = '000' + num
    else:
        if len(num) == 2:
            num = '00' + num
        else:
            if len(num) == 3:
                num = '0' + num

    cifraMayor = ""
    cifraCompleta = False
    numAux = 0
    while cifraCompleta == False:
        mayor = int(num[0])
        cont = 0
        while cont < len(num) -1:
            cont += 1
            digito = int(str(num[cont]))
            if digito > mayor:
                mayor = digito
                numAux = cont
        #cont = 0
        cifraMayor +=str(mayor)
        num = num.replace(str(mayor), "", 1)

        if len(cifraMayor) == 4:
            cifraCompleta = True
    return int(cifraMayor)

def Kaprekar(numero):
    restaNumeros = 0
    numeroIteraciones = 0
    numeroMayor = 0
    numeroMenor = 0
    numMen = ""
    while restaNumeros != 6174:
        numeroMayor = numMay(numero)
        numMayor = str(numeroMayor)
        numeroMenor = int(numMayor[::-1])
        restaNumeros = numeroMayor - numeroMenor
        numeroIteraciones += 1
        numero = restaNumeros
        if numeroIteraciones == 8:
            return 8
    return numeroIteraciones


numero_casosPrueba = int(input("Ingresa el numero de veces que desea realizar la constante de Kaprekar: "))
cont = 1
while cont <= numero_casosPrueba:
    numeroIng = int(input("numero:"))
    if numeroIng == 1674:
        print("0")
    else:
        if validarNumero(numeroIng):
            print("El numero: "+ str(numeroIng) + ", Iteraciones: " + str(Kaprekar(numeroIng)))
        else:
            print('8')
    cont += 1