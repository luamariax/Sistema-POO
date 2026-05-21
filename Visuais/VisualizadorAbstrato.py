"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""
from abc import ABC, abstractmethod


class VisualizadorAbstrato(ABC):
    @abstractmethod
    def nome_da_pagina(self) -> str:
        pass
    
    @abstractmethod
    def construir(self):
        pass
    
    @abstractmethod
    def mostrar(self, page):
        pass

    