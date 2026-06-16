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

        elif acao == "salvar_nota":
            if dados:
                dados['id_user'] = self.servico.id_user_logado
                dados['id_semestre'] = self.servico.id_semestre_logado
                dados['id_materia'] = self.servico.id_materia_logado
                dados['id_trabalho'] = self.servico._id_trabalho_logado
                self.servico.repositorio.editar_trabalho(dados)
                if self.servico._dic_atividade is not None:
                    self.servico._dic_atividade['nota_obtida'] = dados['nota_obtida']
                self.carregar_dados_para_tela()
                if self.rota.page:
                    self.visualizador.mostrar(self.rota.page)

        elif acao == "marcar_entregue":
            dados_entrega = {
                'id_user': self.servico.id_user_logado,
                'id_semestre': self.servico.id_semestre_logado,
                'id_materia': self.servico.id_materia_logado,
                'id_trabalho': self.servico._id_trabalho_logado,
                'entregue': "True"
            }
            self.servico.repositorio.editar_trabalho(dados_entrega)
            if self.servico._dic_atividade is not None:
                self.servico._dic_atividade['entregue'] = "True"
            self.carregar_dados_para_tela()
            if self.rota.page:
                self.visualizador.mostrar(self.rota.page)
