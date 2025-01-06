import os

from exceptions import PedidoInvalidoError, PedidoVazio
from logger import logger
from models import Pedido


def ler_pedidos(caminho):
    pedidos = []
    try:
        with open(caminho, "r") as arquivo:
            linhas = arquivo.readlines()
            if not linhas:
                raise PedidoVazio("O arquivo está vazio.")

            for linha in linhas:
                try:
                    pedidos.append(Pedido(
                        numero_pedido=linha[0:10].strip(),
                        quantidade=linha[10:15].strip(),
                        valor_unitario=linha[15:25].strip(),
                    ))
                except PedidoInvalidoError as e:
                    logger.warning(f"Pedido inválido ignorado: {linha}. Erro: {e}")
        return pedidos

    except:
        raise

def salvar_relatorio(caminho, pedidos):
    try:
        dir_saida = os.path.dirname(caminho)
        if dir_saida and not os.path.exists(dir_saida):
            os.makedirs(dir_saida)

        with open(caminho, "w") as arquivo:
            arquivo.write("Top 5 Pedidos por Valor Total:\n")
            arquivo.write("Número do Pedido | Valor Total\n")
            arquivo.write("-" * 30 + "\n")
            for pedido in pedidos:
                arquivo.write(f"{pedido['numero_pedido']} | R$ {pedido['valor_total']:.2f}\n")

    except PermissionError:
        logger.error(f"Permissão negada ao tentar salvar o relatório: {caminho}")
        raise
    except Exception as e:
        logger.error(f"Erro inesperado ao salvar relatório: {e}")
        raise