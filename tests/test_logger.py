import os
import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
src_path = path_root.joinpath('src')
sys.path.append(str(src_path))
from logger import logger  # type: ignore


def test_logger_cria_arquivo():
    log_dir = "logs"
    
    # Logando uma mensagem para testar
    logger.info("Teste de log")
    
    # Verificando se algum arquivo foi criado no diretório logs
    log_files = [f for f in os.listdir(log_dir) if f.endswith(".log")]
    
    # Assertiva de que pelo menos um arquivo de log foi criado
    assert len(log_files) > 0, f"Nenhum arquivo de log encontrado no diretório {log_dir}"