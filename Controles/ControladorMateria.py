"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

""""
from .ControladorAbstrato import ControladorAbstrato

#import dos servicos
from Controles.ControladorAbstrato import ControladorAbstrato
class ControladorMateria(ControladorAbstrato):
    def processar_acao(self, acao: str, dados: dict = None):
        self.rota.atualizar_estado(acao)
"""
"""
padrões de escrita
classe usa PascalCase
função e variáveis usa snake_case
"""
from .ControladorAbstrato import ControladorAbstrato
from Servicos.Servico import Servico

class ControladorMateria(ControladorAbstrato):
    def __init__(self, rota, servico: Servico, visualizador):
        super().__init__(rota, servico, visualizador)


    def carregar_dados_para_tela(self):
        materia = self.servico._objetos_do_usuario
        if materia:
            self.visualizador.titulo_materia = materia.titulo
            self.visualizador.professor = materia.professor
            self.visualizador.sala = materia.sala
            self.visualizador.horarios = materia.horarios
        else:
            print("ControladorMateria: Nenhum objeto de matéria encontrado no serviço.")

    def processar_acao(self, acao: str, dados: dict = None):
        if acao == "0":
            self.rota.atualizar_estado("0")
        elif acao == "1":
            self.rota.atualizar_estado("1")
        elif acao == "2":
            self.rota.atualizar_estado("2")