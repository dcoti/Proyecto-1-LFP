import EntradaArchivos
import AutomataOrden
import AnalizadorLexico
import AnalizadorLexicoOrden
import AutomataMenu
import Graphivs
from datetime import datetime
now = datetime.now()
valor=True

menu=""""
_________________________________________
|***********Proyecto #1 - LFP***********|
|***************************************|
|Daniel Enrique Coti Peñate             |
|***********Carnet: 201801146***********|
|*Lenguajes Formales y de Programación**|
|**************Seccion: B+**************|
|****Escuela de Ciencias y Sistemas*****|
----------------------------------------- 

1. Cargue el Menú
2. Cargar Orden
3. Generar Menú
4. Generar Factura
5. Generar Arbol
6. Salir 
"""
while (valor==True):
    print(str(now.day)+"/"+str(now.month)+"/"+str(now.year))
    print(menu)
    opcion = int(input("Ingrese su opcion\n"))
    if opcion==1:
        EntradaArchivos.menucargado=EntradaArchivos.cargarmenu()
        if EntradaArchivos.menucargado!="":
            EntradaArchivos.iterarMenu(EntradaArchivos.menucargado)
            Menu = EntradaArchivos.automatadelMenu()
            AutomataMenu.recorredor(Menu)
            AnalizadorLexico.imprimirtokensMenu()
            print("Se cargo el Menú\n")
            print("Se genero una tabla de Tokens \n")
    elif opcion==2:
        EntradaArchivos.ordencargado=EntradaArchivos.cargarorden()
        if EntradaArchivos.ordencargado!="":
            EntradaArchivos.iterarOrden(EntradaArchivos.ordencargado)
            Orden = EntradaArchivos.automatadelaFactura()
            AutomataOrden.recorredorOrden(Orden)
            AnalizadorLexicoOrden.imrpimirtokensOrden()
            print("Se Cargo la orden\n")
            print("Se genero una tabla de Tokens \n")
    elif opcion==3:
        if (EntradaArchivos.menucargado != "") & (EntradaArchivos.ordencargado != "") & (EntradaArchivos.menucargado!=[]) & (EntradaArchivos.ordencargado!=[]):
            EntradaArchivos.imprimirMenu()
        else:
            print("No se puede usar esta opcion debito a que falta cargar el menú o la orden")
    elif opcion==4:
        if (EntradaArchivos.menucargado != "") & (EntradaArchivos.ordencargado != "") & (EntradaArchivos.menucargado!=[]) & (EntradaArchivos.ordencargado!=[]):
            EntradaArchivos.imprimirOrden()
        else:
            print("No se puede usar esta opcion debito a que falta cargar el menú o la orden")
    elif opcion==5:
        if (EntradaArchivos.menucargado != "") & (EntradaArchivos.ordencargado != "") & (EntradaArchivos.menucargado!=[]) & (EntradaArchivos.ordencargado!=[]):
            AutomataMenu.generargrak()
            Graphivs.generarpdf()
            print("Se genero el arbol \n")
        else:
            print("No se puede usar esta opcion debito a que falta cargar el menú o la orden")
    elif opcion==6:
        valor=False
        print("Gracias por utilizar nuestro servicio")
    else:
        print("No se eligio una opcion correcta, elija una de las opciones que existen en el Menú")