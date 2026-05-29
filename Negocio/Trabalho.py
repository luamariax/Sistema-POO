from datetime import date
from .AtividadeAvaliativa import AtividadeAvaliativa
from datetime import datetime

class Trabalho(AtividadeAvaliativa):
    def __init__(self, id: str, titulo: str, valorAtividade: float, dataEntrega: date, descricaoTarefa: str, grupo: str):
        super().__init__(id, titulo, valorAtividade)
        self.dataEntrega = dataEntrega
        self.descricaoTarefa = descricaoTarefa
        self.grupo = grupo
        
    @property
    def dataEntrega(self):
        return self._dataEntrega
    @dataEntrega.setter
    def dataEntrega(self, valor):
        if not valor.strip():
            raise ValueError("CLASSE:Trabalho.py//dataEntrega não pode ser vazio.")
        self._dataEntrega = datetime.strptime(valor.strip(), "%Y-%m-%d") 

    @property
    def descricaoTarefa(self):
        return self._descricaoTarefa
    @descricaoTarefa.setter
    def descricaoTarefa(self, valor):
        if not valor.strip():
            raise ValueError("CLASSE:Trabalho.py//descricaoTarefa não pode ser vazio.")
        self._descricaoTarefa = valor.strip()

    @property
    def grupo(self):
        return self._grupo
    @grupo.setter
    def grupo(self, valor):
        if not valor.strip():
            raise ValueError("CLASSE:Trabalho.py//grupo não pode ser vazio.")
        self._grupo = valor.strip()
    

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