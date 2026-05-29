"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

import flet as ft
from .VisualizadorAbstrato import VisualizadorAbstrato
from Controles.ControladorAbstrato import ControladorAbstrato

class VisualizadorEntrada(VisualizadorAbstrato):
    def __init__(self):
        self._controlador = None
        self._nome = "nome da pessoa"

    @property
    def controlador(self):
        return self._controlador
    
    @controlador.setter
    def controlador(self, controle):
        if not isinstance(controle, ControladorAbstrato):
            raise TypeError(f"CLASSE:VisualizadorEntrada.py// Objeto não é do tipo Controlador.")
        self._controlador = controle

    def nome_da_pagina(self) -> str:
        return "pagina_entrada"
    
    def construir(self):
        # ==========================================
        # 1. CABEÇALHO (Botão Voltar, Título)
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
            ft.Text(f"PAGÍNA DE ENTRADA", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
        ], alignment=ft.MainAxisAlignment.START)

        info_entrada = ft.Column([
            titulo_com_botao,
            # Trocamos o padding por uma Row com um Container invisível de 40 pixels!
            ft.Row([
                ft.Container(width=40), # Este é o nosso "espaço em branco"
                ft.Column([
                    ft.Text(f"Bem vind@! {self._nome}", size=16, color=ft.Colors.GREY_700),
                ])
            ])
        ])

        # Monta o cabeçalho final
        cabecalho = ft.Column([
            info_entrada,
            ft.Divider(color=ft.Colors.BLUE_200, thickness=2, height=30),
            ft.Text("O que você gostaria de ver?", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
        ])

        # ==========================================
        # 2. Opção de ver próximos eventos
        # ==========================================
        opcao_eventos = ft.Container(
            content=ft.Row([
                ft.Text("📅 Todos os eventos", size=14, expand=True),
                ft.ElevatedButton(
                    "Ver",                 
                    color=ft.Colors.WHITE,      
                    bgcolor=ft.Colors.BLUE,     
                    # Manda "2" para a Rota abrir os Eventos
                    on_click=lambda e: self._on_click(e, "2")
                )
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            padding=15,
            bgcolor=ft.Colors.BLUE_50, 
            border_radius=8
        )

        # ==========================================
        # 3. Opção de ver os semestres cadastrados
        # ==========================================

        opcao_semestres = ft.Container(
            content=ft.Row([
                ft.Text("🎓 Todos os semestres", size=14, expand=True),
                ft.ElevatedButton(
                    "Ver",                 
                    color=ft.Colors.WHITE,
                    bgcolor=ft.Colors.GREEN,
                    # Manda "1" para a Rota abrir os Semestres
                    on_click=lambda e: self._on_click(e, "1")
                )
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            padding=15,
            bgcolor=ft.Colors.GREEN_50,
            border_radius=8
        )
        
        # Retorna a Coluna principal com todos os elementos
        return ft.Column([
            cabecalho,
            opcao_eventos,
            ft.Divider(height=10, color=ft.Colors.TRANSPARENT), # Espaçador invisível
            opcao_semestres,
            ft.Divider(color=ft.Colors.GREY_300)
        ])
    
        
    def _on_click(self, e, comando):
        if hasattr(self, 'controlador'):
            self.controlador.processar_acao(comando)
    
    def mostrar(self, page: ft.Page):
        page.clean()
        page.add(self.construir())
        page.update()
