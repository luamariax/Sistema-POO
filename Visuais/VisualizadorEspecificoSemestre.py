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
        self.lista_materias = []
        self.titulo_semestre = "Carregando..."
        self.page = None

    @property
    def controlador(self):
        return self._controlador

    @controlador.setter
    def controlador(self, controle):
        if not isinstance(controle, ControladorAbstrato):
            raise TypeError("Objeto não é do tipo Controlador.")
        self._controlador = controle

    def nome_da_pagina(self) -> str:
        return "pagina_especifico_semestre"

    def construir(self):
        # CABEÇALHO
        botao_voltar = ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=lambda e: self._on_click(e, "0"))
        titulo = ft.Text(f"📚 {self.titulo_semestre}", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
        cabecalho = ft.Row([botao_voltar, titulo])

        if not self.lista_materias:
            coluna_materias = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.MENU_BOOK, size=40, color=ft.Colors.ORANGE_400),
                    ft.Text("Nenhuma matéria cadastrada.", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("Deseja cadastrar uma nova disciplina?", size=14)
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                alignment=ft.alignment.center,
                padding=30
            )
        else:
            lista_cards = []
            for i, mat in enumerate(self.lista_materias):
                card = ft.Container(
                    content=ft.Row([
                        ft.Column([
                            ft.Text(f"{mat['titulo']}", size=16, weight=ft.FontWeight.BOLD),
                            ft.Text(f"Prof: {mat['professor']} | Sala: {mat['sala']}", size=14),
                        ], expand=True),
                        ft.ElevatedButton("Abrir", bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE, 
                                         on_click=lambda e, pos=i: self._on_click(e, f"1-{pos}"))
                    ]),
                    padding=15, bgcolor=ft.Colors.BLUE_50, border_radius=8
                )
                lista_cards.append(card)
            coluna_materias = ft.Column(lista_cards)

        # ROLAGEM E CONSTRUÇÃO FINAL
        return ft.Container(
            content=ft.Column([
                cabecalho,
                ft.Divider(),
                coluna_materias,
                ft.Divider(),
                # Aqui você pode adicionar o botão de "Criar Nova Matéria"
                ft.Row([ft.ElevatedButton("Adicionar Matéria", icon=ft.Icons.ADD)], alignment=ft.MainAxisAlignment.CENTER)
            ], scroll=ft.ScrollMode.AUTO),
            expand=True,
            padding=20
        )

    def _on_click(self, e, comando):
        if self.controlador:
            self.controlador.processar_acao(comando)
    
    def mostrar(self, page: ft.Page):
        self.page = page
        if self.controlador and hasattr(self.controlador, 'carregar_dados_para_tela'):
            self.controlador.carregar_dados_para_tela()
        page.clean()
        page.add(self.construir())
        page.update()