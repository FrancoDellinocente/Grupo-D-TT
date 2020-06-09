class Unidad(object):    
     
    '''
    Representa una unidad dentro de una operacion, esta puede ser tanto un numero
    entero, como un operador tal como "/*-+^" o el nombre de una variable, booleanos indicaran
    cual de las tres variantes corresponde a la instancia de la clase.
    ''' 
     
    def __init__(self, i):
        '''
        El constructor recibe un string y confirma cual de las tres variantes de Unidad
        sera la instancia de la clase. Los nombres de variables deberan comenzar obligatoriamente
        con un caracter alfabetico, y luego del primer contener cualquier caracter numerico si se
        desea, de lo contrario resultara en un error.
        '''    
        self.__numero = 0
        self.__operador = ''
        self.__variable = ''    
        if i[0] in "+-*/()^" and str.__len__(i) < 2: 
            self.__oper = True
            self.__var = False
            self.__operador = str(i[0])        
        elif i[0] in "0123456789-":
            self.__oper = False
            self.__var = False
            self.__numero = int(i)
        else:
            self.__oper = False
            self.__var = True
            self.__variable = str(i)

    '''
    No se devolvera el valor de las variables que no corresponden a la variante de la instancia
    '''
    @property
    def oper(self):
        return self.__oper
    @property
    def operador(self):
        if self.__oper is True and self.__var is False:
            return self.__operador
    @property
    def numero(self):
        if self.__oper is False and self.__var is False:
            return self.__numero
    @property
    def var(self):
        return self.__var            
    @property
    def variable(self):
        if self.__var is True and self.__oper is False:
            return self.__variable
    
        
    

    