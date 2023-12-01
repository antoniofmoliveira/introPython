"""
Listagem 9.10 – Geração de uma página web a partir de um dicionário
Exercício 9.30 Modifique o programa da listagem 9.10 para gerar uma lista html,
usando os elementos ul e li. Todos os elementos da lista devem estar dentro do
elemento ul, e cada item dentro de um elemento li. Exemplo:
<ul><li>Item1</li><li>Item2</li><li>Item3</li></ul>
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
        pagina.write("<ul>")
        for e in v:
            pagina.write(f"<li>{e:s}</li>")
        pagina.write("</ul>")
    pagina.write(
        """</body>
</html>
"""
    )
