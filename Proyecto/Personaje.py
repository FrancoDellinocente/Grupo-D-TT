import sqlite3
def sql_connection():

    try:

        con = sqlite3.connect('persoajese.db')

        return con

    except Error:

        print(Error)

def sql_creaTabla(con):

    cursorPer = con.cursor()

    cursorPer.execute("CREATE TABLE perso(id integer PRIMARY KEY, name text)")#tambien la asociacion con la tabla plantilla

    con.commit()

con = sql_connection()
sql_creaTabla(con)

pos=1

while True: #while true para que se repita hasta que el usuario desee salir de personaje
    while True: # while true para que solo ponga numeros que deseeamos
        print("ingrese el numero de lo que desea hacer: \n"
              "1. crear un personaje\n"
              "2. editar un personaje\n"
              "3. elimina un personaje\n"
              "4. salir de edicion de hoja de personaje \n")
        num = int(input())
        if num == 1 or num == 2 or num == 3 or num == 4:
            break
    if num == 1:
        '''
        print("ingrese que plantilla usara para crear su personaje")
        #aca podemos hacer que muestre las plantillas y que ingrese el id de la que quiera
        n= int(input())
        '''
        print("ingrese nombre del nuevo personaje: ")
        nom = input()
        cursorPer.execute("INSERT INTO perso VALUES(pos, nom)")#aca se vincularia
        con.commit()
        '''
        for i in range(#nose como se obtiene el size de una base de datos):
	        print ("ingrese valor para el siguiente atributo: " #aca se deberia poner el nombre del atributo, nose como se hace eso en bd)
	        aux = input()
	        cursorPer.execute('UPDATE perso SET name = aux where id = i')
        '''
        pos+1
    elif num == 2:
        '''
        print("ingrese nombre del personaje: ")
        cursorObj.execute('SELECT * FROM perso')
        rows = cursorObj.fetchall()
        for row in rows:
            print(row)
        #eso mostraria todos los dates de la tabla perso
        aux = input()
        cursorPer.execute('SELECT aux FROM perso')
        '''
        print("ingrese el numero del atributo que desea cambiar: ")
        # aca deberiamos mostrar los nombres de los atributos con su numero de columna
        aux = input()
        '''
        aca deberiamos encontrar una forma que dado el numero de columna seleccione la misma, nose como se hace eso,
        solo haye el ejemplo de abajo para poder llegar a selccionar una sola tabla
        #select column1 from tables_name
        '''
        print("ingrese el valor del atributo recuerde que al mismo se le sumara el valor base del arquetipo")
        val = input()
        '''
        aca creeria que deberia acceder a la tabla de plantilla  para buscar el nombre del atributo cambiado que se remplasaria por name del ejemplo
        de abajo y el 1 deberia ser el id de la plantilla creo
        ejemplo:
            cursorPer.execute('UPDATE perso SET name = val where id = 1')
        '''
    elif num == 3:
        print("escriba el id de la personaje que desea eliminar: ")
        cursorObj.execute('SELECT * FROM perso')
        rows = cursorObj.fetchall()
        for row in rows:
            print(row)
        #eso mostraria todos los dates de la tabla perso
        aux = input()
        cursorPer.execute('DELETE id==aux FROM perso')
        #creeria que ahi borraria la fila

    elif num == 4:
        print("finalizo la carga de atributos")
        exit()
