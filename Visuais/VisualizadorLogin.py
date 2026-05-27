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
        self.email_field = ft.TextField(label="Email", width=300)
        self.senha_field = ft.TextField(label="Senha", password=True, width=300)
        self.erro_text = ft.Text("", color=ft.Colors.RED)
        self.login_button = ft.ElevatedButton("Entrar", on_click=self._on_login_click)

    def nome_da_pagina(self) -> str:
        return "pagina_login"

    def construir(self):
        # ==========================================
        # 1. CABEÇALHO (Botão Voltar, Título e Nota)
        # ==========================================
        
        # O VERDADEIRO BOTÃO DE VOLTAR (Ícone de Seta enviando "0")
        botao_voltar = ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            icon_color=ft.Colors.BLUE_900,
            tooltip="Voltar para a página anterior",
            on_click=lambda e: self._on_click(e, "0")
        )

        titulo_com_botao = ft.Row([
            botao_voltar,
            ft.Text(f"PÁGINA DE LOGIN", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
        ], alignment=ft.MainAxisAlignment.START)

        info_login = ft.Column([
            titulo_com_botao,
            ft.Row([
                ft.Container(width=40), 
                ft.Column([
                    ft.Text(f"escreva seu e-mail e senha", size=16, color=ft.Colors.GREY_700)
                ])
            ])
        ])

        # Monta o cabeçalho final
        cabecalho = ft.Column([
            info_login,
            ft.Divider(color=ft.Colors.BLUE_200, thickness=2, height=30),
            ft.Text("Atividades Avaliativas", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
        ])

        # ==========================================
        # 4. BOTÃO NOVA ATIVIDADE
        # ==========================================
        botao_novo = ft.Row([
            ft.ElevatedButton(
                "➕ Nova Atividade",          
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.ORANGE_700,
                # Enviando "1" para abrir a página da atividade
                on_click=lambda e: self._on_click(e, "1")
            )
        ], alignment=ft.MainAxisAlignment.CENTER)


        return ft.Column([
            ft.Text("Página de Login", size=30, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            self.email_field,
            self.senha_field,
            self.login_button,
            self.erro_text,
            ft.ElevatedButton("Voltar para Página Inicial", on_click=lambda e: self._on_click(e, "0"))
        ])

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
        # Limpa campos e erro ao entrar na página
        self.email_field.value = ""
        self.senha_field.value = ""
        self.erro_text.value = ""
        page.add(self.construir())
        
        
