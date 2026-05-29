from .Objeto import Objeto

class Materia(Objeto):
    def __init__(self, id: int, titulo: str, descricao: str, professor: str, sala: str, horarios: str):
        super().__init__(id, titulo, descricao)
        
        self.professor = professor      #Type: str
        self.sala = sala                #Type: str
        self.horarios = horarios        #Type: str
        self.avaliacoes = [] # Lista de Atividades Avaliativas [cite: 52]

    @property
    def professor(self):
        return self._professor
    @professor.setter
    def professor(self, valor):
        if not valor.strip():
            raise ValueError("CLASSE:Materia.py//professor não pode ser vazio.")
        self._professor = valor.strip()
    
    @property
    def sala(self):
        return self._sala
    @sala.setter
    def sala(self, valor):
        if not valor.strip():
            raise ValueError("CLASSE:Materia.py//sala não pode ser vazio.")
        self._sala = valor.strip()

    @property
    def horarios(self):
        return self._horarios
    @horarios.setter
    def horarios(self, valor):
        if not valor.strip():
            raise ValueError("CLASSE:Materia.py//horarios não pode ser vazio.")
        self._horarios = valor.strip()

    # Métodos específicos da Matéria vindos do seu UML [cite: 53, 54]
    def adicionar_atividade(self, atividade) -> None:
        self.avaliacoes.append(atividade)

    def retirar_atividade(self, atividade) -> None:
        if atividade in self.avaliacoes:
            self.avaliacoes.remove(atividade)

    def calcular_nota(self) -> float:
        # Lógica para somar as notas das atividades avaliativas cadastradas (provas ou trabalhos)
        total = 0.0
        for av in self.avaliacoes:
            if av._nota_obtida is not None:
                total += av._nota_obtida
        return total

    def criar(self, dados: dict) -> None:
        print(f"Ações de criação executadas para a Matéria: {self.titulo}")

    def editar(self, dados: dict) -> None:
        if "titulo" in dados: self.titulo = dados["titulo"]
        if "descricao" in dados: self.descricao = dados["descricao"]
        if "professor" in dados: self.professor = dados["professor"]
        if "horarios" in dados: self.horarios = dados["horarios"]
        print(f"» Matéria ID {self.id} editada com sucesso!")

    def deletar(self) -> None:
        self.avaliacoes.clear()
        print(f"» Matéria '{self.titulo}' foi deletada do sistema.")