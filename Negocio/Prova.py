from datetime import date
from .AtividadeAvaliativa import AtividadeAvaliativa

class Prova(AtividadeAvaliativa):
    def __init__(self, id: str, titulo: str, valorAtividade: float, dia: date, conteudo: str, duracao: int):
        super().__init__(id, titulo, valorAtividade)
        self.dia = dia
        self.conteudo = conteudo
        self.duracao = duracao

    def adicionar_nota(self, nota: float) -> None:
        if not isinstance(nota, (int, float)):
            raise ValueError("A nota deve ser um número.")
        
        if nota < 0 or nota > self.valorAtividade:
            raise ValueError(f"A nota tem de estar entre 0 e {self.valorAtividade}!")
        
        self.notaObtida = float(nota)
        print(f"Nota {self.notaObtida} adicionada a '{self.titulo}'.")