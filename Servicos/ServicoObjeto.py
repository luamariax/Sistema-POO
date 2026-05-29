"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""
from Modelos.Repositorio import Repositorio
class ServicoObjeto():
    def __init__(self, repositorio: Repositorio):
        self.repositorio = repositorio
        self._objetos = None   