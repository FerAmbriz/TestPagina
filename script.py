import datetime

# Obtener la hora actual
ahora = datetime.datetime.now()

# Crear contenido HTML
contenido_html = f"""
<html>
<head>
    <title>Mi Página en GitHub Pages</title>
</head>
<body>
    <h1>Hola, mundo!</h1>
    <p>La hora actual es: {ahora}</p>
</body>
</html>
"""

# Guardar el contenido en un archivo HTML
with open("index.html", "w") as archivo:
    archivo.write(contenido_html)
