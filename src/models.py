from exceptions import PedidoInvalidoError


class Pedido:
    def __init__(self, numero_pedido, quantidade, valor_unitario):
        self.numero_pedido = self.validar_numero_pedido(numero_pedido)
        self.quantidade = self.validar_quantidade(quantidade)
        self.valor_unitario = self.validar_valor_unitario(valor_unitario)

    def calcular_valor_total(self):
        return self.quantidade * self.valor_unitario

    @staticmethod
    def validar_numero_pedido(numero):
        if not numero.isdigit() or len(numero) != 10:
            raise PedidoInvalidoError(f"Número do pedido inválido: {numero}")
        return numero

    @staticmethod
    def validar_quantidade(quantidade):
        try:
            quantidade = int(quantidade)
            if quantidade <= 0:
                raise ValueError()
            return quantidade
        except ValueError:
            raise PedidoInvalidoError(f"Quantidade inválida: {quantidade}")

    @staticmethod
    def validar_valor_unitario(valor):
        try:
            valor = int(valor) / 100
            if valor <= 0:
                raise ValueError()
            return valor
        except ValueError:
            raise PedidoInvalidoError(f"Valor unitário inválido: {valor}")