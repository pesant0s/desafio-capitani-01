def calcular_top_pedidos(pedidos, limite=5):
    pedidos_com_valor_total = [
        {
            "numero_pedido": pedido.numero_pedido,
            "valor_total": pedido.calcular_valor_total()
        }
        for pedido in pedidos
    ]
    return sorted(pedidos_com_valor_total, key=lambda x: x["valor_total"], reverse=True)[:limite]