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

class VisualizadorMateria(VisualizadorAbstrato):
    def __init__(self):
        # A variável 'materia' começará como None. 
        # O Controlador vai preenchê-la com o objeto TADMateria real.
        self.materia = None 
    
    def nome_da_pagina(self) -> str:
        return "pagina_materia"
    
    def construir(self):
        # Proteção: Se a tela tentar desenhar antes dos dados do controlador chegarem
        if not self.materia:
            # Trocamos o Container com alignment por uma Row centralizada (funciona em qualquer versão do Flet)
            return ft.Row([
                ft.Text("A carregar dados da matéria...", size=20, color=ft.Colors.GREY)
            ], alignment=ft.MainAxisAlignment.CENTER)

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
            ft.Text(f"📚 {self.materia.nome}", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
        ])

        info_materia = ft.Column([
            titulo_com_botao,
            ft.Container(height=10),
            ft.Text(f"👨‍🏫 Professor: {self.materia.professor}", size=16, color=ft.Colors.GREY_700),
            ft.Text(f"⏰ Horário: {self.materia.horario}", size=16, color=ft.Colors.GREY_700),
        ], padding=ft.padding.only(left=40))

        # ==========================================
        # 2. LISTA DINÂMICA DE ATIVIDADES
        # ==========================================
        coluna_atividades = ft.Column()

        for ativ in self.materia.atividades:
            is_prova = "Prova" in ativ.titulo
            cor_fundo = ft.Colors.BLUE_50 if is_prova else ft.Colors.GREEN_50
            cor_botao = ft.Colors.BLUE if is_prova else ft.Colors.GREEN
            icone = "📝" if is_prova else "📁"
            texto_botao = "Dar Nota" if is_prova else "Entregar"

            cartao = ft.Container(
                content=ft.Row([
                    ft.Text(f"{icone} {ativ.titulo} ({ativ.valor} pts)\nStatus: {ativ.status}", 
                            size=14, expand=True, weight=ft.FontWeight.W_500),
                    ft.ElevatedButton(
                        texto_botao,
                        color=ft.Colors.WHITE,
                        bgcolor=cor_botao,
                        on_click=lambda e, id_ativ=ativ.id: self._on_click(e, f"dar_nota_{id_ativ}")
                    )
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                padding=15,
                bgcolor=cor_fundo,
                border_radius=8
            )
            coluna_atividades.controls.extend([cartao, ft.Divider(height=10, color=ft.Colors.TRANSPARENT)])

        # ==========================================
        # 3. RENDERIZAÇÃO
        # ==========================================
        return ft.Column([
            info_materia,
            ft.Divider(color=ft.Colors.BLUE_200, thickness=2, height=30),
            ft.Text("Atividades Avaliativas", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
            ft.Container(height=10),
            coluna_atividades,
            ft.ElevatedButton(
                "➕ Nova Atividade",
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.ORANGE_700,
                on_click=lambda e: self._on_click(e, "1")
            )
        ])
    
    def _on_click(self, e, comando):
        if hasattr(self, 'controlador') and self.controlador:
            self.controlador.processar_acao(comando)
    
    def mostrar(self, page: ft.Page):
        if self.controlador and hasattr(self.controlador, 'carregar_dados_para_tela'):
            self.controlador.carregar_dados_para_tela(self)
            
        page.clean()
        page.add(self.construir())
        page.update()