# a través de esta clase accederemos al fichero
# mis datos se van a almacenar en un fichero de texto normal
#los datos en el fichero de texto van a tener esta estructura
#   DNI
#   nombre
#   edad
#   sexo
#por ejemplo:
#   99999999X
#   Veronica
#   19
#   M
import ModeloPersona

def abrirFichero(fichero,modo):
    try:
        file = open(fichero, modo)
        return file
    except OSError as err:
        print("Error: {0}".format(err))
    return

class ListaPersonas (object):
    #variables de clase
    fichero="DatosGuardados.txt"

    #no voy a hacer ningún constructor porque todas las funciones y 
    # las variables van a ser de clase y no de instancia

    #funcion auxiliar para abrir fichero
    #siempre vamos a utilizar el mismo fichero desde diferentes modos
    def file_manipulation( mode):
        try:
            file = open("DatosGuardados.txt", mode)
            return file
        except OSError as err:
            return -1
        return
    
    #funcion para listar
    def listar()->list:
        lista=[]
        fr=abrirFichero(ListaPersonas.fichero,"r")
        lineF = fr.readlines()
        cont=0
        dni=""
        nombre=""
        edad=0
        sexo="M"
        for line in lineF:
            if line != "\n":
                if cont % 4 == 0:
                    dni=line
                elif cont % 4 == 1:
                    nombre=line
                elif cont % 4 == 2:
                    edad=line
                elif cont % 4 == 3:
                    sexo=line
                    pers=[dni,nombre,edad,sexo]
                    lista.append(pers)
            cont=cont+1
        fr.close()
        return lista

    #funcion para añadir al fichero
    def aniadir(persona):
        fw=abrirFichero(ListaPersonas.fichero,"a")
        fw.write(persona.toStringParaListaPersonas())
        fw.close()

    #funcion para borrar del fichero
    def borrar(dni)->None:
        todasLasLineas=[]
        lineasParaEscribir=[]
        encontrado=False
        posDNI=-1
        
        #leemos las lineas y seleccionamos lo que vamos a reescribir
        fr=abrirFichero(ListaPersonas.fichero,"r")
        todasLasLineas=fr.readlines()
        for i in range (len(todasLasLineas)):
            todasLasLineas[i]=todasLasLineas[i].split("\n")[0]
            if dni==todasLasLineas[i]:
                encontrado=True
                posDNI=i
            if (encontrado and 
                (posDNI==i  or (posDNI+1)==i or (posDNI+2)==i or (posDNI+3)==i)):
                pass
            else:
                if len(todasLasLineas[i])>0:
                    lineasParaEscribir.append(todasLasLineas[i])
                else:
                    lineasParaEscribir.append("")
        fr.close()

        #borramos el fichero
        borrador=abrirFichero(ListaPersonas.fichero,"w")
        borrador.write("")
        borrador.close()
        
        fw=abrirFichero(ListaPersonas.fichero,"a")
        for i in range (len(lineasParaEscribir)):
            fw.write(lineasParaEscribir[i]+"\n")
        
        fw.close()

    #funcion para modificar una persona en el fichero
    def modificar(dni,nuevoNombre,nuevaEdad,nuevoSexo)->None:
        ListaPersonas.borrar(dni)
        personita=ModeloPersona.Persona(nuevoNombre,nuevaEdad,nuevoSexo)

        fw=abrirFichero(ListaPersonas.fichero,"a")
        fw.write(dni+"\n"
                +personita.getNombre()+"\n"
                +str(personita.getEdad())+"\n"
                +personita.getSexo()+"\n")
        fw.close()

    def obtenerTodosLosDNIS()->list:
        lista=ListaPersonas.listar()
        listaDNI=[]
        for i in range(len(lista)):
            listaDNI.append(lista[i][0])
        return listaDNI

    #Funcion para comprobar que ningun dni creado se repite con los anteriores dnis creados
    def dniExiste(dni) -> bool:
        res = False
        ListaDNIS=ListaPersonas.obtenerTodosLosDNIS()
        #si no hay dnis, no hay que comprobar si se repite
        if len(ListaDNIS) !=0:
            #recorremos la lista de dnis
            for i in range (0,len(ListaDNIS),+1):
                #si la posicion a comprobar es igual a la longitud, se va a salir de los limites
                if i==len(ListaDNIS):
                    break 
                else:
                    if dni == ListaDNIS[i]:
                        res=True
        return res