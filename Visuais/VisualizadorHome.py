"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

"""
import flet as ft
from .VisualizadorAbstrato import VisualizadorAbstrato

class VisualizadorHome(VisualizadorAbstrato):
    def __init__(self):
        self.container = ft.Container()
    
    def nome_da_pagina(self) -> str:
        return "pagina_inicial"
    
    def construir(self):
        return ft.Column([
            ft.Text("Página Inicial - Menu Principal", size=30, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Escolha uma opção:"),
            ft.ElevatedButton("Ir para Página Login", on_click=lambda e: self._on_click(e, "2")),
            ft.ElevatedButton("Ir para Página Cadastro", on_click=lambda e: self._on_click(e, "1")),
        ])
    
    def _on_click(self, e, comando):
        if hasattr(self, 'controlador'):
            self.controlador.processar_acao(comando)
    
    def mostrar(self, page: ft.Page):
        page.clean()
        page.add(self.construir())
"""

import flet as ft
from .VisualizadorAbstrato import VisualizadorAbstrato

class VisualizadorHome(VisualizadorAbstrato):
    def __init__(self):
        self.container = ft.Container()
    
    def nome_da_pagina(self) -> str:
        return "pagina_inicial"
    
    def construir(self):
        # Título grande e centralizado
        titulo = ft.Row(ft.Text(
            "Menu Principal",
            size=80,
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER,
        ))

        # Botões
        botao_login = ft.ElevatedButton(
            "Ir para Página Login",
            on_click=lambda e: self._on_click(e, "2"),
            width=250,  # largura opcional para uniformidade
        )
        botao_cadastro = ft.ElevatedButton(
            "Ir para Página Cadastro",
            on_click=lambda e: self._on_click(e, "1"),
            width=250,
        )

        coluna_principal = ft.Column(
            controls=[titulo, botao_login, botao_cadastro],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # centraliza horizontalmente
            alignment=ft.MainAxisAlignment.CENTER,              # centraliza verticalmente
            spacing=20,
            expand=True,  # ocupa toda a altura disponível
        )

        return coluna_principal
    
    def _on_click(self, e, comando):
        if hasattr(self, 'controlador'):
            self.controlador.processar_acao(comando)
    
    def mostrar(self, page: ft.Page):
        page.clean()
        page.add(self.construir())


