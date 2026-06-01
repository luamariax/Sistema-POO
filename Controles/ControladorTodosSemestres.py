"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

""""
class ControladorTodosSemestres(ControladorAbstrato):
    def __init__(self, rota, servico: Servico, visualizador):
        super().__init__(rota, servico, visualizador)

        
    def processar_acao(self, acao: str, dados: dict = None):
        self.rota.atualizar_estado(acao)
"""


from .ControladorAbstrato import ControladorAbstrato
from Modelos.Servico import Servico


class ControladorTodosSemestres(ControladorAbstrato):
    def __init__(self, rota, servico: Servico, visualizador):
        super().__init__(rota, servico, visualizador)

    def carregar_dados_para_tela(self):
        usuario_atual = self.servico.usuario_logado
        
        if not usuario_atual:
            print("CLASSE:ControladorTodosSemestres.py// [Erro] Nenhum utilizador logado.")
            return

        lista_semestres = self.servico.repositorio.buscar_semestres_por_usuario(usuario_atual.id_user)       
        self.visualizador.lista_semestres = lista_semestres

    def processar_acao(self, acao: str, dados: dict = None):
        if acao == "0":
            # 0 na Rota de "todos_semestres" volta para a "pagina_entrada"
            self.rota.atualizar_estado("0")
            
        elif "-" in acao:
            # O visualizador envia "1-0". O split("-") divide a string numa lista: ["1", "0"]
            partes = acao.split("-")
            comando_rota = partes[0]   # Fica com o "1"
            posicao = int(partes[1])   # Fica com a posição matemática (ex: 0)
            
            if comando_rota == "1":
                self.servico.instanciar_objeto('Semestre', posicao)
                self.rota.atualizar_estado(comando_rota)
            
        elif acao == "salvar_novo":
            if dados:
                dados['id_user'] = self.servico.usuario_logado.id_user
                
                self.servico.usuario_logado.criar_dependente('Semestres', dados, self.servico.repositorio)
                
                self.carregar_dados_para_tela()
                
                if self.rota.page:
                    self.visualizador.mostrar(self.rota.page)
        else:
            # Caso de segurança (fallback)
            self.rota.atualizar_estado(acao)