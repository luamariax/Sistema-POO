"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""
import flet as ft
from .VisualizadorAbstrato import VisualizadorAbstrato
from Controles.ControladorAbstrato import ControladorAbstrato

class VisualizadorEspecificoEvento(VisualizadorAbstrato):
    def __init__(self):
        self._controlador = None
        self.evento = {}  # Dicionário com os dados do evento a ser exibido

        self.exibir_formulario_edicao = False  # Variável para controlar a exibição do formulário de edição
        self.page = None

        # Campos do formulário de edição
        self.campo_titulo = ft.TextField(label="Título")
        self.campo_descricao = ft.TextField(label="Descrição", multiline=True, min_lines=3)
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
            raise TypeError("CLASSE:VisualizadorEspecificoEvento.py// Objeto não é do tipo Controlador.")
        self._controlador = controle

    def nome_da_pagina(self) -> str:
        return "pagina_especifico_evento"

    def construir(self):
        # CABEÇALHO (Botão Voltar e Título)
        botao_voltar = ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            icon_color=ft.Colors.BLUE_900,
            tooltip="Voltar para todos os eventos",
            on_click=lambda e: self._on_click(e, "0")
        )
        titulo = ft.Text("📋 Detalhes do Evento", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
        cabecalho = ft.Row([botao_voltar, titulo], alignment=ft.MainAxisAlignment.START)

        # ÁREA DE INFORMAÇÕES DO EVENTO
        if not self.evento:
            area_informacoes = ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, size=40, color=ft.Colors.ORANGE_400),
                    ft.Text("Nenhum evento selecionado.", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREY_700),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                alignment=ft.Alignment.CENTER,
                padding=30
            )
            area_edicao = ft.Column()
        else:
            # Card com todas as informações do evento
            area_informacoes = ft.Container(
                content=ft.Column([
                    ft.Text(
                        self.evento.get('titulo', '—'),
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_900
                    ),
                    ft.Divider(color=ft.Colors.BLUE_100),
                    _linha_info(ft.Icons.CALENDAR_TODAY,     "Data de início", self.evento.get('data_inicio', '—')),
                    _linha_info(ft.Icons.EVENT_AVAILABLE,    "Data de fim",    self.evento.get('data_fim', '—')),
                    _linha_info(ft.Icons.LOCATION_ON,        "Local",          self.evento.get('local', '—')),
                    _linha_info(ft.Icons.PERSON,             "Organizador",    self.evento.get('organizador', '—')),
                    _linha_info(ft.Icons.DESCRIPTION,        "Descrição",      self.evento.get('descricao', '—')),
                ]),
                padding=25,
                bgcolor=ft.Colors.BLUE_50,
                border_radius=12,
            )

            # ÁREA DE EDIÇÃO
            area_edicao = ft.Column()

            if self.exibir_formulario_edicao:
                formulario_card = ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Text("Editar Evento", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                            ft.IconButton(
                                icon=ft.Icons.CLOSE,
                                icon_color=ft.Colors.RED_700,
                                tooltip="Fechar formulário de edição",
                                on_click=self._alternar_formulario_edicao
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

                        ft.Container(height=10),  # Espaçador invisível

                        ft.Row([
                            ft.ElevatedButton("Cancelar", color=ft.Colors.RED, on_click=self._alternar_formulario_edicao),
                            ft.ElevatedButton("Salvar Modificações", bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE, on_click=self._salvar_edicao)
                        ], alignment=ft.MainAxisAlignment.END)
                    ]),
                    width=500,  # não deixa o formulário esticar na tela toda
                    padding=25,
                    bgcolor=ft.Colors.WHITE,
                    border_radius=12,
                )

                area_edicao.controls.append(
                    ft.Row([formulario_card], alignment=ft.MainAxisAlignment.CENTER)
                )
            else:
                botao_editar = ft.ElevatedButton(
                    "Editar Evento",
                    icon=ft.Icons.EDIT,
                    bgcolor=ft.Colors.BLUE_700,
                    color=ft.Colors.WHITE,
                    on_click=self._alternar_formulario_edicao
                )
                area_edicao.controls.append(
                    ft.Row([botao_editar], alignment=ft.MainAxisAlignment.CENTER)
                )

        # JUNTA TUDO NA TELA FINAL
        coluna_principal = ft.Column([
            cabecalho,
            ft.Divider(color=ft.Colors.BLUE_200),
            area_informacoes,
            ft.Container(height=20),  # Espaçador invisível
            area_edicao
        ], scroll=ft.ScrollMode.AUTO)

        return ft.Container(
            content=coluna_principal,
            expand=True,
            padding=20
        )

    # FUNÇÕES INTERNAS DE LÓGICA DO FLET

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

    def _alternar_formulario_edicao(self, e):
        self.exibir_formulario_edicao = not self.exibir_formulario_edicao

        # Ao abrir o formulário, pré-preenche os campos com os dados atuais do evento
        if self.exibir_formulario_edicao and self.evento:
            self.campo_titulo.value      = self.evento.get('titulo', '')
            self.campo_descricao.value   = self.evento.get('descricao', '')
            self.campo_data_inicio.value = self.evento.get('data_inicio', '')
            self.campo_data_fim.value    = self.evento.get('data_fim', '')
            self.campo_local.value       = self.evento.get('local', '')
            self.campo_organizador.value = self.evento.get('organizador', '')

        if self.page:
            self.page.clean()
            self.page.add(self.construir())
            self.page.update()

    def _salvar_edicao(self, e):
        dados_do_form = {
            'titulo':      self.campo_titulo.value,
            'descricao':   self.campo_descricao.value,
            'data_inicio': self.campo_data_inicio.value,
            'data_fim':    self.campo_data_fim.value,
            'local':       self.campo_local.value,
            'organizador': self.campo_organizador.value
        }

        self.campo_titulo.value      = ""
        self.campo_descricao.value   = ""
        self.campo_data_inicio.value = ""
        self.campo_data_fim.value    = ""
        self.campo_local.value       = ""
        self.campo_organizador.value = ""

        self.exibir_formulario_edicao = False
        self._on_click(e, "salvar_edicao", dados_do_form)

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


# FUNÇÃO AUXILIAR (fora da classe, escopo do módulo)

def _linha_info(icone, rotulo: str, valor: str) -> ft.Row:
    """Monta uma linha de informação com ícone, rótulo em negrito e valor."""
    return ft.Row([
        ft.Icon(icone, size=18, color=ft.Colors.BLUE_700),
        ft.Text(f"{rotulo}:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.GREY_800),
        ft.Text(valor, size=14, color=ft.Colors.GREY_700),
    ], spacing=8)



