from Modelos.Repositorio import Repositorio
from Negocio.User import User
from Negocio.Evento import Evento
from Negocio.Semestre import Semestre
from Negocio.Materia import Materia
from Negocio.Prova import Prova
from Negocio.Trabalho import Trabalho

class Servico():
    def __init__(self, repositorio: Repositorio):
        self.repositorio = repositorio
        self._usuario_logado = None             # User
        self._objetos_do_usuario = []           # Lista Objetos
        self._atividades_do_usuario = []        # Lista AtividadeAvaliativa
        
        self._id_user_logado = None
        self._id_evento_logado = None        
        self._id_semestre_logado = None       
        self._id_materia_logado = None   
        self._id_prova_logado = None
        self._id_trabalho_logado = None


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
            self._id_user_logado = usuario_dict['id_user']
            return user
        return None

    def instanciar_objetos(self, tipo: str):
        """
        Vai chamar o repositorio para o 'tipo' de objeto referente a aquela id_user.
        Irá receber uma lista de dicionários, e interando pela lista criará os objetos.
        """
        if tipo == 'Semestres':
            todos_semestres_list_dict = self.repositorio.buscar_semestres_por_usuario(self._id_user_logado)
            for semestre_dict in todos_semestres_list_dict:
                novo_semestre = Semestre(
                    id=semestre_dict['id_semestre'],
                    titulo=semestre_dict['titulo'],
                    
                )



    def logout(self):
        """Desloga o usuário atual."""
        self._usuario_logado = None

    def cadastro_usuario(self, nome, email, senha):
        """
        Tenta autenticar o usuário, 
        Se bem-sucedido, ele dá erro de que usuário já existe.
        Do contrário, ele salva o novo user
        """
        usuario_dict = self.repositorio.buscar_usuario_por_email(email)
        if not usuario_dict:
            #Se não achar email
            dicionario = {"nome": nome, "email":email, "senha":senha}
            self.repositorio.criar_usuario(dicionario)
            return True
        return False
