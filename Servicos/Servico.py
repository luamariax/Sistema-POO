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
        self._objetos_do_usuario = None         # Objeto
        self._atividades_do_usuario = None      # AtividadeAvaliativa
        
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

    def instanciar_objeto(self, tipo: str, posicao: int):
        """
        Vai chamar o repositorio para o 'tipo' de objeto referente a aquela id_user.
        Irá receber uma lista de dicionários, e selecionará pela posição recebida.
        Criará o objeto com o dicionário.
        """
        if tipo == 'Semestres':
            todos_semestres_list_dict = self.repositorio.buscar_semestres_por_usuario(self._id_user_logado)
            semestre_visualizado_dict = todos_semestres_list_dict[posicao]
            self._id_semestre_logado = semestre_visualizado_dict['id_semestre']
            semestre_instanciado = Semestre(
                    id=semestre_visualizado_dict['id_semestre'],
                    titulo=semestre_visualizado_dict['titulo'],
                    descricao=semestre_visualizado_dict['descricao'],
                    ano=semestre_visualizado_dict['ano'],
                    semestre_num=semestre_visualizado_dict['semestre_num'],
                    ativo=semestre_visualizado_dict['ativo']
                )
            self._objetos_do_usuario = semestre_instanciado
        elif tipo == 'Evento':
            todos_eventos_list_dict = self.repositorio.buscar_eventos_por_usuario(self._id_user_logado)
            evento_visualizado_dict = todos_eventos_list_dict[posicao]
            self._id_evento_logado = evento_visualizado_dict['id_semestre']
            evento_instanciado = Evento(
                    id=evento_visualizado_dict['id_evento'],
                    titulo=evento_visualizado_dict['titulo'],
                    descricao=evento_visualizado_dict['descricao'],
                    data_inicio=evento_visualizado_dict['data_inicio'],
                    data_fim=evento_visualizado_dict['data_fim'],
                    local=evento_visualizado_dict['local'],
                    organizador=evento_visualizado_dict['organizador']
                )
            self._objetos_do_usuario = evento_instanciado
        if tipo == 'Materia':
            todos_materias_list_dict = self.repositorio.buscar_materias_por_semestre_usuario(self._id_user_logado, self._id_semestre_logado)
            materia_visualizado_dict = todos_materias_list_dict[posicao]
            self._id_materia_logado = materia_visualizado_dict['id_semestre']
            materia_instanciado = Materia(
                id=materia_visualizado_dict['id'],
                titulo=materia_visualizado_dict['titulo'],
                descricao=materia_visualizado_dict['descricao'],
                professor=materia_visualizado_dict['professor'],
                sala=materia_visualizado_dict['sala'],
                horarios=materia_visualizado_dict['horarios']
            )
            self._objetos_do_usuario = materia_instanciado
        else:
            raise ValueError(f"Tipo {tipo} não valido para tal ação")
        
    def retirar_objeto(self, tipo: str):
        """
        Acaba com a instância do objeto que estava salvo
        """
        self._objetos_do_usuario = None
        if tipo == 'Semestre':
            self._id_semestre_logado = None
        elif tipo == 'Evento':
            self._id_evento_logado = None
        elif tipo == 'Materia':
            self._id_materia_logado = None
        else:
            raise ValueError(f"Tipo {tipo} não valido para tal ação")

    def instancia_atividade(self, tipo:str, posicao: int):
        if tipo == "Prova":
            pass
        elif tipo == "Trabalho":
            pass
        else:
            raise ValueError(f"Tipo {tipo} não valido para tal ação")
        
    def retira_atividade(self, tipo: str):
        """
        Acaba com a instância da atividade que estava salvo
        """
        self._objetos_do_usuario = None
        if tipo == 'Prova':
            self._id_prova_logado = None
        elif tipo == 'Trabalho':
            self._id_trabalho_logado = None
        else:
            raise ValueError(f"Tipo {tipo} não valido para tal ação")

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
