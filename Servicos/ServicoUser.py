"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""
import unittest
from unittest.mock import MagicMock

from Modelos.Repositorio import Repositorio
from Negocio.User import User

class ServiceLogin:
    def __init__(self, repositorio: Repositorio):
        self.repositorio = repositorio
        self._usuario_logado = None   

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


class TestServicoUserAutenticar(unittest.TestCase):

    def setUp(self):
        self.repositorio = MagicMock()
        self.servico = ServicoUser(self.repositorio)

    # ── caso 1: credenciais corretas ──────────────────────────────────────
    def test_autenticar_credenciais_validas_retorna_usuario(self):
        self.repositorio.buscar_usuario_por_email.return_value = USUARIO_VALIDO

        resultado = self.servico.autenticar("ana.souza@ufmg.br", "Abc@1234")

        self.assertEqual(resultado, USUARIO_VALIDO)

    def test_autenticar_credenciais_validas_popula_self_user(self):
        self.repositorio.buscar_usuario_por_email.return_value = USUARIO_VALIDO

        self.servico.autenticar("ana.souza@ufmg.br", "Abc@1234")

        self.assertIsNotNone(self.servico.user)
        self.assertEqual(self.servico.user.email, "ana.souza@ufmg.br")
        self.assertEqual(self.servico.user.nome, "Ana Souza")

    # ── caso 2: senha incorreta ───────────────────────────────────────────
    def test_autenticar_senha_incorreta_retorna_none(self):
        self.repositorio.buscar_usuario_por_email.return_value = USUARIO_VALIDO

        resultado = self.servico.autenticar("ana.souza@ufmg.br", "SenhaErrada")

        self.assertIsNone(resultado)

    def test_autenticar_senha_incorreta_nao_popula_self_user(self):
        self.repositorio.buscar_usuario_por_email.return_value = USUARIO_VALIDO

        self.servico.autenticar("ana.souza@ufmg.br", "SenhaErrada")

        self.assertIsNone(self.servico.user)

    # ── caso 3: email não encontrado ──────────────────────────────────────
    def test_autenticar_email_inexistente_retorna_none(self):
        self.repositorio.buscar_usuario_por_email.return_value = None

        resultado = self.servico.autenticar("desconhecido@ufmg.br", "Abc@1234")

        self.assertIsNone(resultado)

    def test_autenticar_email_inexistente_nao_popula_self_user(self):
        self.repositorio.buscar_usuario_por_email.return_value = None

        self.servico.autenticar("desconhecido@ufmg.br", "Abc@1234")

        self.assertIsNone(self.servico.user)

    # ── caso 4: verificação de interação com o repositório ───────────────
    def test_autenticar_chama_repositorio_com_email_correto(self):
        self.repositorio.buscar_usuario_por_email.return_value = None

        self.servico.autenticar("ana.souza@ufmg.br", "Abc@1234")

        self.repositorio.buscar_usuario_por_email.assert_called_once_with(
            "ana.souza@ufmg.br"
        )


if __name__ == "__main__":
    unittest.main()
