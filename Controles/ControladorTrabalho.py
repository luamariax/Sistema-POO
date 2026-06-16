"""
padrões de escrita
classe usa PascalCase
função e variáveis usa snake_case
"""
from .ControladorAbstrato import ControladorAbstrato
from Modelos.Servico import Servico

class ControladorTrabalho(ControladorAbstrato):
    def __init__(self, rota, servico: Servico, visualizador):
        super().__init__(rota, servico, visualizador)

    def carregar_dados_para_tela(self):
        trabalho_dict = self.servico._dic_atividade
        if not trabalho_dict:
            return
        self.visualizador.titulo = trabalho_dict.get('titulo', '')
        self.visualizador.data_entrega = trabalho_dict.get('data_entrega', '')
        self.visualizador.descricao_tarefa = trabalho_dict.get('descricao_tarefa', '')
        self.visualizador.grupo = trabalho_dict.get('grupo', '')
        self.visualizador.entregue = trabalho_dict.get('entregue', '')
        self.visualizador.valor_nota = trabalho_dict.get('valor_nota', '')
        self.visualizador.nota_obtida = trabalho_dict.get('nota_obtida', '')

    def processar_acao(self, acao: str, dados: dict = None):
        if acao == "0":
            self.servico._id_trabalho_logado = None
            self.servico._dic_atividade = None
            self.rota.atualizar_estado("0")
