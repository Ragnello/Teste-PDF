import re
import pandas as pd
from io import StringIO
import os

# --------------------  FUNÇÕES  --------------------  #

def tratar_tabelas(texto):
    regras = re.compile(r'((?:\|.+\|(?:\n|\r))+)', re.MULTILINE)
    tabelas = regras.findall(texto)
    return tabelas


def transf_mk_excel(texto, num_pagina):
    lista_tabelas = tratar_tabelas(texto)
    if len(lista_tabelas) > 0:
        # Ler as tabelas
        for i, texto_tabela in enumerate(lista_tabelas):
            tabela = pd.read_csv(StringIO(texto_tabela),
                                 sep="|", encoding="utf-8", engine="python")
            tabela = tabela.dropna(how="all", axis=0)
            tabela = tabela.dropna(how="all", axis=1)

            # Salvar em excel
            tabela.to_excel(f"tabelas/Pagina{num_pagina}_tabela{i+1}.xlsx", index=False)

# --------------------  MAIN  -------------------- #

pasta = "PaginasPDF"
lista_paginas = os.listdir(pasta)

for i, pagina in enumerate(lista_paginas):
    with open(f"{pasta}/{pagina}", "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()

    num_pagina = i+1
    transf_mk_excel(texto, num_pagina)
