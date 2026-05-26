from datetime import datetime
from .Objeto import Objeto

class Evento(Objeto):
    def __init__(self, id: int, titulo: str, descricao: str, dataInicio: datetime, dataFim: datetime):
        super().__init__(id, titulo, descricao)
        self.validar_datas(dataInicio, dataFim)
        self.dataInicio = dataInicio
        self.dataFim = dataFim

    def validar_datas(self, dataInicio: datetime, dataFim: datetime):
        if not isinstance(dataInicio, datetime) or not isinstance(dataFim, datetime):
            raise ValueError("As datas devem ser do tipo datetime.")
        if dataInicio >= dataFim:
            raise ValueError("A data de início deve ser anterior à data de fim.")
        
    def duracao(self) -> int:
        return (self.dataFim - self.dataInicio).days
    
