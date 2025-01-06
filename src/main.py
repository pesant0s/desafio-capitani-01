from config import Config
from exceptions import *
from logger import logger
from repositories import ler_pedidos, salvar_relatorio
from services import calcular_top_pedidos


def main():
    logger.info("Início...")
    try:
        pedidos = ler_pedidos(Config.ENTRADA_PATH)
        top_pedidos = calcular_top_pedidos(pedidos)
        salvar_relatorio(Config.SAIDA_PATH, top_pedidos)
    except PedidoVazio as pv:
        logger.warning(str(pv))
    except Exception as e:
        logger.error(f"Ocorreu um erro crítico durante o processamento: {str(e)}")
    
    logger.info("Fim do processamento!")

if __name__ == "__main__":
    main()