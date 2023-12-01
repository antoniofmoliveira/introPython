"""
Listagem 9.25 – Combinação dos componentes de um caminho

### comporta de forma diferente no windows e no linux
"""
import os.path

print(os.path.join("c:", "dados", "programas"))
print(os.path.abspath(os.path.join("c:", "dados", "programas")))

print(os.path.join("/", "dados", "programas"))
print(os.path.abspath(os.path.join("/", "dados", "programas")))
