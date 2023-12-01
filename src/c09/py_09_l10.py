"""
Listagem 9.10 – Geração de uma página web a partir de um dicionário
"""
filmes = {
    "drama": ["Cidadão Kane", "O Poderoso Chefão"],
    "comédia": ["Tempos Modernos", "American Pie", "Dr. Dolittle"],
    "policial": ["Chuva Negra", "Desejo de Matar", "Difícil de Matar"],
    "guerra": ["Rambo", "Platoon", "Tora!Tora!Tora!"],
}
with open("filmes.html", "w", encoding="utf-8") as pagina:
    pagina.write(
        """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Filmes</title>
</head>
<body>
"""
    )
    for c, v in filmes.items():
        pagina.write(f"<h1>{c:s}</h1>")
        for e in v:
            pagina.write(f"<h2>{e:s}</h2>")
    pagina.write(
        """</body>
</html>
"""
    )
