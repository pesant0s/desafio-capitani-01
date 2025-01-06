class PedidoInvalidoError(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class PedidoVazio(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)