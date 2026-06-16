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
                dados['id_eventos'] = self.servico.dic_objeto.get('id_eventos')
                # O view envia 'data_fim' mas a coluna no Excel é 'data_final'
                dados['data_final'] = dados.pop('data_fim', '')

                self.servico.repositorio.editar_evento(dados)

                # Atualiza o dicionário em memória para a tela refletir as mudanças
                self.servico._dic_objeto.update(dados)

                self.carregar_dados_para_tela()

                if self.rota.page:
                    self.visualizador.mostrar(self.rota.page)
        else:
            # Caso de segurança (fallback)
            self.rota.atualizar_estado(acao)

