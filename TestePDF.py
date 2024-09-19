from llama_parse import LlamaParse
import os

os.environ["LLAMA_CLOUD_API_KEY"] = "llx-Vd2XDaZuzQC9lPWqUD942greU98GyoPGzIfMzEqmNKxW7ImZ"


documentos = LlamaParse(result_type="text")

print(len(documentos))
