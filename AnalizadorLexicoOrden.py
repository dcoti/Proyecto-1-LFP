import CondicionesOrden
from tablasim import Simbolo
import generarErrores
import TabladeTokens

def analizador(c):
    if CondicionesOrden.flagExpressionId:
        CondicionesOrden.ExpresionId(c)
    elif CondicionesOrden.flagExpressionCadena:
        CondicionesOrden.ExpresionCadena(c)
    elif CondicionesOrden.flagExpressionNumero:
        CondicionesOrden.ExpresionNumero(c)
    elif CondicionesOrden.esletra(c)==True:
        CondicionesOrden.columna+=1
        CondicionesOrden.valor=c
        CondicionesOrden.flagExpressionId=True
    elif CondicionesOrden.esnumero(c)==True:
        CondicionesOrden.columna+=1
        CondicionesOrden.valor=c
        CondicionesOrden.flagExpressionNumero=True
    elif ord(c)==39: #'
        CondicionesOrden.flagExpressionCadena=True
        CondicionesOrden.columna+=1
    elif ord(c)==44: #,
        CondicionesOrden.columna += 1
        CondicionesOrden.valor=c
        CondicionesOrden.tablasOrden.append(Simbolo("coma", ",",CondicionesOrden.fila, (CondicionesOrden.columna-2)))
        CondicionesOrden.valor = ""
    elif ord(c)==10: #Salto de Linea
        CondicionesOrden.fila+=1
        CondicionesOrden.columna=0
        CondicionesOrden.valor=""
    elif ord(c)==32: #espacio
        CondicionesOrden.columna+=1
        CondicionesOrden.valor=""
    else:
        CondicionesOrden.Error(c,"",CondicionesOrden.fila, CondicionesOrden.columna)

def imprimir():
    for s in CondicionesOrden.tablasOrden:
        print(s.token+"->"+s.lexema+"->"+str(s.fila)+"->"+str(s.columna))

ErroresOrden=CondicionesOrden.tablaErroresOrden
Orden = CondicionesOrden.tablasOrden

def imprimirerroresOrden():
    generarErrores.generar(CondicionesOrden.tablaErroresOrden, "--Factura--")

def imrpimirtokensOrden():
    TabladeTokens.generar(CondicionesOrden.tablasOrden, "Orden")