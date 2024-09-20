from llama_parse import LlamaParse
import os

pasta = "PaginasPDF"
os.environ["LLAMA_CLOUD_API_KEY"] = "llx-Vd2XDaZuzQC9lPWqUD942greU98GyoPGzIfMzEqmNKxW7ImZ"

documentos = LlamaParse(result_type="markdown",
                        parsing_instruction="this file contains text and tables, I'd like to get only the tables from the text").load_data("resultado.pdf")

for i, pagina in enumerate(documentos):
    with open(f"{pasta}/pagina{i+1}.md", "w", encoding="utf-8") as arquivo:
        arquivo.write(pagina.text)

# for i, paginas in enumerate(pasta):
#    with open (f"{pasta}/pagina{i+1}.md", "r", encoding="utf-8") as arquivo:
#        texto = arquivo.read()

with open(f"{pasta}/pagina9.md", "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()

# print(texto)
