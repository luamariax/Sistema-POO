"""
padrões de escrita
classe usa PascalCase
função e variáveis usa snake_case
"""
from .ControladorAbstrato import ControladorAbstrato
from Modelos.Servico import Servico

class ControladorProva(ControladorAbstrato):
    def __init__(self, rota, servico: Servico, visualizador):
        super().__init__(rota, servico, visualizador)

    def carregar_dados_para_tela(self):
        prova_dict = self.servico._dic_atividade
        if not prova_dict:
            return
        self.visualizador.titulo = prova_dict.get('titulo', '')
        self.visualizador.dia = prova_dict.get('dia', '')
        self.visualizador.conteudo = prova_dict.get('conteudo', '')
        self.visualizador.sala = prova_dict.get('sala', '')
        self.visualizador.duracao = prova_dict.get('duracao', '')
        self.visualizador.valor_nota = prova_dict.get('valor_nota', '')
        self.visualizador.nota_obtida = prova_dict.get('nota_obtida', '')

    def processar_acao(self, acao: str, dados: dict = None):
        if acao == "0":
            self.servico._id_prova_logado = None
            self.servico._dic_atividade = None
            self.rota.atualizar_estado("0")

        elif acao == "salvar_nota":
            if dados:
                dados['id_user'] = self.servico.id_user_logado
                dados['id_semestre'] = self.servico.id_semestre_logado
                dados['id_materia'] = self.servico.id_materia_logado
                dados['id_prova'] = self.servico._id_prova_logado
                self.servico.repositorio.editar_prova(dados)
                if self.servico._dic_atividade is not None:
                    self.servico._dic_atividade['nota_obtida'] = dados['nota_obtida']
                self.carregar_dados_para_tela()
                if self.rota.page:
                    self.visualizador.mostrar(self.rota.page)
