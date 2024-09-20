import ModeloListaPersonas
import ModeloPersona

def obtenerListaPersonas()->list:
    return ModeloListaPersonas.ListaPersonas.listar()
def aniadirALaLista(nombre,edad,sexo)->None:
    persona=ModeloPersona.Persona(nombre,edad,sexo)
    ModeloListaPersonas.ListaPersonas.aniadir(persona)
    
def borrarDeLaLista(dni)->None:
    ModeloListaPersonas.ListaPersonas.borrar(dni)

def modificarPersona(dni,nombre,edad,sexo)->None:
    ModeloListaPersonas.ListaPersonas.modificar(dni,nombre,edad,sexo)