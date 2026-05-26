from .Objeto import Objeto

class Materia(Objeto):
    def __init__(self, id: int, titulo: str, descricao: str, professor: str, horarios: str):
        super().__init__(id, titulo, descricao)
        
        self.professor = professor
        self.horarios = horarios
        self.avaliacoes = [] # Lista de Atividades Avaliativas [cite: 52]

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