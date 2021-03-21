import Condiciones
from tablasim import Simbolo
import generarErrores
import TabladeTokens

def analizador(c):
    if Condiciones.flagExpressionId:
        Condiciones.ExpresionId(c)
    elif Condiciones.flagExpressionCadena:
        Condiciones.ExpresionCadena(c)
    elif Condiciones.flagExpressionNumero:
        Condiciones.ExpresionNumero(c)
    elif Condiciones.flagExpressionDecimal:
        Condiciones.ExpresionDecimal(c, Condiciones.valor)
    elif Condiciones.esletra(c)==True:
        Condiciones.columna+=1
        Condiciones.valor=c
        Condiciones.flagExpressionId=True
    elif Condiciones.esnumero(c)==True:
        Condiciones.columna+=1
        Condiciones.valor=c
        Condiciones.flagExpressionNumero=True
    elif ord(c)==61: #=
        Condiciones.columna+=1
        Condiciones.valor=c
        Condiciones.tablasimbolos.append(Simbolo("Simbolo_igual", "=", Condiciones.fila, (Condiciones.columna-2)))
        Condiciones.valor=c
    elif ord(c)==39: #'
        Condiciones.flagExpressionCadena=True
        Condiciones.columna+=1
    elif ord(c)==91: #[
        Condiciones.columna += 1
        Condiciones.valor = c
        Condiciones.tablasimbolos.append(Simbolo("simbolo_llave_abre", "[", Condiciones.fila, (Condiciones.columna-2)))
        Condiciones.valor=""
    elif ord(c)==93: #]
        Condiciones.columna += 1
        Condiciones.valor = c
        Condiciones.tablasimbolos.append(Simbolo("simbolo_llave_cierra", "]", Condiciones.fila, (Condiciones.columna-2)))
        Condiciones.valor = ""
    elif ord(c)==59: #;
        Condiciones.columna += 1
        Condiciones.valor = c
        Condiciones.tablasimbolos.append(Simbolo("punto_y_coma", ";", Condiciones.fila, (Condiciones.columna - 2)))
        Condiciones.valor = ""
    elif ord(c)==58: #:
        Condiciones.columna+=1
        Condiciones.valor=c
        Condiciones.tablasimbolos.append(Simbolo("Dos_puntos", ":", Condiciones.fila, (Condiciones.columna-2)))
        Condiciones.valor=""
    elif ord(c)==10: #Salto de Linea
        Condiciones.fila+=1
        Condiciones.columna=0
        Condiciones.valor=""
    elif ord(c)==32: #espacio
        Condiciones.columna+=1
        Condiciones.valor=""
    else:
        Condiciones.Error(c,"",Condiciones.fila, Condiciones.columna)

def imprimir():
    for s in Condiciones.tablasimbolos:
        print(s.token+"->"+s.lexema+"->"+str(s.fila)+"->"+str(s.columna))

ErroresMenu=Condiciones.tablaErrores
Menu=Condiciones.tablasimbolos

def imprimirerroresMenu():
    generarErrores.generar(Condiciones.tablaErrores, "--Menu--")

def imprimirtokensMenu():
    TabladeTokens.generar(Condiciones.tablasimbolos, "Menu")