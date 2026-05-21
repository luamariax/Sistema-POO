"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

import flet as ft
from .VisualizadorAbstrato import VisualizadorAbstrato

class VisualizadorMateria(VisualizadorAbstrato):
    def nome_da_pagina(self) -> str:
        return "pagina_materia"
    
    def construir(self):
        return ft.Column([
            ft.Text("Página da Matéria", size=30, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Lista de Atividades Avaliativas"),
            ft.ElevatedButton("Voltar para Página Semestre Especifico", on_click=lambda e: self._on_click(e, "0")),
            ft.ElevatedButton("Ir para Página Atividade", on_click=lambda e: self._on_click(e, "1")),
        ])
    
    def _on_click(self, e, comando):
        if hasattr(self, 'controlador'):
            self.controlador.processar_acao(comando)
    
    def mostrar(self, page: ft.Page):
        page.clean()
        page.add(self.construir())
