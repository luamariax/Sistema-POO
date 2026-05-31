"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""
from abc import ABC, abstractmethod


class ControladorAbstrato(ABC):
    def __init__(self, rota, servico, visualizador):
        self.rota = rota
        self.servico = servico
        self.visualizador = visualizador
    
    @abstractmethod
    def processar_acao(self, acao: str, dados: dict = None):
        pass
