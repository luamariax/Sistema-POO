"""
aqui será o main do app
"""
"""view"""

from Visuais.VisualizadorAtividade import VisualizadorAtividade
from Visuais.VisualizadorCadastro import VisualizadorCadastro
from Visuais.VisualizadorEntrada import VisualizadorEntrada
from Visuais.VisualizadorEspecificoEvento import VisualizadorEspecificoEvento
from Visuais.VisualizadorEspecificoSemestre import VisualizadorEspecificoSemestre
from Visuais.VisualizadorHome import VisualizadorHome
from Visuais.VisualizadorLogin import VisualizadorLogin
from Visuais.VisualizadorMateria import VisualizadorMateria
from Visuais.VisualizadorTodosEventos import VisualizadorTodosEventos
from Visuais.VisualizadorTodosSemestres import VisualizadorTodosSemestres
"""controler"""

from Controles.ControladorAtividade import ControladorAtividade
from Controles.ControladorCadastro import ControladorCadastro
from Controles.ControladorEntrada import ControladorEntrada
from Controles.ControladorEspecificoEvento import ControladorEspecificoEvento
from Controles.ControladorEspecificoSemestre import ControladorEspecificoSemestre
from Controles.ControladorHome import ControladorHome
from Controles.ControladorLogin import ControladorLogin
from Controles.ControladorMateria import ControladorMateria
from Controles.ControladorTodosEventos import ControladorTodosEventos
from Controles.ControladorTodosSemestres import ControladorTodosSemestres
from .modelos.Rota import Rota
"""model"""
from Servicos.ServicoUser import ServicoUser
from Servicos.ServicoObjeto import ServicoObjeto
from Servicos.ServicoAtividade import ServicoAtividade

from typing import Dict, Type
import flet as ft

def main(page: ft.Page):
    page.title = "App com Arquitetura MVC Adaptada"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.window_width = 400
    page.window_height = 600
    
    # Criar instâncias dos visualizadores
    visual_atividade = VisualizadorAtividade
    visual_cadastro = VisualizadorCadastro
    visual_entrada = VisualizadorEntrada
    visual_especifico_evento = VisualizadorEspecificoEvento
    visual_especifico_semestre = VisualizadorEspecificoSemestre
    visual_home = VisualizadorHome
    visual_login = VisualizadorLogin
    visual_materia = VisualizadorMateria
    visual_todos_eventos = VisualizadorTodosEventos
    visual_todos_semestres = VisualizadorTodosSemestres
    
    # Criar dicionários
    todos_visualizadores = {
        "pagina_inicial": visual_home,
        "pagina_login": visual_login,
        "pagina_cadastro": visual_cadastro,
        "pagina_entrada": visual_entrada,
        "pagina_todos_eventos": visual_todos_eventos,
        "pagina_todos_semestres": visual_todos_semestres,
        "pagina_especifico_evento": visual_especifico_evento,
        "pagina_especifico_semestre": visual_especifico_semestre,
        "pagina_materia": visual_materia,
        "pagina_atividade_avaliativa": visual_atividade
    }
    
    # Criar instâncias dos controladores
    controle_atividade = ControladorAtividade(rota)
    controle_cadastro = ControladorCadastro(rota)
    controle_entrada = ControladorEntrada(rota)
    controle_especifico_evento = ControladorEspecificoEvento(rota)
    controle_especifico_semestre = ControladorEspecificoSemestre(rota)
    controle_home = ControladorHome(rota)
    controle_login = ControladorLogin(rota)
    controle_materia = ControladorMateria(rota)
    controle_todos_eventos = ControladorTodosEventos(rota)
    controle_todos_semestres = ControladorTodosSemestres(rota)
    
    # Atualizar dicionário de controladores
    todos_controladores = {
        "pagina_inicial": controle_home,
        "pagina_login": controle_login,
        "pagina_cadastro": controle_cadastro,
        "pagina_entrada": controle_entrada,
        "pagina_todos_eventos": controle_todos_eventos,
        "pagina_todos_semestres": controle_todos_semestres,
        "pagina_especifico_evento": controle_especifico_evento,
        "pagina_especifico_semestre": controle_especifico_semestre,
        "pagina_materia": controle_materia,
        "pagina_atividade_avaliativa": controle_atividade
    }

    # Criar Rota
    rota = Rota(visual_home, controle_home, todos_visualizadores, todos_controladores)
    
    # Associar controladores aos visualizadores
    visual_atividade.controlador = controle_atividade
    visual_cadastro.controlador = controle_cadastro
    visual_entrada.controlador = controle_entrada
    visual_especifico_evento.controlador = controle_especifico_evento
    visual_especifico_semestre.controlador = controle_especifico_evento
    visual_home.controlador = controle_home
    visual_login.controlador = controle_login
    visual_materia.controlador = controle_materia
    visual_todos_eventos.controlador = controle_todos_eventos
    visual_todos_semestres.controlador = controle_todos_semestres
    
    # Configurar página na rota
    rota.set_page(page)
    
    # Mostrar página inicial
    visual_home.mostrar(page)

# Iniciar o app
if __name__ == "__main__":
    ft.app(target=main)