import tkinter
import ModeloPersona

class Table:
     
    def __init__(self,root,titulos,total_rows,total_columns,lst):
        #creacion de los titulos
        for i in range(len(titulos)):
            self.titulo=tkinter.Entry(root, width=20, fg='black',bg="grey",
                                font=('Arial',10,'bold'))
            self.titulo.place(x=0,y=0)
            self.titulo.grid(row=0, column=i)
            self.titulo.insert(tkinter.END, titulos[i])

        # Creacion de las celdas de los datos de persona
        for i in range(total_rows): 
            for j in range(total_columns):
                 
                self.e = tkinter.Entry(root, width=20, fg='black',
                               font=('Arial',10,'bold'))
                 
                self.e.grid(row=i+1, column=j)
                if j==0:
                    self.e.insert(tkinter.END, lst[i][0])
                elif j==1:
                    self.e.insert(tkinter.END, lst[i][1])
                elif j==2:
                    self.e.insert(tkinter.END, lst[i][2])
                elif j==3:
                    self.e.insert(tkinter.END, lst[i][3])
        