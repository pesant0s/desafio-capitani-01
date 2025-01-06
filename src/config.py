import os


class Config:
    ENTRADA_PATH = os.getenv("DESAFIO_ENTRADA_PATH", "data/entrada.txt")
    SAIDA_PATH = os.getenv("DESAFIO_SAIDA_PATH", "data/saida.txt")