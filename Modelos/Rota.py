"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

from Visuais.VisualizadorAbstrato import VisualizadorAbstrato
from Controles.ControladorAbstrato import ControladorAbstrato
from typing import Dict
import flet as ft

class Rota:
    def __init__(self, primeiro_visualizador: VisualizadorAbstrato, 
                 primeiro_controlador: ControladorAbstrato, 
                 todos_visualizadores: Dict[str, VisualizadorAbstrato], 
                 todos_controladores: Dict[str, ControladorAbstrato]):
        self._atual_visualizador = primeiro_visualizador
        self._atual_controlador = primeiro_controlador
        self._lista_visualizadores = todos_visualizadores
        self._lista_controladores = todos_controladores
        self.page = None
    
    def set_page(self, page: ft.Page):
        self.page = page

    def maquina_de_estado(self, input_cliente: str):
        comando = input_cliente
        estado_atual = self._atual_visualizador.nome_da_pagina()
        
        if estado_atual == "pagina_inicial":
            if comando == "1":
                return "pagina_cadastro"
            elif comando == "2":
                return "pagina_login"
        
        elif estado_atual == "pagina_login":
            if comando == "0":
                return "pagina_inicial"
            elif comando == "1":
                return "pagina_entrada"
        
        elif estado_atual == "pagina_cadastro":
            if comando == "0":
                return "pagina_inicial"
            elif comando == "1":
                return "pagina_inicial"
        
        elif estado_atual == "pagina_entrada":
            if comando == "0":
                return "pagina_inicial"
            elif comando == "1" :
                return "pagina_todos_semestres"
            elif comando == "2":
                return "pagina_todos_eventos"
            
        elif estado_atual == "pagina_todos_semestres":
            if comando == "0":
                return "pagina_entrada"
            elif comando == "1":
                return "pagina_especifico_semestre"
        
        elif estado_atual == "pagina_todos_eventos":
            if comando == "0":
                return "pagina_entrada"
            elif comando == "1" :
                return "pagina_especifico_evento"
        
        elif estado_atual == "pagina_especifico_evento":
            if comando == "0":
                return "pagina_todos_eventos"
        
        elif estado_atual == "pagina_especifico_semestre":
            if comando == "0":
                return "pagina_todos_semestres"
            elif comando == "1":
                return "pagina_materia"
        
        elif estado_atual == "pagina_materia":
            if comando == "0":
                return "pagina_especifico_semestre"
            elif comando == "1":
                return "pagina_prova"
            elif comando == "2":
                return "pagina_trabalho"
            
        elif estado_atual == "pagina_prova":
            if comando == "0":
                return "pagina_materia"
        
        elif estado_atual == "pagina_trabalho":
            if comando == "0":
                return "pagina_materia"
        
        return None
    
    def atualizar_estado(self, comando: str):
        proxima_pagina = self.maquina_de_estado(comando)
        if proxima_pagina and proxima_pagina in self._lista_visualizadores:
            self._atual_visualizador = self._lista_visualizadores[proxima_pagina]
            self._atual_controlador = self._lista_controladores[proxima_pagina]
            if self.page:
                self._atual_visualizador.mostrar(self.page)

