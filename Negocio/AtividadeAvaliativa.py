from abc import ABC, abstractmethod

class AtividadeAvaliativa(ABC):
    def __init__(self, id: str, titulo: str, valorAtividade: float, notaObtida):
        self.validar_atributos(id, titulo, valorAtividade, notaObtida) 
        
        self.id = id                            #Type str 
        self.titulo = titulo                    #Type str
        self.valorAtividade = valorAtividade    #Type float
        self.notaObtida = notaObtida            #Type float
        

    def validar_atributos(self, id: str, titulo: str, valorAtividade: float, notaObtida):     
        if not isinstance(id, str) or not id.strip():
            raise ValueError("O ID deve ser uma string e não pode estar vazio.")
        if not isinstance(titulo, str) or not titulo.strip():
            raise ValueError("O título deve ser uma string e não pode estar vazio.")            
        

    @abstractmethod
    def adicionar_nota(self, nota: float) -> None:
        pass
 