"""
aqui será o main do app
"""
import os
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
from Visuais.VisualizadorProva import VisualizadorProva
from Visuais.VisualizadorTrabalho import VisualizadorTrabalho
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
from Controles.ControladorProva import ControladorProva
from Controles.ControladorTrabalho import ControladorTrabalho

"""servico"""
from Servicos.Servico import Servico

"""modelos"""
from Modelos.Rota import Rota
from Modelos.Repositorio import Repositorio

from typing import Dict, Type
import flet as ft

def configurar_app():
    # 1. Criar repositório e serviço
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(diretorio_atual, "Arquivo.xlsx")
    repo = Repositorio(caminho_arquivo)
    servico = Servico(repo)

    visual_atividade = VisualizadorAtividade()
    visual_cadastro = VisualizadorCadastro()
    visual_entrada = VisualizadorEntrada()
    visual_especifico_evento = VisualizadorEspecificoEvento()
    visual_especifico_semestre = VisualizadorEspecificoSemestre()
    visual_home = VisualizadorHome()
    visual_login = VisualizadorLogin()
    visual_materia = VisualizadorMateria()
    visual_todos_eventos = VisualizadorTodosEventos()
    visual_todos_semestres = VisualizadorTodosSemestres()
    visual_prova = VisualizadorProva()
    visual_trabalho = VisualizadorTrabalho()
    
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
        "pagina_atividade_avaliativa": visual_atividade,
        "pagina_prova": visual_prova,
        "pagina_trabalho": visual_trabalho
    }
    
    rota = Rota(visual_home, None, todos_visualizadores, {})

    # Criar instâncias dos controladores
    controle_atividade = ControladorAtividade(rota, servico,visual_atividade)
    controle_cadastro = ControladorCadastro(rota, servico, visual_cadastro)
    controle_entrada = ControladorEntrada(rota, servico, visual_entrada)
    controle_especifico_evento = ControladorEspecificoEvento(rota, servico,visual_especifico_evento)
    controle_especifico_semestre = ControladorEspecificoSemestre(rota, servico,visual_especifico_semestre)
    controle_home = ControladorHome(rota, servico,visual_home)
    controle_login = ControladorLogin(rota, servico, visual_login)
    controle_materia = ControladorMateria(rota, servico,visual_materia)
    controle_todos_eventos = ControladorTodosEventos(rota, servico,visual_todos_eventos)
    controle_todos_semestres = ControladorTodosSemestres(rota, servico,visual_todos_semestres)
    controle_prova = ControladorProva(rota, servico, visual_prova)
    controle_trabalho = ControladorTrabalho(rota, servico, visual_trabalho)
    
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
        "pagina_atividade_avaliativa": controle_atividade,
        "pagina_prova": controle_prova,
        "pagina_trabalho": controle_trabalho
    }

    # Criar Rota
    rota._lista_controladores = todos_controladores
    rota._atual_controlador = controle_home
    
    # Associar controladores aos visualizadores
    visual_atividade.controlador = controle_atividade
    visual_cadastro.controlador = controle_cadastro
    visual_entrada.controlador = controle_entrada
    visual_especifico_evento.controlador = controle_especifico_evento
    visual_especifico_semestre.controlador = controle_especifico_semestre
    visual_home.controlador = controle_home
    visual_login.controlador = controle_login
    visual_materia.controlador = controle_materia
    visual_todos_eventos.controlador = controle_todos_eventos
    visual_todos_semestres.controlador = controle_todos_semestres
    visual_prova.controlador = controle_prova
    visual_trabalho.controlador = controle_trabalho
    
    return rota, visual_home

def main(page: ft.Page):
    page.title = "App com Arquitetura MVC - Múltiplos Arquivos"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.window_width = 400
    page.window_height = 600
    
    rota, pagina_inicial = configurar_app()
    
    
    # Configurar página na rota
    rota.set_page(page)
    
    # Mostrar página inicial
    pagina_inicial.mostrar(page)

# Iniciar o app
if __name__ == "__main__":
    ft.app(target=main)