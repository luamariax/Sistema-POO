"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""
"""
from .ControladorAbstrato import ControladorAbstrato

#import dos servicos
from Controles.ControladorAbstrato import ControladorAbstrato
class ControladorEspecificoSemestre(ControladorAbstrato):
    def processar_acao(self, acao: str, dados: dict = None):
        self.rota.atualizar_estado(acao)
"""

"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""
from .ControladorAbstrato import ControladorAbstrato

class ControladorEspecificoSemestre(ControladorAbstrato):
    def __init__(self, rota, repositorio):
        self.rota = rota
        self.repositorio = repositorio

    def carregar_dados_para_tela(self, id_user: str, id_semestre: str, visualizador):
        # Busca o semestre pelo ID
        semestres = self.repositorio.buscar_semestres_por_usuario(id_user)
        dados_sem = next((s for s in semestres if s['id_semestre'] == id_semestre), None)
        titulo_semestre = dados_sem['titulo'] if dados_sem else "Desconhecido"

        # Busca as matérias reais do repositório
        materias_bd = self.repositorio.buscar_materias_por_semestre_usuario(id_user, id_semestre)

        lista_formatada = []
        for m in materias_bd:
            lista_formatada.append({
                "id": m.get('id_materia'),
                "nome": m.get('titulo', 'Sem Nome'),
                "prof": m.get('professor', 'Sem Professor'),
                "horario": m.get('horario', 'Sem Horário')
            })

        # Entrega os dados ao visualizador
        visualizador.titulo_semestre = titulo_semestre
        visualizador.lista_materias = lista_formatada

    def processar_acao(self, acao: str, dados: dict = None):
        self.rota.atualizar_estado(acao)