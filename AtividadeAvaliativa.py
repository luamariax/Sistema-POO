from abc import ABC, abstractmethod

class AtividadeAvaliativa(ABC):
    def __init__(self, id: str, titulo: str, valorAtividade: float):
        self.validar_atributos(id, titulo, valorAtividade) 
        
        self.id = id
        self.titulo = titulo
        self.valorAtividade = valorAtividade
        
        # 3. A nota obtida na prova só será preenchida quando o usuário saber a nota
        self.notaObtida = None

    def validar_atributos(self, id: str, titulo: str, valorAtividade: float):     
        if not isinstance(id, str) or not id.strip():
            raise ValueError("O ID deve ser uma string e não pode estar vazio.")
        if not isinstance(titulo, str) or not titulo.strip():
            raise ValueError("O título deve ser uma string e não pode estar vazio.")            
        if not isinstance(valorAtividade, (int, float)) or valorAtividade <= 0:
            raise ValueError("O valor da atividade deve ser um número positivo.")

    @abstractmethod
    def adicionar_nota(self, nota: float) -> None:
        pass
 