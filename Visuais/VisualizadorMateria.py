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

#Dados fictícios para visualização da página

import flet as ft
from .VisualizadorAbstrato import VisualizadorAbstrato

class VisualizadorMateria(VisualizadorAbstrato):
    def __init__(self):
        self.container = ft.Container()
        
        # Dados simulados da Matéria (No futuro virão do Controlador/Excel)
        self.materia_nome = "Programação Orientada a Objetos"
        self.materia_prof = "Profa. Luiza Bernardes"
        self.materia_horario = "Terças, 19:00h - 20:40h"
    
    def nome_da_pagina(self) -> str:
        return "pagina_materia"
    
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
            ft.Text(f"📚 {self.materia_nome}", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
        ], alignment=ft.MainAxisAlignment.START)

        info_materia = ft.Column([
            titulo_com_botao,
            # Trocamos o padding por uma Row com um Container invisível de 40 pixels!
            ft.Row([
                ft.Container(width=40), # Este é o nosso "espaço em branco"
                ft.Column([
                    ft.Text(f"👨‍🏫 Professor: {self.materia_prof}", size=16, color=ft.Colors.GREY_700),
                    ft.Text(f"⏰ Horário: {self.materia_horario}", size=16, color=ft.Colors.GREY_700),
                ])
            ])
        ])

        # --- LADO DIREITO ---
        # Simulação: No futuro, chamarás -> nota_atual = self.materia.calcular_nota()
        nota_atual = 15.0  

        caixa_nota = ft.Container(
            content=ft.Column([
                ft.Text("Total Acumulado", size=14, color=ft.Colors.GREY_700, weight=ft.FontWeight.BOLD),
                ft.Text(f"{nota_atual} pts", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700)
            ], 
            horizontal_alignment=ft.CrossAxisAlignment.END,
            spacing=2),
            padding=15,
            bgcolor=ft.Colors.GREEN_50,
            border_radius=8
        )

        # Junta a esquerda e a direita
        linha_topo = ft.Row(
            controls=[info_materia, caixa_nota],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN, 
            vertical_alignment=ft.CrossAxisAlignment.START 
        )

        # Monta o cabeçalho final
        cabecalho = ft.Column([
            linha_topo,
            ft.Divider(color=ft.Colors.BLUE_200, thickness=2, height=30),
            ft.Text("Atividades Avaliativas", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
        ])

        # ==========================================
        # 2. PROVA
        # ==========================================
        atividade_prova = ft.Container(
            content=ft.Row([
                ft.Text("📝 Prova Parcial 1 (10.0 pts) \nStatus: Aguardando nota", size=14, expand=True),
                ft.ElevatedButton(
                    "Dar Nota",                 
                    color=ft.Colors.WHITE,      
                    bgcolor=ft.Colors.BLUE,     
                    on_click=lambda e: self._on_click(e, "dar_nota_prova1")
                )
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            padding=15,
            bgcolor=ft.Colors.BLUE_50, 
            border_radius=8
        )

        # ==========================================
        # 3. TRABALHO
        # ==========================================
        atividade_trabalho = ft.Container(
            content=ft.Row([
                ft.Text("📁 Trabalho Prático (5.0 pts) \nStatus: Não entregue", size=14, expand=True),
                ft.ElevatedButton(
                    "Entregar",                 
                    color=ft.Colors.WHITE,
                    bgcolor=ft.Colors.GREEN,
                    on_click=lambda e: self._on_click(e, "entregar_trab1")
                )
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            padding=15,
            bgcolor=ft.Colors.GREEN_50,
            border_radius=8
        )

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

        # Retorna a Coluna principal com todos os elementos
        return ft.Column([
            cabecalho,
            atividade_prova,
            ft.Divider(height=10, color=ft.Colors.TRANSPARENT), # Espaçador invisível
            atividade_trabalho,
            ft.Divider(color=ft.Colors.GREY_300),
            botao_novo
        ])
    
    def _on_click(self, e, comando):
        # Envia a ação para o controlador, se ele existir
        if hasattr(self, 'controlador') and self.controlador:
            self.controlador.processar_acao(comando)
        else:
            print(f"[AÇÃO DISPARADA] O comando '{comando}' foi acionado!")
    
    def mostrar(self, page: ft.Page):
        page.clean()
        page.add(self.construir())
        page.update()