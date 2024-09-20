#Para el modelo voy a aprovechar algun archivo de los ejercicios de clases 
#para ahorrar un poco de tiempo

#voy a basarme en el ejercicio de persona

import random
from tokenize import Number
import ModeloListaPersonas 

class Persona (object):
    
        #generaDNI(): genera numero aleatorio de 8 cifras
    #   genera la letra correspondiente.
    #   metodo privado se usa en los constructores 
    #   FORMULA DE LETRA DEL DNI:  
    #       calculas numDNI%23
    #       obtienes un numero entre el 0 y el 22
    #       ese num se compara a la siguiente tabla:
    #       0 -> T       1 -> R       2 -> W       3 -> A
    #       4 -> G       5 -> M       6 -> Y       7 -> F
    #       8 -> P       9 -> D       10 -> X      11 -> B
    #       12 -> N      13 -> J      14 -> Z      15 -> S
    #       16 -> Q      17 -> V      18 -> H      19 -> L
    #       20 -> C      21 -> K      22 -> E

    def generaDNI(self) -> str:
        res=""
        #esto es para sacr el numero del dni
        num = random.random()*((99999999-10000000+1)+10000000)
        num=num.__trunc__()
        
        #esto es para sacar la letra, yo iba a poner un "switch" pero pablo vino con esta idea
        listLetras=["T","G","P","N","Q","C","R","M","D","J","V","K","W","Y","X","Z","H","E","A","F","B","S","L"]
        posLetra=num%23
        letra=listLetras[posLetra]
       
        #ahora lo juntamos
        res=""+num.__str__()+letra

        #tenemos un problema, el nuevo dni puede ya existir
        #voy a utilizar recursividad porque lo veo mas facil que con un bucle
        if ModeloListaPersonas.ListaPersonas.dniExiste(res):
            res=Persona.generaDNI()
        
        #entregamos
        return res


    #CONSTRUCTORES
    #voy a utilizar este metodo para añadir personas
    def __init__(self, nombre, edad, sexo):
        #primero lo creamos vacio para que no de problemas
        self.nombre="Sin Nombre" #se nos ha pedido que esto esté vacio, pero me ahorro problemas así
        self.edad= -1
        self.dni="Sin DNI"
        self.sexo="M"
        #damos los parametros
        self.setNombre(nombre)
        self.setEdad(edad)
        self.dni=self.generaDNI()
        self.setSexo(sexo)

    
    #SETTERS
    #voy a utilizar estos metodos para modificar individualmente el/los 
    # parametro/s que el usuario elija modificar
    
    def setNombre(self, nombre:str):
        if len(nombre)>2 and len(nombre)<50:
            self.nombre=nombre
        
    def setEdad(self, edad : int):
        if  edad>0 and edad <150:
            self.edad= edad

    def setSexo(self, sexo : str):
        if sexo == "M" or sexo == "H":
            self.sexo=sexo
        else:
            self.sexo="M"

    #GETTERS
    def getDni(self)->str:
        return self.dni
    def getNombre(self)->str:
        return self.nombre
    def getEdad(self)->str:
        return self.edad
    def getSexo(self)->str:
        return self.sexo

    #toString(): devuelve toda la informacion del objeto.
    #voy a utilizar este metodo para listar cada objeto individualmente
    def toStringParaListaPersonas(self)-> str:
        return (self.dni+
                "\n"+self.nombre+
                "\n"+str(self.edad)+
                "\n"+self.sexo+"\n")