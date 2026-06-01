"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

from .ControladorAbstrato import ControladorAbstrato
from Modelos.Servico import Servico


class ControladorEntrada(ControladorAbstrato):
    def __init__(self, rota, servico: Servico, visualizador):
        super().__init__(rota, servico, visualizador)

    def carregar_dados_para_tela(self):
        usuario_atual = self.servico.usuario_logado
        
        if not usuario_atual:
            print("CLASSE:ControladorEntrada.py// [Erro] Nenhum usuário logado no sistema.")
            return
        
        frase = f"Bem vindo (a)! {usuario_atual.nome}"
        
        self.visualizador.texto_boas_vindas.value = frase

    def processar_acao(self, acao: str, dados: dict = None):
        if acao == "1":
            # Comando 1 na Rota: vai para "pagina_todos_semestres"
            self.rota.atualizar_estado(acao)
            
        elif acao == "2":
            # Comando 2 na Rota: vai para "pagina_todos_eventos"
            self.rota.atualizar_estado(acao)
            
        elif acao == "0":
            # Comando 0 na Rota: Botão Voltar (vai para "pagina_inicial")
            # Limpamos o usuário do Serviço (Logout)
            self.servico.logout()
            self.rota.atualizar_estado(acao)
            
        else:
            self.rota.atualizar_estado(acao)