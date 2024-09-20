import re
import pandas as pd

# --------------------  FUNÇÕES  --------------------  #

def tratar_tabelas(texto):
    regras = re.compile(r'((?:\|.+\|(?:\n|\r))+)', re.MULTILINE)
    tabelas = regras.findall(texto)
    return tabelas

def transf_mk_excel(texto):
    tabelas = tratar_tabelas(texto)
    print(len(tabelas))
    if len(tabelas) > 0:
        pass

# --------------------  MAIN  -------------------- #

pasta = "PaginasPDF"

with open(f"{pasta}/pagina9.md", "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()

transf_mk_excel(texto)
