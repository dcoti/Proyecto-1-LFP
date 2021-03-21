import  os
parte1="""
<html>
    <head>
        <meta charset="utf-8">
        <title>
"""
parte2="""
</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
        <link href="attrib.css" rel="stylesheet">
    </head>
        <body>
            <!-- Image and text -->
        <nav class="navbar navbar-light" style="background-color: Gray;">
            <div class="container-fluid">
            <a class="navbar-brand" href="#">
                
"""
parte3="""
</a>
            </div>
        </nav>
        <br>
"""
parte4="""
</h3>
"""
parte5="""
<h6 class="lead" id="desc">
"""
parte6="""
</h6>
"""
parte7="""
</body>
</html>
"""

def Menus(men):
    file = open("Menu.html","w")
    file.write(parte1)
    for s in men:
        if s.id=="restaurante":
            file.write("Menu del Restaurante \""+s.valor+"\"")
    file.write(parte2)
    for s in men:
        if s.id=="restaurante":
            file.write("<h4>Restaurante \""+s.valor+"\"</h4>")
    file.write(parte3)
    for s in men:
        if s.id=="Comida":
            file.write("<h3><small class=\"text-muted\" id=\"encabezado\">"+s.valor+"</small>")
            file.write(parte4)
            for a in men:
                if (a.id!="restaurante") & (a.id!="Comida") & (a.id!="Precio") & (a.id!="Descripcion") & (s.cont==a.cont):
                    for m in men:
                        if (m.id=="Precio") & (a.cont==m.cont) & (a.contdes==m.contdes):
                            file.write("<p class=\"h5\" id=\"secundary\">"+a.valor+" Q."+m.valor+"</p>")
                            file.write(parte5)
                            for d in men:
                                    if (d.id=="Descripcion") & (a.cont==d.cont) & (a.contdes==d.contdes):
                                        file.write("<small>"+d.valor+"</small>")
                                        file.write(parte6)
                                        break
    file.write(parte7)
    file.close()
    os.startfile("Menu.html")

