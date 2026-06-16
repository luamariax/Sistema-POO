"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

import flet as ft
from .VisualizadorAbstrato import VisualizadorAbstrato
from Controles.ControladorAbstrato import ControladorAbstrato


class VisualizadorProva(VisualizadorAbstrato):
    def __init__(self):
        self._controlador = None
        self.page = None

        self.titulo = "Carregando..."
        self.dia = ""
        self.conteudo = ""
        self.sala = ""
        self.duracao = ""
        self.valor_nota = ""
        self.nota_obtida = ""

    @property
    def controlador(self):
        return self._controlador

    @controlador.setter
    def controlador(self, controle):
        if not isinstance(controle, ControladorAbstrato):
            raise TypeError("Objeto não é do tipo Controlador.")
        self._controlador = controle

    def nome_da_pagina(self) -> str:
        return "pagina_prova"

    def construir(self):
        botao_voltar = ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            on_click=lambda e: self._on_click(e, "0")
        )
        titulo = ft.Text(f"📝 {self.titulo}", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_800)
        cabecalho = ft.Row([botao_voltar, titulo])

        nota_str = str(self.nota_obtida).strip()
        nota_display = nota_str if nota_str not in ["", "None", "nan"] else "Sem nota"

        info_card = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Icon(ft.Icons.CALENDAR_TODAY, color=ft.Colors.GREEN_600),
                        ft.Text(f"Data: {self.dia}", size=16, weight=ft.FontWeight.BOLD),
                    ]),
                    ft.Row([
                        ft.Icon(ft.Icons.ROOM, color=ft.Colors.GREEN_600),
                        ft.Text(f"Sala: {self.sala}", size=16),
                    ]),
                    ft.Row([
                        ft.Icon(ft.Icons.TIMER, color=ft.Colors.GREEN_600),
                        ft.Text(f"Duração: {self.duracao} min", size=16),
                    ]),
                    ft.Divider(color=ft.Colors.GREY_200),
                    ft.Text(f"Conteúdo: {self.conteudo}", size=14, color=ft.Colors.GREY_700),
                    ft.Divider(color=ft.Colors.GREY_200),
                    ft.Row([
                        ft.Container(
                            content=ft.Row([
                                ft.Icon(ft.Icons.STAR_OUTLINE, color=ft.Colors.WHITE),
                                ft.Text(f"Valor: {self.valor_nota}", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
                            ]),
                            bgcolor=ft.Colors.GREEN_700,
                            padding=10,
                            border_radius=8,
                        ),
                        ft.Container(
                            content=ft.Row([
                                ft.Icon(ft.Icons.STAR_ROUNDED, color=ft.Colors.WHITE),
                                ft.Text(f"Nota: {nota_display}", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
                            ]),
                            bgcolor=ft.Colors.GREEN_900,
                            padding=10,
                            border_radius=8,
                        ),
                    ], spacing=10),
                ], spacing=10),
                padding=20
            )
        )

        return ft.Container(
            content=ft.Column([
                cabecalho,
                ft.Divider(),
                info_card,
            ], scroll=ft.ScrollMode.AUTO),
            expand=True,
            padding=20
        )

    def _on_click(self, e, comando, dados=None):
        if self.controlador:
            self.controlador.processar_acao(comando, dados)

    def mostrar(self, page: ft.Page):
        self.page = page
        if self.controlador and hasattr(self.controlador, 'carregar_dados_para_tela'):
            self.controlador.carregar_dados_para_tela()
        page.clean()
        page.add(self.construir())
        page.update()
