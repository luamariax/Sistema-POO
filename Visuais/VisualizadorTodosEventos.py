"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

import flet as ft
from .VisualizadorAbstrato import VisualizadorAbstrato
#versão passada
class VisualizadorTodosEventos(VisualizadorAbstrato):
    def __init__(self):
        self.controlador = None
        self.page = None

        self.lista_dict_eventos = None


    def nome_da_pagina(self) -> str:
        return "pagina_todos_eventos"

    def construir(self):
        """
        Vai chamar o controlador para retornar uma lista de dicionários
        somente com os dados titulo, data_inicio e data_fim
        """
        self.lista_dict_eventos = self.controlador.dar_dados()

        # ==========================================
        # 1. CABEÇALHO
        # ==========================================
        botao_voltar = ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            icon_color=ft.Colors.BLUE_900,
            on_click=lambda e: self._on_click(e, "0")
        )
        titulo_com_botao = ft.Row([
            botao_voltar,
            ft.Text(f"TODOS OS ENVENTOS CADASTRADOS", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
        ])
        info_materia = ft.Column([
            titulo_com_botao,
            ft.Container(height=10),
        ], padding=ft.padding.only(left=40))

        # ---------------------------------
        # Cabeçalho da tabela
        cabecalho = ft.Row(
            controls=[
                ft.Container(ft.Text("Título", weight=ft.FontWeight.BOLD, size=16), expand=2),
                ft.Container(ft.Text("Data Início", weight=ft.FontWeight.BOLD, size=16), expand=1),
                ft.Container(ft.Text("Data Fim", weight=ft.FontWeight.BOLD, size=16), expand=1),
            ],
            spacing=10,
        )

        linhas = []
        for idx, item in enumerate(self.lista_dict_eventos):
            # Cada linha é um Container clicável
            linha = ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Container(ft.Text(item.get("titulo", "")), expand=2),
                        ft.Container(ft.Text(item.get("data_inicio", "")), expand=1),
                        ft.Container(ft.Text(item.get("data_fim", "")), expand=1),
                    ],
                    spacing=10,
                ),
                padding=10,
                border=ft.border.all(1, ft.colors.GREY_400),
                border_radius=5,
                on_click=lambda e, pos=idx: self._on_linha_clicada(e, pos),
                ink=True,  # efeito visual de clique
            )
            linhas.append(linha)

        return ft.Column(controls= titulo_com_botao + [cabecalho] + linhas, spacing=5)
    
    def _on_linha_clicada(self, e, posicao: int):
        """
        Gera o comando e chama o método _on_click.
        """
        comando = f"1-{posicao}"
        self._on_click(e, comando)
    
    def _on_click(self, e, comando):
        if hasattr(self, 'controlador'):
            self.controlador.processar_acao(comando)
    
    def mostrar(self, page: ft.Page):
        page.clean()
        page.add(self.construir())
