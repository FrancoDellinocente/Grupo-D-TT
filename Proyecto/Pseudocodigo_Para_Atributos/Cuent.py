from Uniti import Unidad

class Cuenta(object):
    
    '''
    Representara una operacion aritmetica obtenida a partir de un string, y realizara
    la misma, obteniendo su resultado. 
    Los valores numericos soportados son enteros.
    Las posibles operaciones seran suma, resta, multiplicacion, division y potenciacion,
    para realizar las mismas la cuenta se hara de corrido sin tener en cuenta la separacion
    en terminos combensional de la matematica. Para separar en terminos, se podran utilizar
    parentesis, siendo soportado un solo nivel de parentesis, es decir, no se podran utilizar
    parentesis dentro de parentesis.
    Tambien reconocera nombres de variables de las cuales se verificara su existencia en
    una base de datos, para obtener su valor y realizar las operaciones con el mismo.
    '''
        
    def __init__(self, cadena):
        '''
        El constructor tomara un string que contenga la operacion deseada, creara la matriz
        donde se alojara la cuenta, el texto que representara a la operacion realizada y 
        llamara al metodo addUnidades para obtener el resultado de la operacion.
        '''
        self.__cuenta = [[]]
        self.__texto = ""
        self.__resultado = self.addUnidades(str(cadena))      
    
    def addUnidades(self, cadena):
        '''
        En este metodo se transformaran las diferentes partes del string que contiene la operacion,
        o agregados para la misma, en instancias de la clase Unidad y luego ordenara estas instancias
        dentro del atributo matriz "cuenta". La organizacion estara determinada por la separacion en
        terminos con parentesis, ubicando cada termino en una columna diferente de la matriz.
        '''    
        self.__texto += cadena
        variable = False
        numero = ""
        f = 0
        for i in range(len(cadena)): #Se recorre el string conteniendo la operacion caracter por caracter
            if variable:  #De haber sido reconocido como nombre variable el primer caracter se procedera por esta condicion hasta el final del mismo
                numero += cadena[i]  #Se arma el valor para la instancia de Unidad, concatennando uno por uno sus digitos
                if i+1 == len(cadena) or cadena[i+1] in "+-*/^)(": #Al encontrarse con un operador o el final de la cadena se terminara la carga del nombre de variable
                    variable = False;
                    aux = Unidad(numero) #Creacion de la instancia de unidad con el valor correspondiente
                    self.__cuenta[f].append(aux) # Agregacion ordenada de la instancia a el atributo __cuenta
                    numero = ""                
            elif ((i == 0 or cadena[i-1] == '(') and (cadena[i] == '-')) or (cadena[i] not in "+-*/()") and cadena[i] in "0123456789": #Si el valor es reconocido como numerico, se pasara por esta condicion hasta el final del mismo                
                numero += cadena[i]                
                if i+1 == len(cadena):  #Si se encuentra en el ultimo caracter del string cerrara el valor de la unidad aqui
                    aux = Unidad(numero)
                    self.__cuenta[f].append(aux)
                    numero = ""
                elif (cadena[i] in "+-*/^") and (i != 0 and cadena[i-1] != '('): #Segunda comprobacion de no ser un operador o un parentesis
                    aux = Unidad(numero)
                    self.__cuenta[f].append(aux)
                    numero = ""
                else:
                    if i+1 == len(cadena): #Si se encuentra en el ultimo caracter del string cerrara el valor de la unidad aqui
                        aux = Unidad(numero)
                        self.__cuenta[f].append(aux)
                        numero = ""
                    elif cadena[i+1] in "+-*/)^": #Si el siguiente caracter es un parentesis o un operador se cerrara el valor de la unidad aqui
                        aux = Unidad(numero)
                        self.__cuenta[f].append(aux)
                        numero = ""
            elif (cadena[i] in "()") and (i != 0 and i+1 != len(cadena)): #Si se reconoce la unidad como parentesis se entrara por esta condicion
                if not cadena[i-2] in "()": #Si no son parentesis separados por un solo operador se agregara un termino
                    self.__cuenta.append([])
                    f += 1
                if cadena[i+1] in "+-*/^" and i !=0 and cadena[i+2] not in "0123456789": #Si el valor siguiente dentro del parentesis no es un numero solo, se agregara un termino
                    aux = Unidad(cadena[i+1])
                    self.__cuenta[f].append(aux)
                    self.__cuenta.append([])
                    f += 1                    
            elif cadena[i] not in "()" '''and cadena[i-1] not in "()"''' and cadena[i] in "/*-+^": #Si se reconoce como un operador antes de un parentesis, se entra por esta condicion
                aux = Unidad(cadena[i])
                if cadena[i+1] == '(': #Si el siguiente caracter es la apertura de un parentesis, se agregara un termino
                    self.__cuenta.append([])
                    f += 1
                    self.__cuenta[f].append(aux)
                    numero = ""
                else:
                    self.__cuenta[f].append(aux)
                    numero = ""      
            elif cadena[i] not in "()": #Si no se ingreso a ninguna de las condiciones entonces se reconocera el caracter como el comienzo del nombre de una variable
                numero += cadena[i]
                variable = True
                           
        resul = self.realizarCuenta(self.__cuenta) #Se definira el resultado de la operacion llamando al metodo realizarCuenta
        return resul
    
    
    
    def realizarCuenta(self,cuenta):
        if len(cuenta) > 0:
            resultado = 0
            resultado2 = [[]]
            for i in range(len(cuenta)):                                
                for f in range(len(cuenta[i])):
                    if f == 0 and not cuenta[i][f].oper:
                        if cuenta[i][f].var:
                            if cuenta[i][f].variable in cosa.ejemplo.keys():
                                resultado = int(cosa.ejemplo[cuenta[i][f].variable])
                            else:
                                break
                        else:
                            resultado = int(cuenta[i][f].numero)
                    elif f == 0 and cuenta[i][f].oper:
                        resultado2[0].append(cuenta[i][f])                                      
                    elif cuenta[i][f].oper and f+1 != cuenta[i].__len__():
                        if cuenta[i][f].operador == "+":
                            if cuenta[i][f+1].var:
                                if cuenta[i][f+1].variable in cosa.ejemplo.keys():
                                    resultado += int(cosa.ejemplo[cuenta[i][f+1].variable])
                                else:
                                    break
                            else:
                                resultado += cuenta[i][f+1].numero
                        elif cuenta[i][f].operador == "-":
                            if cuenta[i][f+1].var:
                                if cuenta[i][f+1].variable in cosa.ejemplo.keys():
                                    resultado -= int(cosa.ejemplo[cuenta[i][f+1].variable])
                                else:
                                    break
                            else:                                
                                resultado -= cuenta[i][f+1].numero
                        elif cuenta[i][f].operador == "*":
                            if cuenta[i][f+1].var:
                                if cuenta[i][f+1].variable in cosa.ejemplo.keys():
                                    resultado *= int(cosa.ejemplo[cuenta[i][f].variable])
                                else:
                                    break
                            else:
                                resultado *= cuenta[i][f+1].numero
                        elif cuenta[i][f].operador == "/":
                            if cuenta[i][f+1].var:
                                if cuenta[i][f+1].variable in cosa.ejemplo.keys():
                                    resultado = int(resultado / cosa.ejemplo[cuenta[i][f+1].variable])
                                else:
                                    break
                            else:
                                resultado = int(resultado / cuenta[i][f+1].numero)
                        elif cuenta[i][f].operador == "^":
                            if cuenta[i][f+1].var:
                                if cuenta[i][f+1].variable in cosa.ejemplo.keys():
                                    resultado **= int(cosa.ejemplo[cuenta[i][f+1].variable])
                                else:
                                    break
                            else:
                                resultado **= cuenta[i][f+1].numero
                    elif cuenta[i][f].oper:
                        resultado2[0].append(cuenta[i][f])
                if not cuenta[i][f].oper:        
                    aux = Unidad(str(resultado))
                    resultado2[0].append(aux)
            if len(resultado2[0]) > 1:
                resultado = self.realizarCuenta(resultado2)                
            return resultado       
    
    @property
    def texto(self):
        return self.__texto + "= " + str(self.__resultado)
    @property
    def resultado(self):
        return self.__resultado
    
    
class cosa(object):
    
    ejemplo = {"hola":3,"como":4,"tas":5}
                
                