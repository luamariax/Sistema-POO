"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""
from .ControladorAbstrato import ControladorAbstrato
from Modelos.Servico import Servico


class ControladorEspecificoEvento(ControladorAbstrato):
    def __init__(self, rota, servico: Servico, visualizador):
        super().__init__(rota, servico, visualizador)

    def carregar_dados_para_tela(self):
        usuario_atual = self.servico.usuario_logado

        if not usuario_atual:
            print("CLASSE:ControladorEspecificoEvento.py// [Erro] Nenhum utilizador logado.")
            return

        if not self.servico.dic_objeto:
            print("CLASSE:ControladorEspecificoEvento.py// [Erro] Nenhum evento selecionado no serviço.")
            return

        self.visualizador.evento = self.servico.dic_objeto

    def processar_acao(self, acao: str, dados: dict = None):
        if acao == "0":
            # 0 na rota de "especifico_evento" volta para "todos_eventos"
            self.rota.atualizar_estado("0")

        elif acao == "salvar_edicao":
            if dados:
                dados['id_user'] = self.servico.usuario_logado.id_user

                self.servico.usuario_logado.editar_dependente('Evento', dados, self.servico.repositorio)

                self.carregar_dados_para_tela()

                if self.rota.page:
                    self.visualizador.mostrar(self.rota.page)
        else:
            # Caso de segurança (fallback)
            self.rota.atualizar_estado(acao)

