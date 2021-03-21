from tablasim import Simbolo
tablasimbolos=[]
tablaErrores=[]
fila=0
columna=0
flagExpressionId=False
flagExpressionCadena=False
flagExpressionNumero=False
flagExpressionDecimal=False
valor=""
Estado=0
cont=0
def Error(simbolo, expectativa, fila, columna):
    tablaErrores.append(Simbolo(simbolo, expectativa, fila, columna))

def esletra(c):
    j=ord(c)
    if (j>=65) & (j<=90) | (j>=97) & (j<=122):
        return True
    else:
        return False

def esnumero(c):
    return (ord(c)>=48) & (ord(c)<=57)

def ExpresionId(c):
    global valor, columna, fila, flagExpressionId
    if esletra(c) or esnumero(c) or ord(c)==95:
        valor+=c
        columna+=1
        return;
    elif ord(c)==32:
        columna+=1
        tablasimbolos.append(Simbolo("ID", valor, fila, (columna-1-len(valor))))
        valor=""
        flagExpressionId=False
    elif ord(c)==61:
        tablasimbolos.append(Simbolo("ID", valor, fila, (columna-len(valor))))
        columna+=1
        tablasimbolos.append(Simbolo("Simbolo_igual", "=", fila, (columna-2)))
        valor=""
        flagExpressionId=False
    elif ord(c)==59:
        tablasimbolos.append(Simbolo("ID",valor,fila, (columna-len(valor))))
        columna+=1
        tablasimbolos.append(Simbolo("punto_y_coma",";",fila,(columna-2)))
        valor=""
        flagExpressionId=False
    elif ord(c)==10:
        tablasimbolos.append(Simbolo("ID", valor, fila, (columna - len(valor))))
        fila+=1
        columna+=1
        valor=""
        flagExpressionId=False
    else:
        Error(c,"Error Lexico | expresion no valida, tiene un caracter no valido",fila,columna)

def ExpresionCadena(c):
    global valor, fila, columna, flagExpressionCadena

    if ord(c)==39:
        columna+=1
        tablasimbolos.append(Simbolo("Cadena", valor, fila, (columna-1-len(valor))))
        valor=""
        flagExpressionCadena=False
        return ;
    columna+=1
    valor+=c

def ExpresionDecimal(c, val):
    global valor, fila, columna, cont, flagExpressionDecimal
    conta=cont
    if esnumero(c) & (cont <= 2):
        val += c
        cont = cont + 1
        valor=val
        return
    elif (cont>0) & (cont<=2) & (ord(c)==32):
        columna+=1
        tablasimbolos.append(Simbolo("Numero", valor, fila, (columna - 1 - len(valor))))
        valor=""
        cont=0
        flagExpressionDecimal = False
    elif (cont>0) & (cont<=2) & (ord(c)==59):
        columna += 1
        tablasimbolos.append(Simbolo("Numero", valor, fila, (columna - 1 - len(valor))))
        columna+=1
        tablasimbolos.append(Simbolo("punto_y_coma",";",fila,(columna-2)))
        valor = ""
        flagExpressionDecimal=False
        cont = 0
    else:
        val += c
        Error(valor, "Se espera un numero con formato ##.##", fila, columna)
        flagExpressionDecimal=False
        cont = 0
        return

def ExpresionNumero(c):
    global valor, fila, columna, flagExpressionNumero, cont, flagExpressionDecimal

    if esnumero(c):
        columna+=1
        valor+=c
        return
    elif ord(c)==46:
        valor+=c
        flagExpressionDecimal=True
        flagExpressionNumero=False
        return
    elif ord(c)==59:
        columna+=1
        tablasimbolos.append(Simbolo("Numero", valor+".00", fila, (columna-1-len(valor))))
        columna+=1
        tablasimbolos.append(Simbolo("punto_y_coma",";",fila,(columna-2)))
        valor=""
        flagExpressionNumero=False
    elif ord(c)==32:
        columna+=1
        tablasimbolos.append(Simbolo("Numero", valor + ".00", fila, (columna - 1 - len(valor))))
        valor = ""
        flagExpressionNumero = False
    else:
        Error(c, "Error Lexico | caracter no valido", fila, columna)