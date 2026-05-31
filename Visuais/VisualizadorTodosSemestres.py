"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

import flet as ft
from .VisualizadorAbstrato import VisualizadorAbstrato
from Controles.ControladorAbstrato import ControladorAbstrato

class VisualizadorTodosSemestres(VisualizadorAbstrato):
    def __init__(self):
        self._controlador = None
        self.lista_semestres = []  

        self.exibir_formulario = False  # Variável para controlar a exibição do formulário de criação
        self.page = None 

        # Adicionados InputFilters para garantir que as validações isdigit() da classe não falhem por erro de digitação
        self.campo_titulo = ft.TextField(label="Título (ex: 2026-1)")
        self.campo_descricao = ft.TextField(label="Descrição")

        self.campo_ano = ft.TextField(
            label="Ano (ex: 2026)",
            # Permite APENAS números de 0 a 9
            input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string="")
        )
        
        self.campo_semestre_num = ft.TextField(
            label="Semestre (1 ou 2)",
            # Permite APENAS os números 1 ou 2
            input_filter=ft.InputFilter(allow=True, regex_string=r"[1-2]", replacement_string="")
        )
        
        self.campo_ativo = ft.Dropdown(
            label="Ativo?", 
            options=[ft.dropdown.Option("True"), ft.dropdown.Option("False")]
        )

    @property
    def controlador(self):
        return self._controlador
    
    @controlador.setter
    def controlador(self, controle):
        if not isinstance(controle, ControladorAbstrato):
            raise TypeError("CLASSE:VisualizadorTodosSemestres.py// Objeto não é do tipo Controlador.")
        self._controlador = controle


    def nome_da_pagina(self) -> str:
        return "pagina_todos_semestres"
        
    def construir(self):
        # CABEÇALHO (Botão Voltar e Título)
        botao_voltar = ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            icon_color=ft.Colors.BLUE_900,
            tooltip="Voltar para a página anterior",
            on_click=lambda e: self._on_click(e, "0")
        )
        titulo = ft.Text("🎓 Todos os Semestres", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
        cabecalho = ft.Row([botao_voltar, titulo], alignment=ft.MainAxisAlignment.START)

        # LISTA DE SEMESTRES (Estado Vazio ou Lista)
        if not self.lista_semestres: 
            coluna_lista = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, size=40, color=ft.Colors.ORANGE_400),
                    ft.Text("Nenhum semestre cadastrado.", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREY_700),
                    ft.Text("Deseja cadastrar um novo semestre?", size=14, color=ft.Colors.GREY_500)
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                alignment=ft.alignment.center,
                padding=30
            )
        else:
            lista_cards = []
            for i, sem in enumerate(self.lista_semestres):
                card = ft.Container(
                    content=ft.Row([
                        ft.Column([
                            ft.Text(f"{sem['titulo']}", size=18, weight=ft.FontWeight.BOLD),
                            ft.Text(f"Ano: {sem['ano']} | Descrição: {sem['descricao']}", size=12, color=ft.Colors.GREY_700),
                        ]),
                        ft.ElevatedButton(
                            "Abrir",
                            bgcolor=ft.Colors.GREEN,
                            color=ft.Colors.WHITE,
                            on_click=lambda e, pos=i: self._on_click(e, f"1-{pos}")
                        )
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    padding=15,
                    bgcolor=ft.Colors.GREEN_50,
                    border_radius=8
                )
                lista_cards.append(card)
            
            coluna_lista = ft.Column(lista_cards)

        # ÁREA DE CRIAÇÃO (Card Centralizado e Bonito)
        area_criacao = ft.Column()
        
        if self.exibir_formulario:
            formulario_card = ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text("Cadastrar Novo Semestre", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.IconButton(
                            icon=ft.Icons.CLOSE, 
                            icon_color=ft.Colors.RED_700, 
                            tooltip="Fechar Formulário",
                            on_click=self._alternar_formulario
                        )
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    
                    ft.Divider(color=ft.Colors.GREY_200),
                    
                    self.campo_titulo,
                    self.campo_descricao,
                    ft.Row([
                        ft.Container(self.campo_ano, expand=True), 
                        ft.Container(self.campo_semestre_num, expand=True)
                    ]),
                    self.campo_ativo,
                    
                    ft.Container(height=10), # Espaçador invisível
                    
                    ft.Row([
                        ft.ElevatedButton("Cancelar", color=ft.Colors.RED, on_click=self._alternar_formulario),
                        ft.ElevatedButton("Salvar Novo", bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE, on_click=self._salvar_novo)
                    ], alignment=ft.MainAxisAlignment.END)
                ]),
                width=500, # não deixa o formulário esticar na tela toda
                padding=25,
                bgcolor=ft.Colors.WHITE,
                border_radius=12,
            )
            
            # Adiciona o Card dentro de uma Row centralizada
            area_criacao.controls.append(
                ft.Row([formulario_card], alignment=ft.MainAxisAlignment.CENTER)
            )
        else:
            botao_novo = ft.ElevatedButton(
                "Criar Novo Semestre", 
                icon=ft.Icons.ADD, 
                on_click=self._alternar_formulario
            )
            # Centraliza o botão de criar também
            area_criacao.controls.append(
                ft.Row([botao_novo], alignment=ft.MainAxisAlignment.CENTER)
            )

        # JUNTA TUDO NA TELA FINAL
        return ft.Column([
            cabecalho,
            ft.Divider(color=ft.Colors.BLUE_200),
            coluna_lista,
            ft.Divider(color=ft.Colors.GREY_300),
            area_criacao
        ], scroll=ft.ScrollMode.AUTO)

    #FUNÇÕES INTERNAS DE LÓGICA DO FLET
    
    def _alternar_formulario(self, e):
        self.exibir_formulario = not self.exibir_formulario
        if self.page:
            self.page.clean()
            self.page.add(self.construir())
            self.page.update()

    def _salvar_novo(self, e):
        dados_do_form = {
            'titulo': self.campo_titulo.value,
            'descricao': self.campo_descricao.value,
            'ano': self.campo_ano.value,
            'semestre_num': self.campo_semestre_num.value,
            'ativo': self.campo_ativo.value
        }
        
        self.campo_titulo.value = ""
        self.campo_descricao.value = ""
        self.campo_ano.value = ""
        self.campo_semestre_num.value = ""
        self.campo_ativo.value = None
        
        self.exibir_formulario = False
        self._on_click(e, "salvar_novo", dados_do_form)

    # CONEXÃO COM O CONTROLADOR 

    def _on_click(self, e, comando, dados=None):
        if hasattr(self, 'controlador') and self.controlador:
            self.controlador.processar_acao(comando, dados)

    def mostrar(self, page: ft.Page):
        self.page = page
        if self.controlador and hasattr(self.controlador, 'carregar_dados_para_tela'):
            self.controlador.carregar_dados_para_tela()
            
        page.clean()
        page.add(self.construir())
        page.update()