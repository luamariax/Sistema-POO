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
        titulo = ft.Text(
            "Menu Principal",
            size=80,
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER,
        )

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

        # Coluna para os botões (centralizada)
        botoes_coluna = ft.Column(
            [botao_login, botao_cadastro],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        )

        # Coluna principal com título e botões (tudo centralizado)
        coluna_principal = ft.Column(
            [titulo, botoes_coluna],
            spacing=30,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True,  # para ocupar altura total e centralizar verticalmente
        )

        return coluna_principal
    
    def _on_click(self, e, comando):
        if hasattr(self, 'controlador'):
            self.controlador.processar_acao(comando)
    
    def mostrar(self, page: ft.Page):
        page.clean()
        page.add(self.construir())


