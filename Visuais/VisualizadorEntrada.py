"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

import flet as ft
from .VisualizadorAbstrato import VisualizadorAbstrato

class VisualizadorEntrada(VisualizadorAbstrato):
    def nome_da_pagina(self) -> str:
        return "pagina_entrada"
    
    def construir(self):
        return ft.Column([
            ft.Text("Página de Entrada", size=30, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Você está na página de entrada"),
            ft.ElevatedButton("Voltar para Página Inicial", on_click=lambda e: self._on_click(e, "0")),
            ft.ElevatedButton("Ir para Página Todos Semestres", on_click=lambda e: self._on_click(e, "1")),
            ft.ElevatedButton("Ir para Página Todos Eventos", on_click=lambda e: self._on_click(e, "2")),
        ])
    
    def _on_click(self, e, comando):
        if hasattr(self, 'controlador'):
            self.controlador.processar_acao(comando)
    
    def mostrar(self, page: ft.Page):
        page.clean()
        page.add(self.construir())
