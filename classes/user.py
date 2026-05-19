
""" 
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
User não precisa guardar a senha, 
Pois só precisa da senha pra logar

"""
import unittest


class User():
    def __init__(self, identificacao: str, endereco_eletronico: str, nome_do_usuario: str):
        self._validar_dados(identificacao, endereco_eletronico, nome_do_usuario)
        self.id_user = identificacao
        self.email = endereco_eletronico
        self.nome = nome_do_usuario
    
    @property
    def id_user(self):
        return self._id_user
    @id_user.setter
    def id_user(self, valor):
        if not valor.strip():
            raise ValueError("Não pode ser vazio.")
        self._id_user = valor.strip()

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, valor):
        if not valor.strip():
            raise ValueError("Não pode ser vazio.")
        self._email = valor.strip()

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, valor):
        if not valor.strip():
            raise ValueError("Não pode ser vazio.")
        self._nome = valor.strip()

    def _validar_dados(self, identificacao: str, endereco_eletronico: str, nome_do_usuario: str):
        if not isinstance(identificacao, str):
            raise TypeError("Identificação deve ser uma string.")
        if not identificacao.strip():
            raise ValueError("Identificação não pode ser vazia.")
        if not isinstance(endereco_eletronico, str):
            raise TypeError("Endereço eletrônico deve ser uma string.")
        if not endereco_eletronico.strip():
            raise ValueError("Endereço eletrônico não pode ser vazio.")
        if "@" not in endereco_eletronico or "." not in endereco_eletronico:
            raise ValueError("Endereço eletrônico deve ser um e-mail válido.")
        if not isinstance(nome_do_usuario, str):
            raise TypeError("Nome do usuário deve ser uma string.")
        if not nome_do_usuario.strip():
            raise ValueError("Nome do usuário não pode ser vazio.")
        if not hasattr(self, 'id_user') or not hasattr(self, 'email') or not hasattr(self, 'nome'):
            raise ValueError("O objeto deve ter os atributos id_user, email e nome.")
        
        


class TestUser(unittest.TestCase):

    def test_criar_usuario_valido(self):
        """Testa a criação de um usuário com dados válidos."""
        user = User("123", "usuario@email.com", "João Silva")
        
        self.assertEqual(user.id_user, "123")
        self.assertEqual(user.email, "usuario@email.com")
        self.assertEqual(user.nome, "João Silva")

    def test_remocao_de_espacos_em_branco(self):
        """Testa se o setter aplica o .strip() corretamente nos atributos."""
        user = User("  456  ", "  teste@email.com  ", "  Maria Souza  ")
        
        self.assertEqual(user.id_user, "456")
        self.assertEqual(user.email, "teste@email.com")
        self.assertEqual(user.nome, "Maria Souza")

    def test_id_usuario_vazio_deve_lancar_erro(self):
        """Testa se um ValueError é lançado quando a identificação é vazia."""
        with self.assertRaises(ValueError) as context:
            User("", "usuario@email.com", "João Silva")
        self.assertEqual(str(context.exception), "Não pode ser vazio.")

        # Testando também apenas com espaços
        with self.assertRaises(ValueError):
            User("   ", "usuario@email.com", "João Silva")

    def test_email_vazio_deve_lancar_erro(self):
        """Testa se um ValueError é lançado quando o e-mail é vazio."""
        with self.assertRaises(ValueError) as context:
            User("123", "", "João Silva")
        self.assertEqual(str(context.exception), "Não pode ser vazio.")

        with self.assertRaises(ValueError):
            User("123", "   ", "João Silva")

    def test_nome_vazio_deve_lancar_erro(self):
        """Testa se um ValueError é lançado quando o nome é vazio."""
        with self.assertRaises(ValueError) as context:
            User("123", "usuario@email.com", "")
        self.assertEqual(str(context.exception), "Não pode ser vazio.")

        with self.assertRaises(ValueError):
            User("123", "usuario@email.com", "   ")

    def test_modificacao_de_atributos_com_sucesso(self):
        """Testa se a alteração dos atributos através das propriedades funciona."""
        user = User("123", "antigo@email.com", "Carlos")
        
        user.id_user = "789"
        user.email = "novo@email.com"
        user.nome = "Carlos Eduardo"
        
        self.assertEqual(user.id_user, "789")
        self.assertEqual(user.email, "novo@email.com")
        self.assertEqual(user.nome, "Carlos Eduardo")

if __name__ == '__main__':
    unittest.main()