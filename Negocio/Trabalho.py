from datetime import date
from .AtividadeAvaliativa import AtividadeAvaliativa

class Trabalho(AtividadeAvaliativa):
    def __init__(self, id: str, titulo: str, valorAtividade: float, dataEntrega: date, descricaoTarefa: str, grupo: str):
        super().__init__(id, titulo, valorAtividade)
        self.dataEntrega = dataEntrega
        self.descricaoTarefa = descricaoTarefa
        self.grupo = grupo
        
        # O trabalho está pendente na lista do aluno
        self.entregue = False 

    def marcar_como_entregue(self):
        self.entregue = True
        print(f"Trabalho '{self.titulo}' marcado como concluído e entregue!")

    def adicionar_nota(self, nota: float) -> None:
        if not isinstance(nota, (int, float)):
            raise ValueError("A nota deve ser um número.")
            
        if nota < 0 or nota > self.valorAtividade:
            raise ValueError(f"A nota deve estar entre 0 e {self.valorAtividade}.")
        
        # Se o usuário está adicionando uma nota, assumimos que o trabalho já foi entregue
        self.entregue = True 
        
        self.notaObtida = float(nota)