import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
src_path = path_root.joinpath('src')
sys.path.append(str(src_path))
import unittest
from unittest.mock import MagicMock

from models import Pedido  # type: ignore
from services import calcular_top_pedidos  # type: ignore


class TestCalcularTopPedidos(unittest.TestCase):

    def setUp(self):
        # Criando pedidos de exemplo
        self.pedido_1 = MagicMock(spec=Pedido)
        self.pedido_1.numero_pedido = "0000000123"
        self.pedido_1.calcular_valor_total.return_value = 150.0  # Quantidade 10, Valor Unitário 15.00
        
        self.pedido_2 = MagicMock(spec=Pedido)
        self.pedido_2.numero_pedido = "0000000456"
        self.pedido_2.calcular_valor_total.return_value = 200.0  # Quantidade 20, Valor Unitário 10.00
        
        self.pedido_3 = MagicMock(spec=Pedido)
        self.pedido_3.numero_pedido = "0000000789"
        self.pedido_3.calcular_valor_total.return_value = 120.0  # Quantidade 12, Valor Unitário 10.00
        
        self.pedido_4 = MagicMock(spec=Pedido)
        self.pedido_4.numero_pedido = "0000000001"
        self.pedido_4.calcular_valor_total.return_value = 180.0  # Quantidade 18, Valor Unitário 10.00
        
        self.pedido_5 = MagicMock(spec=Pedido)
        self.pedido_5.numero_pedido = "0000000987"
        self.pedido_5.calcular_valor_total.return_value = 250.0  # Quantidade 25, Valor Unitário 10.00

        self.pedido_6 = MagicMock(spec=Pedido)
        self.pedido_6.numero_pedido = "0000006543"
        self.pedido_6.calcular_valor_total.return_value = 100.0  # Quantidade 10, Valor Unitário 10.00

        self.pedidos = [self.pedido_1, self.pedido_2, self.pedido_3, self.pedido_4, self.pedido_5, self.pedido_6]

    def test_calcular_top_pedidos(self):
        # Chamando a função calcular_top_pedidos
        top_pedidos = calcular_top_pedidos(self.pedidos)

        # Verificando os valores calculados
        for pedido in top_pedidos:
            print(f"Pedido {pedido['numero_pedido']} - Valor Total: {pedido['valor_total']}")

        # Verificando a ordem
        self.assertEqual(top_pedidos[0]['numero_pedido'], "0000000987")  # Pedido 5 com 250.0
        self.assertEqual(top_pedidos[1]['numero_pedido'], "0000000456")  # Pedido 2 com 200.0
        self.assertEqual(top_pedidos[2]['numero_pedido'], "0000000001")  # Pedido 4 com 180.0

    def test_calcular_top_pedidos_limite_3(self):
        # Chamando a função calcular_top_pedidos com o limite de 3
        top_pedidos = calcular_top_pedidos(self.pedidos, limite=3)

        # Verificando os 3 primeiros pedidos
        self.assertEqual(top_pedidos[0]['numero_pedido'], "0000000987")  # Pedido 5 com 250.0
        self.assertEqual(top_pedidos[1]['numero_pedido'], "0000000456")  # Pedido 2 com 200.0
        self.assertEqual(top_pedidos[2]['numero_pedido'], "0000000001")  # Pedido 4 com 180.0

    def test_calcular_top_pedidos_vazio(self):
        # Testando a função com lista vazia
        top_pedidos = calcular_top_pedidos([])
        self.assertEqual(top_pedidos, [])

if __name__ == "__main__":
    unittest.main()