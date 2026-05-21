"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""
from abc import ABC, abstractmethod
from modelos.Rota import Rota

class ControladorAbstrato(ABC):
    def __init__(self, rota: Rota):
        self.rota = rota
    
    @abstractmethod
    def processar_acao(self, acao: str, dados: dict = None):
        pass
