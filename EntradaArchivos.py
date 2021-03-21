from tkinter import *
from tkinter.filedialog import askopenfilename
import AnalizadorLexico
import AutomataMenu
import AutomataOrden
import AnalizadorLexicoOrden
import operaciones
root = Tk()
root.withdraw()
root.update()
cont=0
menucargado = []
ordencargado = []

def generar(ruta):
    file = open(ruta)
    file = file.read()
    carga = list(file)
    return carga

def cargarmenu():
    ruta = askopenfilename(filetypes=[("Abrir Menú", "*.lfp")])
    if ruta=="":
        print("No se eligio ningun menu")
        return  ruta
    else:
        origen = generar(ruta)
        return origen


def cargarorden():
    global cont
    ruta = askopenfilename(filetypes=[("Abrir Orden", "*.lfp")])
    if ruta=="":
        print("No se eligio ninguna orden")
        return ruta
    else:
        cont+=1
        origen = generar(ruta)
        return origen
#itera la lista
def iterarMenu(lista):
    for c in lista:
        h = ord(c)
        AnalizadorLexico.analizador(c)

def imprimirMenu():
    if (AnalizadorLexico.ErroresMenu==[]) & (AnalizadorLexicoOrden.ErroresOrden==[]):
        AutomataMenu.imprimirAutomata()
        print("Se genero el Menú\n")
    else:
        if AnalizadorLexico.ErroresMenu!=[]:
            AnalizadorLexico.imprimirerroresMenu()
        else:
            print("Hay errores en la Orden")

def iterarOrden(lista):
    for c in lista:
        AnalizadorLexicoOrden.analizador(c)

def imprimirOrden():
    if (AnalizadorLexico.ErroresMenu==[]) and (AnalizadorLexicoOrden.ErroresOrden==[]):
        operaciones.iterar()
        operaciones.imp()
        print("Se genero la Factura\n")
    else:
        if AnalizadorLexicoOrden.ErroresOrden!=[]:
            AnalizadorLexicoOrden.imprimirerroresOrden()
        else:
            print("Hay errores en el Menú")

def automatadelMenu():
    return AnalizadorLexico.Menu

def automatadelaFactura():
    return AnalizadorLexicoOrden.Orden