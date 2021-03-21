from tablasim import Simbolo
tablasOrden=[]
tablaErroresOrden=[]
tablaatributos=[]
fila=0
columna=0
flagExpressionId=False
flagExpressionCadena=False
flagExpressionNumero=False
valor=""
Estado=0

def Error(simbolo, expectativa, fila, columna):
    tablaErroresOrden.append(Simbolo(simbolo, expectativa, fila, columna))

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
    if esletra(c) or esnumero(c) or ord(c)==95 or ord(c)==45:
        valor+=c
        columna+=1
        return;
    elif ord(c)==32:
        valor+=c
        columna+=1
        tablasOrden.append(Simbolo("ID", valor, fila, (columna-1-len(valor))))
        valor=""
        flagExpressionId=False
    elif ord(c)==10:
        tablasOrden.append(Simbolo("ID", valor, fila, (columna - len(valor))))
        fila+=1
        columna+=1
        valor=""
        flagExpressionId=False
    else:
        Error(c,"",fila,columna)

def ExpresionCadena(c):
    global valor, fila, columna, flagExpressionCadena

    if ord(c)==39:
        columna+=1
        tablasOrden.append(Simbolo("Cadena", valor, fila, (columna-1-len(valor))))
        valor=""
        flagExpressionCadena=False
        return ;
    columna+=1
    valor+=c

def ExpresionNumero(c):
    global valor, fila, columna, flagExpressionNumero
    h=ord(c)
    if esnumero(c) | (ord(c)==46):
        columna+=1
        valor+=c
        return
    if ord(c)==44:
        columna+=1
        tablasOrden.append(Simbolo("Numero", valor, fila, (columna-1-len(valor))))
        columna+=1
        tablasOrden.append(Simbolo("coma", ",", fila, (columna-2)))
        valor=""
        flagExpressionNumero=False
    elif ord(c)==10:
        columna += 1
        tablasOrden.append(Simbolo("Numero", valor, fila, (columna - 1 - len(valor))))
        valor = ""
        flagExpressionNumero = False
    elif ord(c)==32:
        columna += 1
        tablasOrden.append(Simbolo("Numero", valor, fila, (columna - 1 - len(valor))))
        valor = ""
        flagExpressionNumero = False
    elif ord(c)==37:
        columna+=1
        tablasOrden.append(Simbolo("Propina", valor, fila, (columna-1-len(valor))))
        valor=""
        flagExpressionNumero=False
    else:
        Error(c, "", fila, columna)