import os

parte1=""""
<html>
    <head>
        <title>Tokens</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
    </head>
    <body>
        <nav class="navbar navbar-light" style="background-color: #e3f2fd;">
            <div class="container-fluid">
              <span class="navbar-brand mb-0 h1">Tabla de Tokens</span>
            </div>
        </nav>
        <center>
"""

parte2="""
        </center>
        <div>
            <center>
                <table class="table table-dark table-hover">
                    <thead>
                        <tr>
                            <th><center>No.</center></th>
                            <th><center>Tokens</center></th>
                            <th><center>Fila</center></th>
                            <th><center>Columna</center></th>
                            <th><center>Lexema</center></th>
                        </tr>
                    </thead>
"""

parte3="""
                </table>
            </center>
        </div>
    </body>
</html>
"""

def generar(token, archivo):
    cont=1
    file = open("Tabla de Token del "+archivo+".html", "w")
    file.write(parte1)
    file.write("<p class=\"h1\">"+archivo+"</p>")
    file.write(parte2)
    for i in token:
        file.write("<tr><td><center>"+str(cont)+"</center></td><td><center>"+i.token+"</center></td><td><center>"+str(i.fila)+"</center></td><td><center>"+str(i.columna)+"</center></td><td><center>"+i.lexema+"</center></td></tr>")
        cont+=1
    file.write(parte3)
    file.close()