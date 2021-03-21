from tablasim import Atributo
import Menu
import  Condiciones
import Graphivs
tablaatributos=[]
flagAutomataMenu=False
contador=0
contaux=0
Estado=0
temp=None

def automataMenu(s):
    global tablaatributos, flagAutomataMenu, Estado, temp, contador, contaux
    if Estado==1:
        if s.token=="Simbolo_igual":
            Estado=2
        elif s.token=="ID":
            contaux+=1
            temp = Atributo(s.lexema,"", 0, contaux)
            Estado=5
        else:
            Estado=-1
            flagAutomataMenu=False
            Condiciones.Error(s.lexema, "Error sintactico, se esperaba un =", s.fila, s.columna)
    elif Estado==2: #Estado de aceptación
        if s.token=="Cadena":
            temp.valor=s.lexema
            tablaatributos.append(temp)
            temp=None
            flagAutomataMenu=False
        else:
            Estado=-1
            flagAutomataMenu=False
            Condiciones.Error(s.lexema, "Se esperaba el nombre del Restaurante", s.fila, s.columna)
    elif Estado==3: #Estado de aceptación
        if s.token=="Dos_puntos":
            flagAutomataMenu=False
        else:
            Estado=-1
            flagAutomataMenu=False
            Condiciones.Error(s.lexema, "Error sintactico | Se esperaba :", s.fila, s.columna)
    elif Estado==4:
        if s.token=="ID":
            temp=Atributo(s.lexema,"")
            Estado=1
        else:
            Estado = -1
            flagAutomataMenu = False
            Condiciones.Error(s.lexema, "Error sintactico | Se esperaba un ID", s.fila, s.columna)
    elif Estado==5:
        if s.token=="punto_y_coma":
            Estado=6
        else:
            Estado = -1
            flagAutomataMenu = False
            Condiciones.Error(s.lexema, "Error sintactico | Se esperaba ;", s.fila, s.columna)
    elif Estado==6:
        if s.token=="Numero":
            temp=Atributo("Precio", s.lexema, contador, contaux)
            tablaatributos.append(temp)
            temp=None
            Estado=5
        elif s.token=="Cadena":
            if temp!=None:
                temp.valor=s.lexema
                temp.cont=contador
                tablaatributos.append(temp)
                temp=None
                Estado=5
            else:
                temp=Atributo("Descripcion", s.lexema, contador, contaux)
                tablaatributos.append(temp)
                temp=None
                Estado=7
        else:
            Estado = -1
            flagAutomataMenu = False
            Condiciones.Error(s.lexema, "Error sintactico | Se esperaba una cadena", s.fila, s.columna)
    elif Estado==7:
        if s.token=="simbolo_llave_cierra": #Estado de aceptación
            flagAutomataMenu=False
        else:
            Estado = -1
            flagAutomataMenu = False
            Condiciones.Error(s.lexema, "Error sintactico | Se esperaba una ]", s.fila, s.columna)

def recorredor(tablasimbolos):
    global flagAutomataMenu, temp, Estado, tablaatributos, contador, contaux
    for s in tablasimbolos:
        if flagAutomataMenu:
            automataMenu(s)
        elif s.token=="ID":
            temp = Atributo(s.lexema, "", 0, 0)
            Estado=1
            flagAutomataMenu=True
        elif s.token=="Cadena":
            contador+=1
            contaux=0
            temp = Atributo("Comida", s.lexema, contador,0)
            tablaatributos.append(temp)
            temp=None
            Estado=3
            flagAutomataMenu = True
        elif s.token=="simbolo_llave_abre":
            Estado=1
            flagAutomataMenu = True
        else:
            Condiciones.Error(s.lexema, "Error sintactico | se esperaba un ID, cadena o [", s.fila, s.columna)

def imprimirAutomata():
        Menu.Menus(tablaatributos)

def generargrak():
    Graphivs.generargrafo(tablaatributos)