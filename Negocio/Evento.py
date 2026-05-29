from datetime import datetime
from .Objeto import Objeto
from datetime import datetime

class Evento(Objeto):
    def __init__(self, id: int, titulo: str, descricao: str, data_inicio: datetime, data_fim: datetime, local: str, organizador: str):
        dataInicio = datetime.strptime(data_inicio.strip(), "%Y-%m-%d")
        dataFim = datetime.strptime(data_fim.strip(), "%Y-%m-%d")
        super().__init__(id, titulo, descricao)
        self.validar_datas(dataInicio, dataFim)
        self.dataInicio = dataInicio    #Type datetime
        self.dataFim = dataFim          #Type datetime
        self.local = local              #Type str
        self.organizador = organizador  #Type str

    @property
    def local(self):
        return self._local
    @local.setter
    def local(self, valor):
        if not valor.strip():
            raise ValueError("CLASSE:Evento.py//Não pode ser vazio.")
        self._local = valor.strip()

    @property
    def organizador(self):
        return self._organizador
    @organizador.setter
    def organizador(self, valor):
        if not valor.strip():
            raise ValueError("CLASSE:Evento.py//Não pode ser vazio.")
        self._organizador = valor.strip()

    def validar_datas(self, dataInicio: datetime, dataFim: datetime):
        if not isinstance(dataInicio, datetime) or not isinstance(dataFim, datetime):
            raise ValueError("As datas devem ser do tipo datetime.")
        if dataInicio >= dataFim:
            raise ValueError("A data de início deve ser anterior à data de fim.")
        
    def duracao(self) -> int:
        return (self.dataFim - self.dataInicio).days
    
