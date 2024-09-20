#Hacer una aplicación, que mantenga una lista de objetos(tema libre), es decir, como mínimo ={
#   Listar,
#       voy a listar todas las personas, como un Select * from ListaPersonas
#       la lista va a ser literalmente una lista de personas []
#       voy a llamar a esta funcion en la vista para printear estos datos 
#       en una tabla justo cuando la aplicacion empieza a funcionar
#   Añadir,
#   Borrar, 
#   Modificar}
# Los datos se guardarán en un fichero para poder recuperarlos.
# La aplicación utilizará una interfaces gráfica (tkinter u otra)
import VistaINICIAL

def llamarAPrintTabla(ventana,titulos,total_rows,total_columns,lst):
    VistaINICIAL.printTabla(ventana,titulos,total_rows,total_columns,lst)