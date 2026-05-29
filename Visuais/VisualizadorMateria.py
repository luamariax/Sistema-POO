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
        self.container = ft.Container()
        
        # Inicialmente vazio. O ControladorMateria é quem vai preencher isto
        # com os dados do Excel antes de chamar o mostrar().
        self.materia = None 
    
    def nome_da_pagina(self) -> str:
        return "pagina_materia"
    
    def construir(self):
        # Proteção: Se a tela tentar desenhar antes dos dados chegarem, não quebra o app.
        if not self.materia:
            return ft.Text("A carregar dados da matéria...", size=20, color=ft.Colors.GREY)

        # ==========================================
        # 1. CABEÇALHO (Agora usa self.materia.X)
        # ==========================================
        botao_voltar = ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            icon_color=ft.Colors.BLUE_900,
            tooltip="Voltar para a página anterior",
            on_click=lambda e: self._on_click(e, "0")
        )

        titulo_com_botao = ft.Row([
            botao_voltar,
            ft.Text(f"📚 {self.materia.nome}", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
        ], alignment=ft.MainAxisAlignment.START)

        info_materia = ft.Column([
            titulo_com_botao,
            ft.Row([
                ft.Container(width=40), 
                ft.Column([
                    ft.Text(f"👨‍🏫 Professor: {self.materia.professor}", size=16, color=ft.Colors.GREY_700),
                    ft.Text(f"⏰ Horário: {self.materia.horario}", size=16, color=ft.Colors.GREY_700),
                ])
            ])
        ])

        # A nota atual pode ser atualizada futuramente chamando self.materia.calcular_nota()
        nota_atual = 0.0  

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

        linha_topo = ft.Row(
            controls=[info_materia, caixa_nota],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN, 
            vertical_alignment=ft.CrossAxisAlignment.START 
        )

        cabecalho = ft.Column([
            linha_topo,
            ft.Divider(color=ft.Colors.BLUE_200, thickness=2, height=30),
            ft.Text("Atividades Avaliativas", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
        ])

        # ==========================================
        # 2. LISTA DINÂMICA DE ATIVIDADES
        # ==========================================
        # Criamos uma coluna vazia que vai ser preenchida pelo 'for' abaixo
        coluna_atividades = ft.Column()

        # Percorremos todas as atividades reais que vieram do Excel
        for atividade in self.materia.atividades:
            
            # Condicionais para mudar a cor e o ícone dependendo do tipo da atividade
            is_prova = "Prova" in atividade.titulo
            cor_fundo = ft.Colors.BLUE_50 if is_prova else ft.Colors.GREEN_50
            cor_botao = ft.Colors.BLUE if is_prova else ft.Colors.GREEN
            icone = "📝" if is_prova else "📁"
            texto_botao = "Dar Nota" if is_prova else "Entregar"

            cartao = ft.Container(
                content=ft.Row([
                    ft.Text(f"{icone} {atividade.titulo} ({atividade.valor} pts) \nStatus: {atividade.status}", size=14, expand=True),
                    ft.ElevatedButton(
                        texto_botao,                
                        color=ft.Colors.WHITE,      
                        bgcolor=cor_botao,
                        # Passamos o ID REAL da atividade para o Controlador saber qual botão foi clicado
                        on_click=lambda e, id_ativ=atividade.id: self._on_click(e, f"dar_nota_{id_ativ}")
                    )
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                padding=15,
                bgcolor=cor_fundo, 
                border_radius=8
            )
            
            coluna_atividades.controls.append(cartao)
            coluna_atividades.controls.append(ft.Divider(height=10, color=ft.Colors.TRANSPARENT))

        # ==========================================
        # 3. BOTÃO NOVA ATIVIDADE
        # ==========================================
        botao_novo = ft.Row([
            ft.ElevatedButton(
                "➕ Nova Atividade",          
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.ORANGE_700,
                on_click=lambda e: self._on_click(e, "1")
            )
        ], alignment=ft.MainAxisAlignment.CENTER)

        # ==========================================
        # 4. RENDERIZAÇÃO FINAL
        # ==========================================
        return ft.Column([
            cabecalho,
            coluna_atividades, # Inserimos a lista gerada dinamicamente aqui
            ft.Divider(color=ft.Colors.GREY_300),
            botao_novo
        ])
    
    def _on_click(self, e, comando):
        if hasattr(self, 'controlador') and self.controlador:
            self.controlador.processar_acao(comando)
        else:
            print(f"[AÇÃO DISPARADA] O comando '{comando}' foi acionado!")
    
    def mostrar(self, page: ft.Page):
        page.clean()
        page.add(self.construir())
        page.update()