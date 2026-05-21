"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

import flet as ft
from .VisualizadorAbstrato import VisualizadorAbstrato

class VisualizadorLogin(VisualizadorAbstrato):
    def __init__(self):
        self.container = ft.Container()
    
    def nome_da_pagina(self) -> str:
        return "pagina_login"
    
    def construir(self):
        return ft.Column([
            ft.Text("Página de Login", size=30, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Processo de login"),
            ft.ElevatedButton("Voltar para Página Inicial", on_click=lambda e: self._on_click(e, "0")),
            ft.ElevatedButton("Ir para Página Entrada", on_click=lambda e: self._on_click(e, "1")),
        ])
    
    def _on_click(self, e, comando):
        if hasattr(self, 'controlador'):
            self.controlador.processar_acao(comando)
    
    def mostrar(self, page: ft.Page):
        page.clean()
        page.add(self.construir())