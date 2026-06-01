"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

import flet as ft
from .VisualizadorAbstrato import VisualizadorAbstrato


class VisualizadorLogin(VisualizadorAbstrato):
    def __init__(self):
        self.controlador = None
        self.page = None

        self.email_field = ft.TextField(
            label="E-mail",
            hint_text="seu@email.com",
            prefix_icon=ft.Icons.EMAIL_OUTLINED,
            keyboard_type=ft.KeyboardType.EMAIL,
            autocorrect=False,
            width=360,
            border_radius=10,
            focused_border_color=ft.Colors.BLUE_400,
        )

        self.senha_field = ft.TextField(
            label="Senha",
            hint_text="Digite sua senha",
            prefix_icon=ft.Icons.LOCK_OUTLINED,
            password=True,
            can_reveal_password=True,
            width=360,
            border_radius=10,
            focused_border_color=ft.Colors.BLUE_400,
        )

        self.erro_text = ft.Text(
            "",
            color=ft.Colors.RED_400,
            size=13,
            italic=True,
        )

        self.login_button = ft.ElevatedButton(
            "Entrar",
            on_click=self._on_login_click,
            width=360,
            height=48,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                bgcolor=ft.Colors.BLUE_600,
                color=ft.Colors.WHITE,
                text_style=ft.TextStyle(size=16, weight=ft.FontWeight.BOLD),
            ),
        )

    def nome_da_pagina(self) -> str:
        return "pagina_login"

    def construir(self):
        card = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        "Bem-vindo de volta",
                        size=26,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Text(
                        "Faça login para continuar",
                        size=14,
                        color=ft.Colors.GREY_500,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Divider(height=16, color=ft.Colors.TRANSPARENT),
                    self.email_field,
                    self.senha_field,
                    ft.Container(height=4),
                    self.erro_text,
                    ft.Container(height=4),
                    self.login_button,
                    ft.Divider(height=8, color=ft.Colors.TRANSPARENT),
                    ft.TextButton(
                        "Voltar para Página Inicial",
                        on_click=lambda e: self._on_click(e, "0"),
                        style=ft.ButtonStyle(color=ft.Colors.BLUE_400),
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=8,
            ),
            width=420,
            padding=ft.Padding.symmetric(horizontal=32, vertical=40),
            border_radius=16,
            bgcolor=ft.Colors.SURFACE,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=20,
                color=ft.Colors.with_opacity(0.12, ft.Colors.BLACK),
                offset=ft.Offset(0, 4),
            ),
        )

        return ft.Container(
            content=card,
            alignment=ft.Alignment.CENTER,
            expand=True,
        )

    def _on_click(self, e, comando):
        if self.controlador:
            self.controlador.processar_acao(comando)

    def _on_login_click(self, e):
        email = self.email_field.value
        senha = self.senha_field.value
        if self.controlador:
            self.controlador.processar_acao("login", {"email": email, "senha": senha})

    def mostrar_erro(self, mensagem: str):
        self.erro_text.value = mensagem
        if self.page:
            self.page.update()

    def limpar_erro(self):
        self.erro_text.value = ""
        if self.page:
            self.page.update()

    def mostrar(self, page: ft.Page):
        self.page = page
        page.clean()
        self.email_field.value = ""
        self.senha_field.value = ""
        self.erro_text.value = ""
        page.add(self.construir())
        
        
