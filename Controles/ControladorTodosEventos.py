"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

from Servicos.Servico import Servico
from Controles.ControladorAbstrato import ControladorAbstrato
#versão passada
class ControladorTodosEventos(ControladorAbstrato):
    def __init__(self, rota, servico: Servico, visualizador):
        super().__init__(rota, servico, visualizador)
        self.repo = self.servico.repositorio

    def dar_dados(self):
        usar_id_user = "U001"
        lista_dict_eventos = self.repo.buscar_eventos_por_usuario(usar_id_user)
        return lista_dict_eventos

    def processar_acao(self, acao: str, dados: dict = None):
        self.rota.atualizar_estado(acao)