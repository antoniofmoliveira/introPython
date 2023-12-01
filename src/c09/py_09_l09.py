"""
Listagem 9.9 – Uso de aspas triplas para escrever as strings
"""
with open("pagina.html", "w", encoding="utf-8") as pagina:
    pagina.write(
        """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Título da Página</title>
</head>
<body>
Olá!
"""
    )
    for l in range(10):
        pagina.write(f"<p>{l:d}</p>\n")
    pagina.write(
        """</body>
</html>
    """
    )
