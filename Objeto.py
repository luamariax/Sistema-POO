from ABC import ABC, abstractmethod

class Objeto(ABC):
    @abstractmethod
    def __init__(self, id: int, titulo: str, descricao: str):
        self.validar_atributos(id, titulo, descricao)
        self.id = id
        self.titulo = titulo
        self.descricao = descricao

    def validar_atributos(self, id: int, titulo: str, descricao: str):     
        if not isinstance(id, int) or id <= 0:
            raise ValueError("O ID deve ser um inteiro positivo.")
        
        if not isinstance(titulo, str) or not titulo.strip():
            raise ValueError("O título deve ser uma string não vazia.")
        
        if not isinstance(descricao, str) or not descricao.strip():
            raise ValueError("A descrição deve ser uma string não vazia.")
        
    def exibir_informacoes(self):
        print(f"ID: {self.id}")
        print(f"Título: {self.titulo}")
        print(f"Descrição: {self.descricao}")

    
    

