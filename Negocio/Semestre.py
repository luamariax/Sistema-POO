class Semestre(Objeto):
    def __init__(self, id: int, titulo: str, descricao: str, ano: int, semestre_num: int, ativo: bool):
        super().__init__(id, titulo, descricao)
        
        self.ano = ano
        self.semestre_num = semestre_num
        self.ativo = ativo
        self.materias = [] # Lista que guardará as matérias deste semestre

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