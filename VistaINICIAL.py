
import tkinter
import VistaTabla
import ControladorModelo

#FUNCION PARA PRINTEAR LA TABLA
def printTabla(ventana,titulos,lst):
    bloqueTablaInfo=tkinter.PanedWindow(ventana,border=10,bd=20)
    bloqueTablaInfo.pack(side='top',expand=True)
    bloqueTablaInfo.place(x=0, y=0)
    
    # pasamos el numero de filas y columnas
    total_rows = len(lst)
    total_columns = 0
    if len(lst)>0:
        total_columns =4
    VistaTabla.Table(bloqueTablaInfo,titulos,total_rows,total_columns,lst)

#FUNCIONES DE LOS BOTONES

def accionBotonAniadir(nombrep:str,edadp:str,sexop:str,
    ventana,titulos):
    edad=0

    #le quitamos el salto de linea a todo
    nombredef=nombrep.split()
    if len(nombredef)>0:
        nombredef=nombredef[0]
    else:
        nombredef=""
    edadString=edadp.split()
    if len(edadString)>0:
        edadString=edadString[0]
    else:
        edadString="0"
    sexodef=sexop.split()
    if len(sexodef)>0:
        sexodef=sexodef[0]
    else:
        sexodef=""

    #parseamos el tipo de dato
    if edadString.isdigit():
        edad=int(edadString)
    
    #llamamos a la funcion corresondiente
    ControladorModelo.aniadirALaLista(nombredef,edad,sexodef)

    #volvemos a obtener la lista de personas actualizada
    lst= ControladorModelo.obtenerListaPersonas()
    #volvemos a printear la tabla
    printTabla(ventana,titulos,lst)

def accionBotonBorrar(dnip:str,
        ventana,titulos):
    #le quitamos el salto de linea a todo
    dniDef=dnip.split()
    if len(dniDef)>0:
        dniDef=dniDef[0]
    else:
        dniDef=""
    #llamamos a la funcion corresondiente
    ControladorModelo.borrarDeLaLista(dniDef)

    #volvemos a obtener la lista de personas actualizada
    lst= ControladorModelo.obtenerListaPersonas()
    #volvemos a printear la tabla
    printTabla(ventana,titulos,lst)

def accionBotonModificar(dnip:str,nombrep:str,edadp:str,sexop:str,
        ventana,titulos):
    edad=0

    #le quitamos el salto de linea a todo
    dniDef=dnip.split()
    if len(dniDef)>0:
        dniDef=dniDef[0]
    else:
        dniDef=""
    nombredef=nombrep.split()
    if len(nombredef)>0:
        nombredef=nombredef[0]
    else:
        nombredef=""
    edadString=edadp.split()
    if len(edadString)>0:
        edadString=edadString[0]
    else:
        edadString="0"
    sexodef=sexop.split()
    if len(sexodef)>0:
        sexodef=sexodef[0]
    else:
        sexodef=""

    #parseamos el tipo de dato
    if edadString.isdigit():
        edad=int(edadString)
    
    #llamamos a la funcion corresondiente
    ControladorModelo.modificarPersona(dniDef,nombredef,edad,sexodef)
    
    #volvemos a obtener la lista de personas actualizada
    lst= ControladorModelo.obtenerListaPersonas()
    #volvemos a printear la tabla
    printTabla(ventana,titulos,lst)

#Creamos la ventana principal
ventana=tkinter.Tk()

#diseñamos la ventana principal
ventana.geometry("950x600")
ventana.title("Ventana Inicial")

#diseñamos los bloques de contenido
bloqueAniadir=tkinter.PanedWindow(ventana,border=10,width=600,height=120)
bloqueAniadir.pack(side='top',expand=True)
bloqueAniadir.place(x=600, y=0)

bloqueBorrar=tkinter.PanedWindow(ventana,border=10,width=600,height=100)
bloqueBorrar.pack(side='top',expand=True)
bloqueBorrar.place(x=600, y=150)

bloqueModificar=tkinter.PanedWindow(ventana,border=10,width=600,height=200)
bloqueModificar.pack(side='top',expand=True)
bloqueModificar.place(x=600, y=240)

#diseñamos el contenido de la tabla

#pasamos la lista de los titulos de la tabla
titulos=["DNI","NOMBRE","EDAD","SEXO"]

#pasamos la informacion de ListaPersonas
lst = ControladorModelo.obtenerListaPersonas()

#creamos la tabla: utilizamos la clase tabla
printTabla(ventana,titulos,lst)


#diseñamos el contenido del bloqueAñadir
etiquetaAniadir=tkinter.Label(bloqueAniadir, text= "AÑADIR PERSONA",background="grey")
etiquetaAniadir.pack(side='top',expand=1)
etiquetaAniadir.place(x=20,y=0)

etiquetaNombre=tkinter.Label(bloqueAniadir, text= "Nombre: ")
etiquetaNombre.pack(side='top')
etiquetaNombre.place(x=20,y=30)

casillaAniadirNombre=tkinter.Text(bloqueAniadir,width=20,height=1)
casillaAniadirNombre.pack(side='top')
casillaAniadirNombre.place(x=100,y=30)

etiquetaEdad=tkinter.Label(bloqueAniadir, text= "Edad: ")
etiquetaEdad.pack(side='top')
etiquetaEdad.place(x=20,y=60)

casillaAniadirEdad=tkinter.Text(bloqueAniadir,width=20,height=1)
casillaAniadirEdad.pack(side='top')
casillaAniadirEdad.place(x=100,y=60)

etiquetaSexo=tkinter.Label(bloqueAniadir, text= "Sexo: ")
etiquetaSexo.pack(side='top')
etiquetaSexo.place(x=20,y=90)

casillaAniadirSexo=tkinter.Text(bloqueAniadir,width=20,height=1)
casillaAniadirSexo.pack(side='top')
casillaAniadirSexo.place(x=100,y=90)

#BOTON PARA AÑADIR
botonAniadir=tkinter.Button(bloqueAniadir, text= "Añadir", 
    command=lambda: accionBotonAniadir(casillaAniadirNombre.get(1.0,"end"),
        casillaAniadirEdad.get(1.0,"end"),casillaAniadirSexo.get(1.0,"end"),
        ventana,titulos))
botonAniadir.pack(side='top')
botonAniadir.place(x=270,y=90)

#diseñamos el contenido del bloqueBorrar
etiquetaBorrar=tkinter.Label(bloqueBorrar, text= "BORRAR PERSONA",background="grey")
etiquetaBorrar.pack(side='left')
etiquetaBorrar.place(x=20,y=0)

etiquetaDNI=tkinter.Label(bloqueBorrar, text= "DNI: ")
etiquetaDNI.pack(side='left')
etiquetaDNI.place(x=20,y=30)

casillaBorrar=tkinter.Text(bloqueBorrar,width=20,height=1)
casillaBorrar.pack(side='right')
casillaBorrar.place(x=100,y=30)

#BOTON BORRAR
botonBorrar=tkinter.Button(bloqueBorrar, text= "Borrar",
    command=lambda: accionBotonBorrar(casillaBorrar.get(1.0,"end"),
        ventana,titulos))
botonBorrar.pack(side='top')
botonBorrar.place(x=270,y=30)

#diseñamos el contenido del bloqueModificar
etiquetaModificar=tkinter.Label(bloqueModificar, text= "MODIFICAR PERSONA",background="grey")
etiquetaModificar.pack(side='top')
etiquetaModificar.place(x=20,y=0)

etiquetaDNI=tkinter.Label(bloqueModificar, text= "DNI: ")
etiquetaDNI.pack(side='top')
etiquetaDNI.place(x=20,y=30)

casillaModificarDNI=tkinter.Text(bloqueModificar,width=20,height=1)
casillaModificarDNI.pack(side='top')
casillaModificarDNI.place(x=100,y=30)

etiquetaNombre=tkinter.Label(bloqueModificar, text= "Nombre: ")
etiquetaNombre.pack(side='top')
etiquetaNombre.place(x=20,y=60)

casillaModificarNombre=tkinter.Text(bloqueModificar,width=20,height=1)
casillaModificarNombre.pack(side='top')
casillaModificarNombre.place(x=100,y=60)

etiquetaEdad=tkinter.Label(bloqueModificar, text= "Edad: ")
etiquetaEdad.pack(side='top')
etiquetaEdad.place(x=20,y=90)

casillaModificarEdad=tkinter.Text(bloqueModificar,width=20,height=1)
casillaModificarEdad.pack(side='top')
casillaModificarEdad.place(x=100,y=90)

etiquetaSexo=tkinter.Label(bloqueModificar, text= "Sexo: ")
etiquetaSexo.pack(side='top')
etiquetaSexo.place(x=20,y=120)

casillaModificarSexo=tkinter.Text(bloqueModificar,width=20,height=1)
casillaModificarSexo.pack(side='top')
casillaModificarSexo.place(x=100,y=120)

#BOTON MODIFICAR
botonModificar=tkinter.Button(bloqueModificar, text= "Modificar",
    command= lambda: accionBotonModificar(casillaModificarDNI.get(1.0,"end"),
        casillaModificarNombre.get(1.0,"end"),casillaModificarEdad.get(1.0,"end"),
        casillaModificarSexo.get(1.0,"end"),
        ventana,titulos))
botonModificar.pack(side='top')
botonModificar.place(x=270,y=120)

ventana.mainloop()
