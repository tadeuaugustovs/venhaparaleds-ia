from crewai.tools import BaseTool
from typing import Type, List
from pydantic import BaseModel, Field
import os
import PyPDF2

class EntradaExtracaoPDF(BaseModel):
    """Esquema de entrada para extração de texto de PDFs."""
    caminho_pasta: str = Field(
        default=os.path.join(os.getcwd(), "pdfs"),
        description="Caminho para a pasta contendo os PDFs.")
    tamanho_trecho: int = Field(100, description="Número de caracteres por trecho extraído.")
    max_trechos: int = Field(20, description="Número máximo de trechos extraídos por documento.")

class ExtratorPDF(BaseTool):
    name: str = "Extrator de PDF"
    description: str = "Extrai texto de PDFs na pasta fixa e os divide em partes gerenciáveis."
    args_schema: Type[BaseModel] = EntradaExtracaoPDF

    def _run(self, caminho_pasta: str = None, tamanho_trecho: int = 100, max_trechos: int = 20) -> List[str]:
        caminho_pasta = os.path.join(os.getcwd(), "pdfs")
        textos_extraidos = []
        total_tokens = 0
        limite_tokens = 8000  # Limite máximo de tokens antes de reduzir o tamanho

        print(f"Diretório atual: {os.getcwd()}")
        print(f"Tentando acessar: {caminho_pasta}")

        if not os.path.exists(caminho_pasta):
            return [f"Erro: A pasta '{caminho_pasta}' não existe."]

        for nome_arquivo in os.listdir(caminho_pasta):
            if nome_arquivo.endswith(".pdf"):
                caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)
                with open(caminho_arquivo, "rb") as arquivo:
                    leitor = PyPDF2.PdfReader(arquivo)
                    texto = "".join((pagina.extract_text() or "").strip().replace("\n", " ") for pagina in leitor.pages)

                    # Divide o texto em partes menores
                    trechos = [texto[i:i+tamanho_trecho] for i in range(0, len(texto), tamanho_trecho)][:max_trechos]

                    # Calcula total de tokens antes de enviar
                    total_tokens += sum(len(t) for t in trechos)
                    print(f"Total de tokens extraídos do PDF {nome_arquivo}: {total_tokens}")

                    # Se ultrapassar o limite, reduz tamanho dos trechos e a quantidade extraída
                    while total_tokens > limite_tokens:
                        print("⚠️ Excesso de tokens! Reduzindo tamanho dos trechos e quantidade extraída...")
                        tamanho_trecho = max(50, tamanho_trecho // 2)  # Reduz tamanho do trecho, mínimo de 50 caracteres
                        max_trechos = max(5, max_trechos // 2)  # Reduz a quantidade de trechos, mínimo de 5
                        trechos = [texto[i:i+tamanho_trecho] for i in range(0, len(texto), tamanho_trecho)][:max_trechos]
                        total_tokens = sum(len(t) for t in trechos)

                    textos_extraidos.extend(trechos)

        return textos_extraidos
