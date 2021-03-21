class Simbolo:

    def __init__(self, token, lexema, fila, columna):
        self.token=token
        self.lexema=lexema
        self.fila=fila
        self.columna=columna

class Atributo:

    def __init__(self, id, valor, cont, contdes):
        self.id=id
        self.valor=valor
        self.cont=cont
        self.contdes=contdes

class FacturaFinal:

    def __init__(self, Cantidad, Concepto, Precio, Total):
        self.cantidad = Cantidad
        self.concepto = Concepto
        self.precio = Precio
        self.total = Total