"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""
import unittest
from unittest.mock import MagicMock

from Modelos.Repositorio import Repositorio
from Negocio.User import User

class ServicoUser():
    def __init__(self, repositorio: Repositorio):
        self.repositorio = repositorio
        self.usuario_logado = None   

    @property
    def usuario_logado(self) -> User | None:
        """Retorna o usuário atualmente logado, ou None."""
        return self._usuario_logado

    def autenticar(self, email: str, senha: str) -> User | None:
        """
        Tenta autenticar o usuário.
        Se bem-sucedido, cria um objeto User, armazena internamente e retorna.
        Caso contrário, retorna None.
        """
        usuario_dict = self.repositorio.buscar_usuario_por_email(email)
        if usuario_dict and usuario_dict['senha'] == senha:
            # Cria instância de User
            user = User(
                identificacao=usuario_dict['id_user'],
                endereco_eletronico=usuario_dict['email'],
                nome_do_usuario=usuario_dict['nome']
            )
            self._usuario_logado = user
            return user
        return None

    def logout(self):
        """Desloga o usuário atual."""
        self._usuario_logado = None
    




USUARIO_VALIDO = {
    "id_user": "U001",
    "email": "ana.souza@ufmg.br",
    "nome": "Ana Souza",
    "senha": "Abc@1234",
}


