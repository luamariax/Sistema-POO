"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

import flet as ft
from .VisualizadorAbstrato import VisualizadorAbstrato
from Controles.ControladorAbstrato import ControladorAbstrato


class VisualizadorMateria(VisualizadorAbstrato):
    def __init__(self):
        self._controlador = None
        self.titulo_materia = "Carregando..."
        self.professor = ""
        self.sala = ""
        self.horarios = ""
        
        # Variável para o Badge de Nota Total
        self.nota_total = 0.0 
        
        self.lista_provas = []
        self.lista_trabalhos = []
        
        self.page = None
        self.exibir_form_prova = False
        self.exibir_form_trabalho = False

        # --- Campos do Formulário de Prova ---
        self.p_titulo = ft.TextField(label="Título da Prova")
        self.p_valor = ft.TextField(label="Valor (ex: 20)")
        self.p_dia = ft.TextField(label="Data (AAAA-MM-DD)")
        self.p_conteudo = ft.TextField(label="Conteúdo")
        self.p_sala = ft.TextField(label="Sala")
        self.p_duracao = ft.TextField(label="Duração (min)")

        # --- Campos do Formulário de Trabalho ---
        self.t_titulo = ft.TextField(label="Título do Trabalho")
        self.t_valor = ft.TextField(label="Valor (ex: 10)")
        self.t_data = ft.TextField(label="Data de Entrega (AAAA-MM-DD)")
        self.t_desc = ft.TextField(label="Descrição")
        self.t_grupo = ft.TextField(label="Grupo? (Sim/Não)")

    @property
    def controlador(self):
        return self._controlador
    
    @controlador.setter
    def controlador(self, controle):
        if not isinstance(controle, ControladorAbstrato):
            raise TypeError("Objeto não é do tipo Controlador.")
        self._controlador = controle

    def nome_da_pagina(self) -> str:
        return "pagina_materia"

    def construir(self):
        # 1. CABEÇALHO
        botao_voltar = ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=lambda e: self._on_click(e, "0"))
        titulo = ft.Text(f"📘 {self.titulo_materia}", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
        cabecalho = ft.Row([botao_voltar, titulo])
        
        # ---------------------------------------------------------
        # 2. CARTÃO DE INFORMAÇÕES (Com a Nota Total embutida)
        # ---------------------------------------------------------
        info_card = ft.Card(
            content=ft.Container(
                content=ft.Row([
                    # Coluna 1: Professor
                    ft.Container(
                        content=ft.Row([ft.Icon(ft.Icons.PERSON, color=ft.Colors.BLUE_500), ft.Text(f"Prof: {self.professor}", weight=ft.FontWeight.BOLD)]),
                        expand=True
                    ),
                    # Coluna 2: Sala
                    ft.Container(
                        content=ft.Row([ft.Icon(ft.Icons.ROOM, color=ft.Colors.BLUE_500), ft.Text(f"Sala: {self.sala}", weight=ft.FontWeight.BOLD)]),
                        expand=True
                    ),
                    # Coluna 3: Horário
                    ft.Container(
                        content=ft.Row([ft.Icon(ft.Icons.SCHEDULE, color=ft.Colors.BLUE_500), ft.Text(f"Horário: {self.horarios}", weight=ft.FontWeight.BOLD)]),
                        expand=True
                    ),
                    # Coluna 4: Badge da Nota Total
                    ft.Container(
                        content=ft.Row([
                            ft.Icon(ft.Icons.STAR_ROUNDED, color=ft.Colors.AMBER_400),
                            ft.Text(f"Total: {self.nota_total:.1f}", weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
                        ]),
                        bgcolor=ft.Colors.BLUE_900,
                        padding=10,
                        border_radius=10,
                    ),
                ], alignment=ft.MainAxisAlignment.START), 
                padding=20 
            )
        )

        # ---------------------------------------------------------
        # 3. LISTAS DE AVALIAÇÕES
        # ---------------------------------------------------------
        coluna_avaliacoes = ft.Column()
        
        # --- Bloco de Provas ---
        coluna_avaliacoes.controls.append(ft.Text("📝 Provas", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700))
        if not self.lista_provas:
            coluna_avaliacoes.controls.append(ft.Text("Nenhuma prova cadastrada.", color=ft.Colors.GREY_500))
        else:
            for i, p in enumerate(self.lista_provas):
                coluna_avaliacoes.controls.append(
                    ft.Container(
                        content=ft.Row([
                            ft.Column([
                                ft.Text(f"{p.get('titulo')} - Valor: {p.get('valor_nota')}", weight=ft.FontWeight.BOLD),
                                ft.Text(f"Data: {p.get('dia')} | Sala: {p.get('sala')}", size=12, color=ft.Colors.GREY_700)
                            ], expand=True),
                            
                            ft.ElevatedButton("Acessar", bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE, 
                                             on_click=lambda e, pos=i: self._on_click(e, f"1-{pos}"))
                        ]), 
                        padding=15, bgcolor=ft.Colors.GREEN_50, border_radius=8, width=float('inf')
                    )
                )

        coluna_avaliacoes.controls.append(ft.Container(height=10))

        # --- Bloco de Trabalhos ---
        coluna_avaliacoes.controls.append(ft.Text("💼 Trabalhos", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_700))
        if not self.lista_trabalhos:
            coluna_avaliacoes.controls.append(ft.Text("Nenhum trabalho cadastrado.", color=ft.Colors.GREY_500))
        else:
            for i, t in enumerate(self.lista_trabalhos):
                coluna_avaliacoes.controls.append(
                    ft.Container(
                        content=ft.Row([
                            ft.Column([
                                ft.Text(f"{t.get('titulo')} - Valor: {t.get('valor_nota')}", weight=ft.FontWeight.BOLD),
                                ft.Text(f"Entrega: {t.get('data_entrega')} | Grupo: {t.get('grupo')}", size=12, color=ft.Colors.GREY_700)
                            ], expand=True),
                            
                            ft.ElevatedButton("Acessar", bgcolor=ft.Colors.ORANGE, color=ft.Colors.WHITE, 
                                             on_click=lambda e, pos=i: self._on_click(e, f"2-{pos}"))
                        ]), 
                        padding=15, bgcolor=ft.Colors.ORANGE_50, border_radius=8, width=float('inf')
                    )
                )

        # ---------------------------------------------------------
        # 4. ÁREA DE CRIAÇÃO (Formulários ou Botões)
        # ---------------------------------------------------------
        area_criacao = ft.Column()

        if self.exibir_form_prova:
            area_criacao.controls.append(self._criar_card_prova())
        elif self.exibir_form_trabalho:
            area_criacao.controls.append(self._criar_card_trabalho())
        else:
            area_criacao.controls.append(
                ft.Row([
                    ft.ElevatedButton("Adicionar Prova", icon=ft.Icons.ADD, bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE, on_click=self._abrir_form_prova),
                    ft.ElevatedButton("Adicionar Trabalho", icon=ft.Icons.ADD, bgcolor=ft.Colors.ORANGE, color=ft.Colors.WHITE, on_click=self._abrir_form_trabalho)
                ], alignment=ft.MainAxisAlignment.CENTER)
            )

        # ---------------------------------------------------------
        # MONTAGEM FINAL DA TELA
        # ---------------------------------------------------------
        return ft.Container(
            content=ft.Column([
                cabecalho,
                ft.Divider(),
                info_card,
                ft.Divider(),
                coluna_avaliacoes,
                ft.Divider(),
                area_criacao
            ], scroll=ft.ScrollMode.AUTO),
            expand=True, padding=20
        )

    # ------------------ FORMULÁRIOS ------------------
    def _criar_card_prova(self):
        return ft.Container(
            content=ft.Column([
                ft.Text("Cadastrar Nova Prova", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                self.p_titulo,
                ft.Row([ft.Container(self.p_valor, expand=True), ft.Container(self.p_dia, expand=True)]),
                self.p_conteudo,
                ft.Row([ft.Container(self.p_sala, expand=True), ft.Container(self.p_duracao, expand=True)]),
                ft.Row([
                    ft.ElevatedButton("Cancelar", color=ft.Colors.RED, on_click=self._cancelar_form),
                    ft.ElevatedButton("Salvar Prova", bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE, on_click=self._salvar_prova)
                ], alignment=ft.MainAxisAlignment.END)
            ]),
            padding=20, bgcolor=ft.Colors.WHITE, border_radius=12
        )

    def _criar_card_trabalho(self):
        return ft.Container(
            content=ft.Column([
                ft.Text("Cadastrar Novo Trabalho", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_700),
                self.t_titulo,
                ft.Row([ft.Container(self.t_valor, expand=True), ft.Container(self.t_data, expand=True)]),
                self.t_desc,
                self.t_grupo,
                ft.Row([
                    ft.ElevatedButton("Cancelar", color=ft.Colors.RED, on_click=self._cancelar_form),
                    ft.ElevatedButton("Salvar Trabalho", bgcolor=ft.Colors.ORANGE, color=ft.Colors.WHITE, on_click=self._salvar_trabalho)
                ], alignment=ft.MainAxisAlignment.END)
            ]),
            padding=20, bgcolor=ft.Colors.WHITE, border_radius=12
        )

    # ------------------ LÓGICA DE CLIQUE E NAVEGAÇÃO ------------------
    def _abrir_form_prova(self, e):
        self.exibir_form_prova = True
        self.exibir_form_trabalho = False
        self.mostrar(self.page)

    def _abrir_form_trabalho(self, e):
        self.exibir_form_trabalho = True
        self.exibir_form_prova = False
        self.mostrar(self.page)

    def _cancelar_form(self, e):
        self.exibir_form_prova = False
        self.exibir_form_trabalho = False
        self.mostrar(self.page)

    def _salvar_prova(self, e):
        dados = {
            'titulo': self.p_titulo.value,
            'valor_nota': self.p_valor.value,
            'dia': self.p_dia.value,
            'conteudo': self.p_conteudo.value,
            'sala': self.p_sala.value,
            'duracao': self.p_duracao.value
        }
        self.p_titulo.value = self.p_valor.value = self.p_dia.value = self.p_conteudo.value = self.p_sala.value = self.p_duracao.value = ""
        self.exibir_form_prova = False
        self._on_click(e, "salvar_nova_prova", dados)

    def _salvar_trabalho(self, e):
        dados = {
            'titulo': self.t_titulo.value,
            'valor_nota': self.t_valor.value,
            'data_entrega': self.t_data.value,
            'descricao_tarefa': self.t_desc.value,
            'grupo': self.t_grupo.value
        }
        self.t_titulo.value = self.t_valor.value = self.t_data.value = self.t_desc.value = self.t_grupo.value = ""
        self.exibir_form_trabalho = False
        self._on_click(e, "salvar_novo_trabalho", dados)

    def _on_click(self, e, comando, dados=None):
        if self.controlador:
            self.controlador.processar_acao(comando, dados)

    def mostrar(self, page: ft.Page):
        self.page = page 
        if self.controlador:
            self.controlador.carregar_dados_para_tela()
        page.clean()
        page.add(self.construir())
        page.update()