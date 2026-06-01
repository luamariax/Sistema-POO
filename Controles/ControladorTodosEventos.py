"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

from .ControladorAbstrato import ControladorAbstrato
from Servicos.Servico import Servico


class ControladorTodosEventos(ControladorAbstrato):
    def __init__(self, rota, servico: Servico, visualizador):
        super().__init__(rota, servico, visualizador)

    def carregar_dados_para_tela(self):
        usuario_atual = self.servico.usuario_logado
        
        if not usuario_atual:
            print("CLASSE:ControladorTodosEventos.py// [Erro] Nenhum utilizador logado.")
            return

        lista_eventos = self.servico.repositorio.buscar_eventos_por_usuario(usuario_atual.id_user)      
        self.visualizador.lista_eventos = lista_eventos

    def processar_acao(self, acao: str, dados: dict = None):
        if acao == "0":
            # 0 na Rota de "todos_eventos" volta para a "pagina_entrada"
            self.rota.atualizar_estado("0")
            
        elif "-" in acao:
            # O visualizador envia "1-0". O split("-") divide a string numa lista: ["1", "0"]
            partes = acao.split("-")
            comando_rota = partes[0]   
            posicao = int(partes[1])   
            
            if comando_rota == "1":
                self.servico.instanciar_objeto('Evento', posicao)
                self.rota.atualizar_estado(comando_rota)
            
        elif acao == "salvar_novo":
            if dados:
                dados['id_user'] = self.servico.usuario_logado.id_user
                
                self.servico.usuario_logado.criar_dependente('Evento', dados, self.servico.repositorio)
                
                self.carregar_dados_para_tela()
                
                if self.rota.page:
                    self.visualizador.mostrar(self.rota.page)
        else:
            # Caso de segurança (fallback)
            self.rota.atualizar_estado(acao)