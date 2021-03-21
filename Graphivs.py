import os
from fpdf import FPDF

def generargrafo(Menu):
    contador=0
    file = open("arbol.dot", "w")
    file.write("digraph G {\n")
    for imp in Menu:
        if (imp.id=="restaurante") | (imp.id=="Restaurantes"):
            file.write(imp.id+"[label=\""+imp.valor+"\"]")
            for com in Menu:
                if (com.id=="Comida"):
                    contador+=1
                    id = "comida"+str(contador)
                    file.write(id+"[label=\""+com.valor+"\"]")
                    file.write(imp.id+"->"+id+"\n")
                    for comida in Menu:
                        if (comida.cont==com.cont) & (comida.id!="Comida") & (comida.id!="Precio") & (comida.id!="Descripcion"):
                            for precio in Menu:
                                if (precio.cont==comida.cont) & (precio.contdes==comida.contdes) & (precio.id=="Precio"):
                                    for descripcion in Menu:
                                        if (descripcion.cont==comida.cont) & (descripcion.contdes==comida.contdes) & (descripcion.id=="Descripcion"):
                                            file.write(comida.id+"[label=\""+comida.valor+", Q."+precio.valor+", "+descripcion.valor+"\"]\n")
                                            file.write(id + "->" + comida.id + "\n")
    file.write("}")
    file.close()
    os.system('dot -Tpdf arbol.dot -o arbol.pdf')


class PDF(FPDF):

    def logo(self, name, x, y, w, h):
        self.image(name, x, y, w, h)

pdf = PDF(orientation='L', unit='mm', format='Letter')

def generarpdf():
    pdf.add_page()
    pdf.logo('arbol.png', 5, 10, 270, 150)
    pdf.output('Menu.pdf', 'F')