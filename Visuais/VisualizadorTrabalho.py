"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

import flet as ft
from .VisualizadorAbstrato import VisualizadorAbstrato
from Controles.ControladorAbstrato import ControladorAbstrato


class VisualizadorTrabalho(VisualizadorAbstrato):
    def __init__(self):
        self._controlador = None
        self.page = None

        self.titulo = "Carregando..."
        self.data_entrega = ""
        self.descricao_tarefa = ""
        self.grupo = ""
        self.entregue = ""
        self.valor_nota = ""
        self.nota_obtida = ""

        self.exibir_form_nota = False
        self.campo_nota = ft.TextField(
            label="Nota obtida",
            input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9.]", replacement_string=""),
            width=200
        )

    @property
    def controlador(self):
        return self._controlador

    @controlador.setter
    def controlador(self, controle):
        if not isinstance(controle, ControladorAbstrato):
            raise TypeError("Objeto não é do tipo Controlador.")
        self._controlador = controle

    def nome_da_pagina(self) -> str:
        return "pagina_trabalho"

    def construir(self):
        botao_voltar = ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            on_click=lambda e: self._on_click(e, "0")
        )
        titulo = ft.Text(f"💼 {self.titulo}", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_800)
        cabecalho = ft.Row([botao_voltar, titulo])

        nota_str = str(self.nota_obtida).strip()
        nota_display = nota_str if nota_str not in ["", "None", "nan"] else "Sem nota"

        entregue_str = str(self.entregue).strip()
        ja_entregue = entregue_str == "True"
        entregue_display = "Sim" if ja_entregue else "Não"
        entregue_cor = ft.Colors.GREEN_700 if ja_entregue else ft.Colors.RED_700

        info_card = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Icon(ft.Icons.CALENDAR_TODAY, color=ft.Colors.ORANGE_600),
                        ft.Text(f"Entrega: {self.data_entrega}", size=16, weight=ft.FontWeight.BOLD),
                    ]),
                    ft.Row([
                        ft.Icon(ft.Icons.GROUP, color=ft.Colors.ORANGE_600),
                        ft.Text(f"Grupo: {self.grupo}", size=16),
                    ]),
                    ft.Row([
                        ft.Icon(ft.Icons.CHECK_CIRCLE_OUTLINE, color=entregue_cor),
                        ft.Text(f"Entregue: {entregue_display}", size=16, color=entregue_cor, weight=ft.FontWeight.BOLD),
                    ]),
                    ft.Divider(color=ft.Colors.GREY_200),
                    ft.Text(f"Descrição: {self.descricao_tarefa}", size=14, color=ft.Colors.GREY_700),
                    ft.Divider(color=ft.Colors.GREY_200),
                    ft.Row([
                        ft.Container(
                            content=ft.Row([
                                ft.Icon(ft.Icons.STAR_OUTLINE, color=ft.Colors.WHITE),
                                ft.Text(f"Valor: {self.valor_nota}", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
                            ]),
                            bgcolor=ft.Colors.ORANGE_700,
                            padding=10,
                            border_radius=8,
                        ),
                        ft.Container(
                            content=ft.Row([
                                ft.Icon(ft.Icons.STAR_ROUNDED, color=ft.Colors.WHITE),
                                ft.Text(f"Nota: {nota_display}", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
                            ]),
                            bgcolor=ft.Colors.ORANGE_900,
                            padding=10,
                            border_radius=8,
                        ),
                    ], spacing=10),
                ], spacing=10),
                padding=20
            )
        )

        if self.exibir_form_nota:
            area_acoes = ft.Container(
                content=ft.Column([
                    ft.Text("Lançar Nota", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_700),
                    ft.Row([
                        self.campo_nota,
                        ft.ElevatedButton(
                            "Salvar",
                            bgcolor=ft.Colors.ORANGE,
                            color=ft.Colors.WHITE,
                            on_click=self._salvar_nota
                        ),
                        ft.TextButton("Cancelar", on_click=self._cancelar_form),
                    ], alignment=ft.MainAxisAlignment.START)
                ]),
                padding=15,
                bgcolor=ft.Colors.ORANGE_50,
                border_radius=10
            )
        else:
            botoes = [
                ft.ElevatedButton(
                    "Lançar Nota",
                    icon=ft.Icons.EDIT,
                    bgcolor=ft.Colors.ORANGE_700,
                    color=ft.Colors.WHITE,
                    on_click=self._abrir_form_nota
                )
            ]
            if not ja_entregue:
                botoes.append(
                    ft.ElevatedButton(
                        "Marcar como Entregue",
                        icon=ft.Icons.CHECK_CIRCLE,
                        bgcolor=ft.Colors.GREEN_700,
                        color=ft.Colors.WHITE,
                        on_click=self._marcar_entregue
                    )
                )
            area_acoes = ft.Row(botoes, spacing=10)

        return ft.Container(
            content=ft.Column([
                cabecalho,
                ft.Divider(),
                info_card,
                ft.Divider(),
                area_acoes,
            ], scroll=ft.ScrollMode.AUTO),
            expand=True,
            padding=20
        )

    def _abrir_form_nota(self, e):
        nota_str = str(self.nota_obtida).strip()
        self.campo_nota.value = nota_str if nota_str not in ["", "None", "nan"] else ""
        self.exibir_form_nota = True
        self.page.clean()
        self.page.add(self.construir())
        self.page.update()

    def _cancelar_form(self, e):
        self.exibir_form_nota = False
        self.page.clean()
        self.page.add(self.construir())
        self.page.update()

    def _salvar_nota(self, e):
        valor = self.campo_nota.value.strip() if self.campo_nota.value else ""
        if not valor:
            if self.page:
                self.page.snack_bar = ft.SnackBar(ft.Text("Digite a nota antes de salvar."), open=True)
                self.page.update()
            return
        self.exibir_form_nota = False
        self._on_click(e, "salvar_nota", {'nota_obtida': valor})

    def _marcar_entregue(self, e):
        self._on_click(e, "marcar_entregue")

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
