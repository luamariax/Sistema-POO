"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""
import flet as ft
from .VisualizadorAbstrato import VisualizadorAbstrato
from Controles.ControladorAbstrato import ControladorAbstrato

class VisualizadorTodosEventos(VisualizadorAbstrato):
    def __init__(self):
        self._controlador = None
        self.lista_eventos = []  

        self.exibir_formulario = False  # Variável para controlar a exibição do formulário de criação
        self.page = None 

        # Adicionados InputFilters para garantir que as validações isdigit() da classe não falhem por erro de digitação
        self.campo_titulo = ft.TextField(label="Título")
        self.campo_descricao = ft.TextField(label="Descrição")
        self.campo_local = ft.TextField(label="Local")
        self.campo_organizador = ft.TextField(label="Organizador")

        self.campo_data_inicio = ft.TextField(
            label="Data de início (ex: 2026-09-26)",
            hint_text="AAAA-MM-DD",
            max_length=10,
            input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9\-]", replacement_string=""),
            on_change=lambda e: self._formatar_data(e, self.campo_data_inicio)
        )

        self.campo_data_fim = ft.TextField(
            label="Data de fim (ex: 2026-10-02)",
            hint_text="AAAA-MM-DD",
            max_length=10,
            input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9\-]", replacement_string=""),
            on_change=lambda e: self._formatar_data(e, self.campo_data_fim)
        )
        

    @property
    def controlador(self):
        return self._controlador
    
    @controlador.setter
    def controlador(self, controle):
        if not isinstance(controle, ControladorAbstrato):
            raise TypeError("CLASSE:VisualizadorTodosEventos.py// Objeto não é do tipo Controlador.")
        self._controlador = controle


    def nome_da_pagina(self) -> str:
        return "pagina_todos_eventos"
        
    def construir(self):
        # CABEÇALHO (Botão Voltar e Título)
        botao_voltar = ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            icon_color=ft.Colors.BLUE_900,
            tooltip="Voltar para a página anterior",
            on_click=lambda e: self._on_click(e, "0")
        )
        titulo = ft.Text("🎓 Todos os Eventos", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
        cabecalho = ft.Row([botao_voltar, titulo], alignment=ft.MainAxisAlignment.START)

        # LISTA DE EVENTOS (Estado Vazio ou Lista)
        if not self.lista_eventos: 
            coluna_lista = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, size=40, color=ft.Colors.ORANGE_400),
                    ft.Text("Nenhum evento cadastrado.", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREY_700),
                    ft.Text("Deseja cadastrar um novo evento?", size=14, color=ft.Colors.GREY_500)
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                alignment=ft.Alignment.CENTER,
                padding=30
            )
        else:
            lista_cards = []
            for i, eve in enumerate(self.lista_eventos):
                card = ft.Container(
                    content=ft.Row([
                        ft.Column([
                            ft.Text(f"{eve['titulo']}", size=18, weight=ft.FontWeight.BOLD),
                            ft.Text(f"Data de início: {eve['data_inicio']} | Local: {eve['local']}", size=12, color=ft.Colors.GREY_700),
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
                        ft.Text("Cadastrar Novo Evento", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.IconButton(
                            icon=ft.Icons.CLOSE, 
                            icon_color=ft.Colors.RED_700, 
                            tooltip="Fechar Formulário",
                            on_click=self._alternar_formulario
                        )
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    
                    ft.Divider(color=ft.Colors.GREY_200),
                    
                    self.campo_titulo,
                    
                    ft.Row([
                        ft.Container(self.campo_data_inicio, expand=True), 
                        ft.Container(self.campo_data_fim, expand=True)
                    ]),
                    self.campo_local,
                    self.campo_organizador,
                    self.campo_descricao,

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
                "Criar Novo Evento", 
                icon=ft.Icons.ADD, 
                on_click=self._alternar_formulario
            )
            # Centraliza o botão de criar também
            area_criacao.controls.append(
                ft.Row([botao_novo], alignment=ft.MainAxisAlignment.CENTER)
            )

        # JUNTA TUDO NA TELA FINAL
        coluna_principal = ft.Column([
            cabecalho,
            ft.Divider(color=ft.Colors.BLUE_200),
            coluna_lista,
            ft.Divider(color=ft.Colors.GREY_300),
            area_criacao
        ], scroll=ft.ScrollMode.AUTO)

        return ft.Container(
            content=coluna_principal,
            expand=True,
            padding=20 # Um padding extra para dar um respiro às bordas da tela
        )

    #FUNÇÕES INTERNAS DE LÓGICA DO FLET
    def _formatar_data(self, e, campo: ft.TextField):
        """Formata o valor do campo para AAAA-MM-DD automaticamente enquanto o usuario digita."""
        apenas_digitos = campo.value.replace("-", "")[:8]
 
        texto_formatado = apenas_digitos
        if len(apenas_digitos) > 4:
            texto_formatado = apenas_digitos[:4] + "-" + apenas_digitos[4:]
        if len(apenas_digitos) > 6:
            texto_formatado = apenas_digitos[:4] + "-" + apenas_digitos[4:6] + "-" + apenas_digitos[6:]
 
        campo.value = texto_formatado
        campo.update()
    
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
            'data_inicio': self.campo_data_inicio.value,
            'data_final': self.campo_data_fim.value,
            'local': self.campo_local.value,
            'organizador': self.campo_organizador.value
        }
        
        self.campo_titulo.value = ""
        self.campo_descricao.value = ""
        self.campo_data_inicio = ""
        self.campo_data_fim = ""
        self.campo_local = ""
        self.campo_organizador = ""
        
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