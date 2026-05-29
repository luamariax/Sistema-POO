"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

"""
import flet as ft
from .VisualizadorAbstrato import VisualizadorAbstrato

class VisualizadorEspecificoSemestre(VisualizadorAbstrato):
    def nome_da_pagina(self) -> str:
        return "pagina_especifico_semestre"
    
    def construir(self):
        return ft.Column([
            ft.Text("Página deste Semestre Específico", size=30, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Lista de Materias desse semestre"),
            ft.ElevatedButton("Voltar para Página Todos Semestres", on_click=lambda e: self._on_click(e, "0")),
            ft.ElevatedButton("Ir para Página Materia", on_click=lambda e: self._on_click(e, "1")),
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
from Controles.ControladorAbstrato import ControladorAbstrato

class VisualizadorEspecificoSemestre(VisualizadorAbstrato):
    def __init__(self):
        self._controlador = None
        self.titulo_semestre = "A carregar..."
        self.lista_materias = []

    @property
    def controlador(self):
        return self._controlador
    
    @controlador.setter
    def controlador(self, controle):
        # Aqui garantimos que o controlador está ligado
        self._controlador = controle

    def nome_da_pagina(self) -> str:
        return "pagina_especifico_semestre"
    
    def construir(self):
        # Botão de voltar (comando "0" volta para pagina_todos_semestres)
        botao_voltar = ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            icon_color=ft.Colors.BLUE_900,
            on_click=lambda e: self._on_click(e, "0")
        )

        cabecalho = ft.Row([
            botao_voltar,
            ft.Text(f"📅 Semestre {self.titulo_semestre}", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
        ])

        coluna_materias = ft.Column()
        for materia in self.lista_materias:
            cartao = ft.Container(
                content=ft.Row([
                    ft.Column([
                        ft.Text(f"📚 {materia['nome']}", size=16, weight=ft.FontWeight.BOLD),
                        ft.Text(f"👨‍🏫 {materia['prof']}", size=14),
                        ft.Text(f"⏰ {materia['horario']}", size=14),
                    ], expand=True),
                    ft.ElevatedButton("Acessar", bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE, 
                                     on_click=lambda e: self._on_click(e, "1"))
                ]),
                padding=15, bgcolor=ft.Colors.BLUE_50, border_radius=8
            )
            coluna_materias.controls.extend([cartao, ft.Divider(height=10, color=ft.Colors.TRANSPARENT)])

        return ft.Column([cabecalho, coluna_materias])
    
    def _on_click(self, e, comando):
        if self.controlador:
            self.controlador.processar_acao(comando)
    
    def mostrar(self, page: ft.Page):
        # A MÁGICA: Pedir os dados ao controlador antes de desenhar
        if self.controlador:
            # Puxamos os dados da Ana (U001) no semestre 2026-1 (S001)
            self.controlador.carregar_dados_para_tela("U001", "S001", self)
            
        page.clean()
        page.add(self.construir())
        page.update()