"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

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
"""
import flet as ft
from .VisualizadorAbstrato import VisualizadorAbstrato
from Controles.ControladorAbstrato import ControladorAbstrato

class VisualizadorMateria(VisualizadorAbstrato):
    def __init__(self):
        self._controlador = None
        self.titulo_materia = "Carregando..."
        self.professor = "Carregando..."
        self.sala = "Carregando..."
        self.horarios = "Carregando..."

    @property
    def controlador(self):
        return self._controlador
    
    @controlador.setter
    def controlador(self, controle):
        if not isinstance(controle, ControladorAbstrato):
            raise TypeError("Objeto não é do tipo Controlador.")
        self._controlador = controle

    def nome_da_pagina(self) -> str:
        return "pagina_materia"

    def construir(self):
        # Cabeçalho
        botao_voltar = ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=lambda e: self._on_click(e, "0"))
        titulo = ft.Text(f"📘 {self.titulo_materia}", size=28, weight=ft.FontWeight.BOLD)

        
        # Cartão de Informações
        info_card = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.ListTile(leading=ft.Icon(ft.Icons.PERSON), title=ft.Text("Professor"), subtitle=ft.Text(self.professor)),
                    ft.ListTile(leading=ft.Icon(ft.Icons.ROOM), title=ft.Text("Sala"), subtitle=ft.Text(self.sala)),
                    ft.ListTile(leading=ft.Icon(ft.Icons.SCHEDULE), title=ft.Text("Horários"), subtitle=ft.Text(self.horarios)),
                ]),
                padding=10
            )
        )

        return ft.Container(
            content=ft.Column([
                ft.Row([botao_voltar, titulo]),
                ft.Divider(),
                info_card,
                ft.Row([
                    ft.ElevatedButton("Ver Provas", icon=ft.Icons.EDIT_DOCUMENT, on_click=lambda e: self._on_click(e, "1")),
                    ft.ElevatedButton("Ver Trabalhos", icon=ft.Icons.WORK, on_click=lambda e: self._on_click(e, "2")),
                ], alignment=ft.MainAxisAlignment.CENTER)
            ], scroll=ft.ScrollMode.AUTO),
            padding=20
        )

    def _on_click(self, e, comando):
        if self.controlador:
            self.controlador.processar_acao(comando)

    def mostrar(self, page: ft.Page):
        self.page = page # Armazene a página
        if self.controlador and hasattr(self.controlador, 'carregar_dados_para_tela'):
            self.controlador.carregar_dados_para_tela()
        
        page.clean()
        page.add(self.construir())
        page.update()