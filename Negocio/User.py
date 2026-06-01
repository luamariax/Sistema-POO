
""" 
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
User não precisa guardar a senha, 
Pois só precisa da senha pra logar
o User será responsável por guardar os dados do usuário e validar os atributos, como id_user, email e nome. Ele deve garantir que os dados sejam válidos e não vazios, aplicando o método .strip() para remover espaços em branco. O User também tem métodos para acessar e modificar esses atributos de forma segura, utilizando propriedades (getters e setters) para garantir a integridade dos dados. Além disso, o User deve ser capaz de validar o formato do email para garantir que seja um endereço eletrônico válido.
"""
import unittest
from Negocio.Evento import Evento
from Negocio.Semestre import Semestre
from Modelos.Repositorio import Repositorio

class User():
    def __init__(self, identificacao: str, endereco_eletronico: str, nome_do_usuario: str):
        self._validar_dados(identificacao, endereco_eletronico, nome_do_usuario)
        self.id_user = identificacao
        self.__email = endereco_eletronico
        self.nome = nome_do_usuario
    
    @property
    def id_user(self):
        return self._id_user
    @id_user.setter
    def id_user(self, valor):
        if not valor.strip():
            raise ValueError("CLASSE:User.py//id_user não pode ser vazio.")
        self._id_user = valor.strip()

    @property
    def email(self):
        return self.__email

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, valor):
        if not valor.strip():
            raise ValueError("CLASSE:User.py//Nome não pode ser vazio.")
        self._nome = valor.strip()

    def _validar_dados(self, identificacao: str, endereco_eletronico: str, nome_do_usuario: str):
        if not isinstance(identificacao, str):
            raise TypeError("CLASSE:User.py//Identificação deve ser uma string.")
        if not identificacao.strip():
            raise ValueError("CLASSE:User.py//Identificação não pode ser vazia.")
        if not isinstance(endereco_eletronico, str):
            raise TypeError("CLASSE:User.py//Endereço eletrônico deve ser uma string.")
        if not endereco_eletronico.strip():
            raise ValueError("CLASSE:User.py//Endereço eletrônico não pode ser vazio.")
        if "@" not in endereco_eletronico or "." not in endereco_eletronico:
            raise ValueError("CLASSE:User.py//Endereço eletrônico deve ser um e-mail válido.")
        if not isinstance(nome_do_usuario, str):
            raise TypeError("CLASSE:User.py//Nome do usuário deve ser uma string.")
        if not nome_do_usuario.strip():
            raise ValueError("CLASSE:User.py//Nome do usuário não pode ser vazio.")

    def criar_dependente(self, tipo: str, dict_incompleto, repo: Repositorio):
        if tipo == 'Semestres':
            nova_id_semestre = repo.criar_semestre(dict_incompleto)
            semestre_dict = dict_incompleto
            semestre_dict['id_semestre'] = nova_id_semestre
            semestre_instanciado = Semestre(
                    id=semestre_dict['id_semestre'],
                    titulo=semestre_dict['titulo'],
                    descricao=semestre_dict['descricao'],
                    ano=semestre_dict['ano'],
                    semestre_num=semestre_dict['semestre_num'],
                    ativo=semestre_dict['ativo']
                )
            return semestre_instanciado
        elif tipo == 'Evento':
            nova_id_evento = repo.criar_evento(dict_incompleto)
            evento_dict = dict_incompleto
            evento_dict['id_evento'] = nova_id_evento
            evento_instanciado = Evento(
                    id=evento_dict['id_evento'],
                    titulo=evento_dict['titulo'],
                    descricao=evento_dict['descricao'],
                    data_inicio=evento_dict['data_inicio'],
                    data_fim=evento_dict['data_fim'],
                    local=evento_dict['local'],
                    organizador=evento_dict['organizador']
                )
            return evento_instanciado
        else:
            raise ValueError(f"Tipo {tipo} não valido para tal ação")
        


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