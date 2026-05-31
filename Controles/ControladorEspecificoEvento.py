"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""
from .ControladorAbstrato import ControladorAbstrato
from Servicos.Servico import Servico

class ControladorEspecificoEvento(ControladorAbstrato):
    def __init__(self, rota, servico: Servico, visualizador):
        super().__init__(rota, servico, visualizador)

    def processar_acao(self, acao: str, dados: dict = None):
        self.rota.atualizar_estado(acao)