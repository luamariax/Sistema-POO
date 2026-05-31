"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

"""import flet as ft
from .VisualizadorAbstrato import VisualizadorAbstrato

class VisualizadorEspecificoEvento(VisualizadorAbstrato):
    def __init__(self):
        self.controlador = None
        self.page = None

        self.dic_evento = None
    
    def nome_da_pagina(self) -> str:
        return "pagina_especifico_evento"
    
    def construir(self):
        # vai receber um dicionário
        self.dic_evento = self.controlador.dar_dados()

        return ft.Column([
            ft.Text("Página deste Evento Específico", size=30, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Dados do evento"),
            ft.ElevatedButton("Voltar para Página Todos Eventos", on_click=lambda e: self._on_click(e, "0")),
        ])
    
    def _on_click(self, e, comando):
        if hasattr(self, 'controlador'):
            self.controlador.processar_acao(comando)
    
    def mostrar(self, page: ft.Page):
        page.clean()
        page.add(self.construir())
        
        """

import flet as ft
from abc import ABC, abstractmethod


class VisualizadorAbstrato(ABC):
    @abstractmethod
    def nome_da_pagina(self) -> str:
        pass
    
    @abstractmethod
    def construir(self):
        pass
    
    @abstractmethod
    def mostrar(self, page):
        pass


class VisualizadorEspecificoEvento(VisualizadorAbstrato):
    def __init__(self):
        self.controlador = None
        self.page = None
        self.dic_evento = None

    def nome_da_pagina(self) -> str:
        return "pagina_especifico_evento"

    def construir(self):
        self.dic_evento = self.controlador.dar_dados()

        titulo     = self.dic_evento.get("titulo", "—")
        descricao  = self.dic_evento.get("descricao", "—")
        data_inicio = self.dic_evento.get("data_inicio", "—")
        data_fim   = self.dic_evento.get("data_fim", "—")
        local      = self.dic_evento.get("local", "—")
        organizador = self.dic_evento.get("organizador", "—")

        # ── Botão voltar (topo esquerdo) ─────────────────────────────────
        btn_voltar = ft.TextButton(
            content=ft.Row(
                [
                    ft.Icon(ft.Icons.ARROW_BACK_IOS_NEW_ROUNDED, size=16),
                    ft.Text("Voltar", size=14),
                ],
                spacing=4,
                tight=True,
            ),
            on_click=lambda e: self._on_click(e, "0"),
        )

        topo = ft.Row(
            [btn_voltar],
            alignment=ft.MainAxisAlignment.START,
        )

        # ── Cabeçalho do evento ──────────────────────────────────────────
        cabecalho = ft.Column(
            [
                ft.Text(
                    titulo,
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    f"Organizado por {organizador}",
                    size=14,
                    color=ft.Colors.GREY_600,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=4,
        )

        # ── Linha divisória ──────────────────────────────────────────────
        divider = ft.Divider(thickness=1, color=ft.Colors.GREY_300)

        # ── Helper: linha de detalhe com ícone ──────────────────────────
        def linha_detalhe(icone: str, rotulo: str, valor: str) -> ft.Row:
            return ft.Row(
                [
                    ft.Icon(icone, size=20, color=ft.Colors.INDIGO_400),
                    ft.Column(
                        [
                            ft.Text(rotulo, size=12, color=ft.Colors.GREY_600),
                            ft.Text(valor,  size=15, weight=ft.FontWeight.W_500),
                        ],
                        spacing=1,
                        tight=True,
                    ),
                ],
                spacing=12,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )

        # ── Card de detalhes ─────────────────────────────────────────────
        card_detalhes = ft.Container(
            content=ft.Column(
                [
                    linha_detalhe(ft.Icons.CALENDAR_TODAY_OUTLINED, "Início", data_inicio),
                    ft.Divider(thickness=0.5, color=ft.Colors.GREY_200),
                    linha_detalhe(ft.Icons.EVENT_AVAILABLE_OUTLINED, "Término", data_fim),
                    ft.Divider(thickness=0.5, color=ft.Colors.GREY_200),
                    linha_detalhe(ft.Icons.LOCATION_ON_OUTLINED, "Local", local),
                    ft.Divider(thickness=0.5, color=ft.Colors.GREY_200),
                    linha_detalhe(ft.Icons.PERSON_OUTLINE_ROUNDED, "Organizador", organizador),
                ],
                spacing=12,
            ),
            padding=ft.Padding(left=20, right=20, top=16, bottom=16),
            border=ft.Border(
                top=ft.BorderSide(1, ft.Colors.GREY_300),
                bottom=ft.BorderSide(1, ft.Colors.GREY_300),
                left=ft.BorderSide(1, ft.Colors.GREY_300),
                right=ft.BorderSide(1, ft.Colors.GREY_300),
            ),
            border_radius=ft.border_radius.all(12),
            bgcolor=ft.Colors.WHITE,
        )

        # ── Seção de descrição ───────────────────────────────────────────
        secao_descricao = ft.Column(
            [
                ft.Text("Descrição", size=16, weight=ft.FontWeight.W_500),
                ft.Text(
                    descricao,
                    size=14,
                    color=ft.Colors.GREY_700,
                    selectable=True,
                ),
            ],
            spacing=6,
        )

        # ── Botão editar (centro inferior) ───────────────────────────────
        btn_editar = ft.ElevatedButton(
            content=ft.Row(
                [
                    ft.Icon(ft.Icons.EDIT_OUTLINED, size=18),
                    ft.Text("Editar evento", size=15),
                ],
                spacing=8,
                tight=True,
            ),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                padding=ft.Padding(left=24, right=24, top=14, bottom=14),
            ),
            on_click=lambda e: self._on_click(e, "editar"),
        )

        rodape = ft.Row(
            [btn_editar],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        # ── Layout completo ──────────────────────────────────────────────
        conteudo = ft.Column(
            [
                topo,
                ft.Container(height=8),
                cabecalho,
                ft.Container(height=4),
                divider,
                ft.Container(height=8),
                card_detalhes,
                ft.Container(height=16),
                secao_descricao,
                ft.Container(height=32),
                rodape,
            ],
            spacing=0,
            expand=True,
        )

        return ft.Container(
            content=conteudo,
            padding=ft.Padding(left=24, right=24, top=16, bottom=24),
            expand=True,
        )

    def _on_click(self, e, comando: str):
        if hasattr(self, "controlador"):
            self.controlador.processar_acao(comando)

    def mostrar(self, page: ft.Page):
        self.page = page
        page.clean()
        page.add(self.construir())


class ControladorStub:
    """Imita o controlador real fornecendo dados fictícios e registrando ações."""
 
    EVENTO_EXEMPLO = {
        "titulo":      "Festival de Tecnologia 2025",
        "descricao":   "Um evento que reúne desenvolvedores, designers e entusiastas "
                       "de tecnologia para palestras, workshops e networking. "
                       "Venha aprender, compartilhar e se conectar com a comunidade!",
        "data_inicio": "10/08/2025 às 09:00",
        "data_fim":    "12/08/2025 às 18:00",
        "local":       "Centro de Convenções BH, Belo Horizonte – MG",
        "organizador": "TechBH Comunidade",
    }
 
    def dar_dados(self) -> dict:
        return self.EVENTO_EXEMPLO
 
    def processar_acao(self, comando: str):
        print(f"[ControladorStub] ação recebida: '{comando}'")

# ── Ponto de entrada ─────────────────────────────────────────────────────────
def main(page: ft.Page):
    page.title = "App com Arquitetura MVC - Múltiplos Arquivos"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.window_width = 400
    page.window_height = 600
 
    view = VisualizadorEspecificoEvento()
    view.controlador = ControladorStub()
    view.mostrar(page)

if __name__ == "__main__":
    pagina = ft.Page
    main(pagina)
