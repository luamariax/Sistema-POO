"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

import flet as ft
from .VisualizadorAbstrato import VisualizadorAbstrato


class VisualizadorCadastro(VisualizadorAbstrato):
    def __init__(self):
        self.container = ft.Container()
    
    def nome_da_pagina(self) -> str:
        return "pagina_cadastro"
    
    def construir(self):
        return ft.Column([
            ft.Text("Página de Cadastro ", size=30, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Você está na página de cadastro"),
            ft.ElevatedButton("Voltar para Página Inicial", on_click=lambda e: self._on_click(e, "0")),
        ])
    
    def _on_click(self, e, comando):
        if hasattr(self, 'controlador'):
            self.controlador.processar_acao(comando)
    
    def mostrar(self, page: ft.Page):
        page.clean()
        page.add(self.construir())
