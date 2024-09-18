import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')
os.environ["LLAMA_CLOUD_API_KEY"] = token

from llama_parse import LlamaParse

documentos = LlamaParse(result_type="text")