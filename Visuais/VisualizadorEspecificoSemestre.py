"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""
import flet as ft
from .VisualizadorAbstrato import VisualizadorAbstrato
from Controles.ControladorAbstrato import ControladorAbstrato

class VisualizadorEspecificoSemestre(VisualizadorAbstrato):
    def __init__(self):
        self._controlador = None
        self.lista_materias = []
        self.titulo_semestre = "Carregando..."
        self.page = None

        self.exibir_formulario = False

        self.campo_titulo = ft.TextField(label="Título da Matéria (ex: Cálculo I)")
        self.campo_descricao = ft.TextField(label="Descrição")
        self.campo_professor = ft.TextField(label="Professor")
        self.campo_sala = ft.TextField(label="Sala")
        self.campo_horarios = ft.TextField(label="Horários (ex: Seg 10h, Qua 10h)")

    @property
    def controlador(self):
        return self._controlador

    @controlador.setter
    def controlador(self, controle):
        if not isinstance(controle, ControladorAbstrato):
            raise TypeError("Objeto não é do tipo Controlador.")
        self._controlador = controle

    def nome_da_pagina(self) -> str:
        return "pagina_especifico_semestre"

    def construir(self):
        # CABEÇALHO
        botao_voltar = ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=lambda e: self._on_click(e, "0"))
        titulo = ft.Text(f"📚 {self.titulo_semestre}", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
        cabecalho = ft.Row([botao_voltar, titulo])

        if not self.lista_materias:
            coluna_materias = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.MENU_BOOK, size=40, color=ft.Colors.ORANGE_400),
                    ft.Text("Nenhuma matéria cadastrada.", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("Deseja cadastrar uma nova disciplina?", size=14)
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=30
            )
        else:
            lista_cards = []
            for i, mat in enumerate(self.lista_materias):
                card = ft.Container(
                    content=ft.Row([
                        ft.Column([
                            ft.Text(f"{mat['titulo']}", size=16, weight=ft.FontWeight.BOLD),
                            ft.Text(f"Prof: {mat['professor']} | Sala: {mat['sala']}", size=14),
                        ], expand=True),
                        ft.ElevatedButton("Abrir", bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE,
                                         on_click=lambda e, pos=i: self._on_click(e, f"1-{pos}"))
                    ]),
                    padding=15, bgcolor=ft.Colors.BLUE_50, border_radius=8
                )
                lista_cards.append(card)
            coluna_materias = ft.Column(lista_cards)

        # ÁREA DE CRIAÇÃO
        area_criacao = ft.Column()

        if self.exibir_formulario:
            formulario_card = ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text("Cadastrar Nova Matéria", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
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
                    self.campo_professor,
                    ft.Row([
                        ft.Container(self.campo_sala, expand=True),
                        ft.Container(self.campo_horarios, expand=True)
                    ]),

                    ft.Container(height=10),

                    ft.Row([
                        ft.ElevatedButton("Cancelar", color=ft.Colors.RED, on_click=self._alternar_formulario),
                        ft.ElevatedButton("Salvar Nova", bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE, on_click=self._salvar_nova)
                    ], alignment=ft.MainAxisAlignment.END)
                ]),
                width=500,
                padding=25,
                bgcolor=ft.Colors.WHITE,
                border_radius=12,
            )

            area_criacao.controls.append(
                ft.Row([formulario_card], alignment=ft.MainAxisAlignment.CENTER)
            )
        else:
            botao_novo = ft.ElevatedButton(
                "Adicionar Matéria",
                icon=ft.Icons.ADD,
                on_click=self._alternar_formulario
            )
            area_criacao.controls.append(
                ft.Row([botao_novo], alignment=ft.MainAxisAlignment.CENTER)
            )

        # ROLAGEM E CONSTRUÇÃO FINAL
        return ft.Container(
            content=ft.Column([
                cabecalho,
                ft.Divider(),
                coluna_materias,
                ft.Divider(),
                area_criacao
            ], scroll=ft.ScrollMode.AUTO),
            expand=True,
            padding=20
        )

    def _alternar_formulario(self, e):
        self.exibir_formulario = not self.exibir_formulario
        if self.page:
            self.page.clean()
            self.page.add(self.construir())
            self.page.update()

    def _salvar_nova(self, e):
        dados_do_form = {
            'titulo': self.campo_titulo.value,
            'descricao': self.campo_descricao.value,
            'professor': self.campo_professor.value,
            'sala': self.campo_sala.value,
            'horario': self.campo_horarios.value,
        }

        self.campo_titulo.value = ""
        self.campo_descricao.value = ""
        self.campo_professor.value = ""
        self.campo_sala.value = ""
        self.campo_horarios.value = ""

        self.exibir_formulario = False
        self._on_click(e, "salvar_novo", dados_do_form)

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
