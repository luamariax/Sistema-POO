"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""
from modelos.Repositorio import Repositorio

class ServicoUser:
    def __init__(self, repositorio: Repositorio):
        self.repositorio = repositorio

    def autenticar(self, email: str, senha: str) -> dict | None:
        """
        Retorna os dados do usuário se autenticado, caso contrário None.
        """
        usuario = self.repositorio.buscar_usuario_por_email(email)
        if usuario and usuario['senha'] == senha:
            return usuario
        return None