"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

import flet as ft
from .VisualizadorAbstrato import VisualizadorAbstrato

class VisualizadorEspecificoEvento(VisualizadorAbstrato):
    def nome_da_pagina(self) -> str:
        return "pagina_especifico_evento"
    
    def construir(self):
        return ft.Column([
            ft.Text("Página deste Evento Específico", size=30, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Dados do evento"),
            ft.ElevatedButton("Voltar para Página Todos Eventos", on_click=lambda e: self._on_click(e, "0")),
        ])
    
    def _on_click(self, e, comando):
        if hasattr(self, 'controlador'):
            self.controlador.processar_acao(comando)
    
    def mostrar(self, page: ft.Page):
        page.clean()
        page.add(self.construir())
