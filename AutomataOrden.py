from tablasim import Atributo
import CondicionesOrden

tablaatributosOrden=[]
flagautomataorden=False
Contador=0
Conaux=0
Estado=0
temp=None
Facturafinal=[]

def automataOrden(s):
    global tablaatributosOrden, flagautomataorden, Contador, Conaux, Estado, temp
    if Estado == 1:
        if s.token=="coma":
            Estado=2
        else:
            Estado = -1
            CondicionesOrden.Error(s.lexema, "Se esperaba una , ",s.fila, s.columna)
            flagautomataorden=False
    elif Estado==2:
        if s.token=="Cadena":
            Estado=3
            tablaatributosOrden.append(Atributo("NIT", s.lexema, 0, 0))
        elif s.token=="ID": #Estado de Aceptación
            tablaatributosOrden.append((Atributo("Pedido", s.lexema, Contador, 0)))
            flagautomataorden=False
        else:
            Estado=-1
            CondicionesOrden.Error(s.lexema, "Se esperaba una , ", s.fila, s.columna)
            flagautomataorden = False
    elif Estado==3:
        if s.token=="coma":
            Estado=4
        else:
            Estado = -1
            CondicionesOrden.Error(s.lexema, "Se esperaba una , ", s.fila, s.columna)
            flagautomataorden = False
    elif Estado==4:
        if s.token=="Cadena":
            Estado=3
            tablaatributosOrden.append(Atributo("ciudad", s.lexema, 0, 0))
        elif s.token=="Propina": #estado de Aceptacion
            tablaatributosOrden.append((Atributo("propina", str(float(s.lexema)/100), 0,0)))
            flagautomataorden=False
        else:
            Estado = -1
            CondicionesOrden.Error(s.lexema, "Se esperaba una , ", s.fila, s.columna)
            flagautomataorden = False

def recorredorOrden(tablasimbolos):
    global tablaatributosOrden, flagautomataorden, Contador, Conaux, Estado, temp
    for s in tablasimbolos:
        if flagautomataorden:
            automataOrden(s)
        elif s.token=="Cadena":
            Estado=1
            tablaatributosOrden.append(Atributo("Cliente", s.lexema, 0, 0))
            flagautomataorden=True
        elif s.token=="Numero":
            Contador+=1
            flagautomataorden=True
            tablaatributosOrden.append(Atributo("Cantidad", s.lexema, Contador,0))
            Estado=1
        else:
            CondicionesOrden.Error(s.lexema, "Error Sintactico | se esperaba un cliente o una contidad", s.fila, s.columna)

def imprimirOrden():
    for im in tablaatributosOrden:
        print(im.id+"_"+im.valor)