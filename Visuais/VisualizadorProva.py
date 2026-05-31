"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

import flet as ft
from .VisualizadorAbstrato import VisualizadorAbstrato

class VisualizadorProva(VisualizadorAbstrato):
    def nome_da_pagina(self) -> str:
        return "pagina_atividade_avaliativa"
    
    def construir(self):
        return ft.Column([
            ft.Text("Página Atividade Avaliativa - PROVA", size=30, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Descrição da atividade e nota"),
            ft.ElevatedButton("Voltar para Página Matéria", on_click=lambda e: self._on_click(e, "0")),
        ])
    
    def _on_click(self, e, comando):
        if hasattr(self, 'controlador'):
            self.controlador.processar_acao(comando)
    
    def mostrar(self, page: ft.Page):
        page.clean()
        page.add(self.construir())
