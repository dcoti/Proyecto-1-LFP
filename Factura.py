import os
from datetime import datetime
now = datetime.now()
porcentaje=0
fecha = str(now.day)+"/"+str(now.month)+"/"+str(now.year)
parte1="""
<html>
    <head>
        <title>Factura</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
        <link href="attrib.css" rel="stylesheet">
    </head>
    <body>
            <!-- Image and text -->
            <nav class="navbar navbar-light" style="background-color: Gray;">
                        <div class="container-fluid">
                        <a class="navbar-brand" href="#">
                         
"""
parte2="""
</a>
                        </div>
            </nav>
            <br>
            <center>
                <h3>
                    <small class="text-muted">Factura No. 01</small><br>
"""
parte3="""
</h3>
            </center> 
            <div id="Datos">
            <p class="Data">Datos del Cliente:</p>
"""
parte4="""
</div>   
            <br><p class="Des">Descripción</p>
            <center>
                <table id="tabla">
                    <thead>
                        <th><center>Cantidad</center></th>
                        <th><center>Articulo</center></ht>
                        <th><center>Precio</center></th>
                        <th><center>Total</center></th>
                    </thead>
                    <tbody>
"""
parte5="""
<tr>
    <td colspan="3" style="background-color: #cdcdcd;">Subtotal</td>
"""
parte6="""
</tr>
                    </tbody>
                </table>
            </center>
    </body>
</html>
"""



def generar(articulos, menu, total, datosgenerales):
    global porcentaje
    arti = articulos
    file = open("Factura.html","w")
    file.write(parte1)
    for s in menu:
        if s.id=="restaurante":
            file.write("<h4>Restaurante \""+s.valor+"\"</h4>")
    file.write(parte2)
    file.write("<small class=\"text-muted\">Fecha: "+fecha+"</small>")
    file.write(parte3)
    for nombre in datosgenerales:
        if nombre.id=="Cliente":
            file.write("<p class=\"Data\">Nombre: "+nombre.valor+"</p>")
    for NIT in datosgenerales:
        if NIT.id=="NIT":
            file.write("<p class=\"Data\">Nit: "+NIT.valor+"</p>")
    for Dic in datosgenerales:
        if Dic.id=="ciudad":
            file.write("<p class=\"Data\">Direccion: "+Dic.valor+"</p>")
    file.write(parte4)
    for art in articulos:
        file.write("<tr><td>"+str(art.cantidad)+"</td><td>"+art.concepto+"</td><td> Q."+str(art.precio)+"0</td><td> Q."+str(art.total)+"</td></tr>")
    file.write(parte5)
    file.write("<td style=\"background-color: #cdcdcd;\"> Q."+str(total)+"</td></tr>")
    for Pro in datosgenerales:
        if Pro.id=="propina":
            file.write("<tr><td colspan=\"3\" style=\"background-color: #cdcdcd;\">Propina "+str(round((float(Pro.valor)*100),2))+"%</td>")
            porcentaje=round((float(Pro.valor)*total),2)
            file.write("<td style=\"background-color: #cdcdcd;\"> Q."+str(porcentaje)+"</td></tr>")
    file.write("<tr><td colspan=\"3\" style=\"background-color: Gray;\">Total</td><td style=\"background-color: Gray;\"> Q."+str(total+porcentaje)+"</td>")
    file.write(parte6)
    file.close()
    os.startfile("Factura.html")