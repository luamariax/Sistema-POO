from datetime import date
from .AtividadeAvaliativa import AtividadeAvaliativa
from datetime import datetime

class Prova(AtividadeAvaliativa):
    def __init__(self, id: str, titulo: str, valorAtividade: float, dia: date, conteudo: str, sala: str, duracao: int):
        super().__init__(id, titulo, valorAtividade)
        self.dia = dia              #Type: date
        self.conteudo = conteudo    #Type: str
        self.sala = sala            #Type: str
        self.duracao = duracao      #Type: int

    @property
    def dia(self):
        return self._dia
    @dia.setter
    def dia(self, valor):
        if not valor.strip():
            raise ValueError("CLASSE:Prova.py//dia não pode ser vazio.")
        self._dia = datetime.strptime(valor.strip(), formato="%Y-%m-%d") 
    
    @property
    def conteudo(self):
        return self._conteudo
    @conteudo.setter
    def conteudo(self, valor):
        if not valor.strip():
            raise ValueError("CLASSE:Prova.py//conteudo não pode ser vazio.")
        self._conteudo = valor.strip()
    
    @property
    def duracao(self):
        return self._duracao
    @duracao.setter
    def duracao(self, valor):
        if not valor.strip():
            raise ValueError("CLASSE:Prova.py//duracao não pode ser vazio.")
        elif not valor.isdigit():
            raise ValueError("CLASSE:Prova.py//duracao tem de ser um inteiro.")
        self._duracao = int(valor.strip())

    @property
    def sala(self):
        return self._sala
    @sala.setter
    def sala(self, valor):
        if not valor.strip():
            raise ValueError("CLASSE:Prova.py//sala não pode ser vazio.")
        self._sala = valor.strip()

    def adicionar_nota(self, nota: float) -> None:
        if not isinstance(nota, (int, float)):
            raise ValueError("A nota deve ser um número.")
        
        if nota < 0 or nota > self.valorAtividade:
            raise ValueError(f"A nota tem de estar entre 0 e {self.valorAtividade}!")
        
        self._notaObtida = float(nota)
        print(f"Nota {self.notaObtida} adicionada a '{self.titulo}'.")