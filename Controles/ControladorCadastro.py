"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""
from .ControladorAbstrato import ControladorAbstrato
from Servicos.ServicoUser import ServicoUser

class ControladorCadastro(ControladorAbstrato):
    def __init__(self, rota, service_login: ServicoUser, visualizador):
        super().__init__(rota)
        self.service = service_login
        self.visualizador = visualizador

    def processar_acao(self, acao: str, dados: dict = None):
        if acao == "cadastro":
            nome  = dados.get("nome")
            email = dados.get("email")
            senha = dados.get("senha")
            cadastro_valido = self.service.cadastro_usuario(nome, email, senha)
            if cadastro_valido:
                # Cadastro bem-sucedido: navega para página 4 (comando "1")
                self.visualizador.limpar_erro()
                self.rota.atualizar_estado("0")
            else:
                self.visualizador.mostrar_erro("Email já utilizado.")
        else:
            # Comandos normais da máquina de estados (ex: "0" para voltar)
            self.rota.atualizar_estado(acao)