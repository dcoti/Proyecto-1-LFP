import AutomataMenu
import AutomataOrden
from tablasim import FacturaFinal
import Factura

Menu = AutomataMenu.tablaatributos
Facturas = AutomataOrden.tablaatributosOrden
Total=0

def iterar():
    global Menu, Facturas, Total
    total=0
    for cantidad in Facturas:
        if cantidad.id=="Cantidad":
            print(cantidad.valor)
            for pedido in Facturas:
                if (pedido.id=="Pedido") & (cantidad.cont==pedido.cont):
                    print(pedido.valor)
                    for Desk in Menu:
                        if pedido.valor==Desk.id:
                            print(Desk.valor)
                            for Precio in Menu:
                                if (Precio.id=="Precio") & (Precio.cont==Desk.cont) & (Precio.contdes==Desk.contdes):
                                    print(Precio.valor)
                                    suma = float(Precio.valor)*int(cantidad.valor)
                                    AutomataOrden.Facturafinal.append(FacturaFinal(cantidad.valor, Desk.valor, Precio.valor, suma))
                                    Total=total=int(total)+float(suma)



def imp():
    Factura.generar(AutomataOrden.Facturafinal, Menu, Total, Facturas)


