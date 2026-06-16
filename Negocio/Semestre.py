from .Objeto import Objeto
from Modelos.Repositorio import Repositorio
from Negocio.Materia import Materia

class Semestre(Objeto):
    def __init__(self, id: int, titulo: str, descricao: str, ano: int, semestre_num: int, ativo: bool):
        super().__init__(id, titulo, descricao)
        
        self.ano = ano                      #Type int
        self.semestre_num = semestre_num    #Type int
        self.ativo = ativo                  #Type bool
        self.materias = [] # Lista que guardará as matérias deste semestre

    @property
    def ano(self):
        return self._ano
    @ano.setter
    def ano(self, valor):
        if not valor.strip():
            raise ValueError("CLASSE:Semestre.py//ano não pode ser vazio.")
        elif not valor.isdigit():
            raise ValueError("CLASSE:Semestre.py//ano tem de ser inteiro.")
        self._ano = int(valor.strip())
    
    @property
    def semestre_num(self):
        return self._semestre_num
    @semestre_num.setter
    def semestre_num(self, valor):
        if not valor.strip():
            raise ValueError("CLASSE:Semestre.py//semestre_num não pode ser vazio.")
        elif not valor.isdigit():
            raise ValueError("CLASSE:Semestre.py//semestre_num tem de ser inteiro.")
        self._semestre_num = int(valor.strip())

    @property
    def ativo(self):
        return self._ativo
    @ativo.setter
    def ativo(self, valor):
        if valor is None or (isinstance(valor, str) and not valor.strip()):
            raise ValueError("CLASSE:Semestre.py//ativo não pode ser vazio.")
        elif valor == "True":
            self._ativo = True
        elif valor == "False":
            self._ativo = False
        else:
            raise ValueError("CLASSE:Semestre.py//ativo tem de True ou False.")
        

    def adicionar_materia(self, materia) -> None:
        self.materias.append(materia)
        print(f"» Matéria '{materia.titulo}' adicionada ao {self.titulo}.")

    def retirar_materia(self, materia) -> None:
        if materia in self.materias:
            self.materias.remove(materia)
            print(f"» Matéria '{materia.titulo}' removida do {self.titulo}.")

    def criar(self, dados: dict) -> None:
        print(f"Ações de criação executadas para o Semestre: {self.titulo}")

    def editar(self, dados: dict) -> None:
        # Se a chave existir no dicionário, nós atualizamos o atributo!
        if "titulo" in dados: self.titulo = dados["titulo"]
        if "descricao" in dados: self.descricao = dados["descricao"]
        if "ano" in dados: self.ano = dados["ano"]
        if "semestre" in dados: self.semestre_num = dados["semestre"]
        if "ativo" in dados: self.ativo = dados["ativo"]
        print(f"» Semestre ID {self.id} editado com sucesso!")

    def deletar(self) -> None:
        self.materias.clear() # Limpa as matérias vinculadas
        print(f"» Semestre '{self.titulo}' foi deletado do sistema.")

    def criar_dependente(self, dict_incompleto, repo: Repositorio):
        nova_id_materia = repo.criar_materia(dict_incompleto)
        materia_dict = dict_incompleto
        materia_dict['id_materia'] = nova_id_materia
        materia_instanciado = Materia(
                id=materia_dict['id_materia'],
                titulo=materia_dict['titulo'],
                descricao=materia_dict['descricao'],
                professor=materia_dict['professor'],
                sala=materia_dict['sala'],
                horarios=materia_dict['horario']
            )
        return materia_instanciado