"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""
from .ControladorAbstrato import ControladorAbstrato

"""import dos servicos"""
from Controles.ControladorAbstrato import ControladorAbstrato
class ControladorEspecificoEvento(ControladorAbstrato):
    def processar_acao(self, acao: str, dados: dict = None):
        self.rota.atualizar_estado(acao)