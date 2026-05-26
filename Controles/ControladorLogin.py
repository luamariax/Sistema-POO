"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

from .ControladorAbstrato import ControladorAbstrato
from Servicos.ServicoUser import ServicoUser

class ControladorLogin(ControladorAbstrato):
    def __init__(self, rota, service_login: ServicoUser, visualizador):
        super().__init__(rota)
        self.service = service_login
        self.visualizador = visualizador

    def processar_acao(self, acao: str, dados: dict = None):
        if acao == "login":
            email = dados.get("email")
            senha = dados.get("senha")
            usuario = self.service.autenticar(email, senha)
            if usuario:
                # Login bem-sucedido: navega para página 4 (comando "1")
                self.visualizador.limpar_erro()
                self.rota.atualizar_estado("1")
            else:
                self.visualizador.mostrar_erro("Email ou senha inválidos.")
        else:
            # Comandos normais da máquina de estados (ex: "0" para voltar)
            self.rota.atualizar_estado(acao)