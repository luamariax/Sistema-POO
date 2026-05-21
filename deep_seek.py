import flet as ft
from abc import ABC, abstractmethod
from typing import Dict, Type

# Classes Abstratas
class VisualizadorAbstrato(ABC):
    @abstractmethod
    def nome_da_pagina(self) -> str:
        pass
    
    @abstractmethod
    def construir(self):
        pass
    
    @abstractmethod
    def mostrar(self, page: ft.Page):
        pass

class ControladorAbstrato(ABC):
    def __init__(self, rota: 'Rota'):
        self.rota = rota
    
    @abstractmethod
    def processar_acao(self, acao: str, dados: dict = None):
        pass

# Implementação da Classe Rota
class Rota:
    def __init__(self, primeiro_visualizador: VisualizadorAbstrato, 
                 primeiro_controlador: ControladorAbstrato, 
                 todos_visualizadores: Dict[str, VisualizadorAbstrato], 
                 todos_controladores: Dict[str, ControladorAbstrato]):
        self._atual_visualizador = primeiro_visualizador
        self._atual_controlador = primeiro_controlador
        self._lista_visualizadores = todos_visualizadores
        self._lista_controladores = todos_controladores
        self.page = None
    
    def set_page(self, page: ft.Page):
        self.page = page
    
    def maquina_de_estado(self, input_cliente: str):
        comando = input_cliente
        estado_atual = self._atual_visualizador.nome_da_pagina()
        
        if estado_atual == "pagina_1":
            if comando == "1":
                return "pagina_3"
            elif comando == "2":
                return "pagina_2"
        
        elif estado_atual == "pagina_2":
            if comando == "0":
                return "pagina_1"
        
        elif estado_atual == "pagina_3":
            if comando == "0":
                return "pagina_1"
            elif comando == "1":
                return "pagina_4"
        
        elif estado_atual == "pagina_4":
            if comando == "0":
                return "pagina_3"
        
        return None
    
    def atualizar_estado(self, comando: str):
        proxima_pagina = self.maquina_de_estado(comando)
        if proxima_pagina and proxima_pagina in self._lista_visualizadores:
            self._atual_visualizador = self._lista_visualizadores[proxima_pagina]
            self._atual_controlador = self._lista_controladores[proxima_pagina]
            if self.page:
                self._atual_visualizador.mostrar(self.page)

# Implementação da Página 1
class VisualizadorPagina1(VisualizadorAbstrato):
    def __init__(self):
        self.container = ft.Container()
    
    def nome_da_pagina(self) -> str:
        return "pagina_1"
    
    def construir(self):
        return ft.Column([
            ft.Text("Página 1 - Menu Principal", size=30, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Escolha uma opção:"),
            ft.ElevatedButton("Ir para Página 3", on_click=lambda e: self._on_click(e, "1")),
            ft.ElevatedButton("Ir para Página 2", on_click=lambda e: self._on_click(e, "2")),
        ])
    
    def _on_click(self, e, comando):
        if hasattr(self, 'controlador'):
            self.controlador.processar_acao(comando)
    
    def mostrar(self, page: ft.Page):
        page.clean()
        page.add(self.construir())

class ControladorPagina1(ControladorAbstrato):
    def processar_acao(self, acao: str, dados: dict = None):
        self.rota.atualizar_estado(acao)

# Implementação da Página 2
class VisualizadorPagina2(VisualizadorAbstrato):
    def nome_da_pagina(self) -> str:
        return "pagina_2"
    
    def construir(self):
        return ft.Column([
            ft.Text("Página 2", size=30, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Você está na página 2"),
            ft.ElevatedButton("Voltar para Página 1", on_click=lambda e: self._on_click(e, "0")),
        ])
    
    def _on_click(self, e, comando):
        if hasattr(self, 'controlador'):
            self.controlador.processar_acao(comando)
    
    def mostrar(self, page: ft.Page):
        page.clean()
        page.add(self.construir())

class ControladorPagina2(ControladorAbstrato):
    def processar_acao(self, acao: str, dados: dict = None):
        self.rota.atualizar_estado(acao)

# Implementação da Página 3
class VisualizadorPagina3(VisualizadorAbstrato):
    def nome_da_pagina(self) -> str:
        return "pagina_3"
    
    def construir(self):
        return ft.Column([
            ft.Text("Página 3", size=30, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Você está na página 3"),
            ft.ElevatedButton("Voltar para Página 1", on_click=lambda e: self._on_click(e, "0")),
            ft.ElevatedButton("Ir para Página 4", on_click=lambda e: self._on_click(e, "1")),
        ])
    
    def _on_click(self, e, comando):
        if hasattr(self, 'controlador'):
            self.controlador.processar_acao(comando)
    
    def mostrar(self, page: ft.Page):
        page.clean()
        page.add(self.construir())

class ControladorPagina3(ControladorAbstrato):
    def processar_acao(self, acao: str, dados: dict = None):
        self.rota.atualizar_estado(acao)

# Implementação da Página 4
class VisualizadorPagina4(VisualizadorAbstrato):
    def nome_da_pagina(self) -> str:
        return "pagina_4"
    
    def construir(self):
        return ft.Column([
            ft.Text("Página 4", size=30, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Você chegou na página 4!"),
            ft.Text("Esta é a última página do fluxo"),
            ft.ElevatedButton("Voltar para Página 3", on_click=lambda e: self._on_click(e, "0")),
        ])
    
    def _on_click(self, e, comando):
        if hasattr(self, 'controlador'):
            self.controlador.processar_acao(comando)
    
    def mostrar(self, page: ft.Page):
        page.clean()
        page.add(self.construir())

class ControladorPagina4(ControladorAbstrato):
    def processar_acao(self, acao: str, dados: dict = None):
        self.rota.atualizar_estado(acao)

# Aplicação Principal
def main(page: ft.Page):
    page.title = "App com Arquitetura MVC Adaptada"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.window_width = 400
    page.window_height = 600
    
    # Criar instâncias dos visualizadores
    vis_pag1 = VisualizadorPagina1()
    vis_pag2 = VisualizadorPagina2()
    vis_pag3 = VisualizadorPagina3()
    vis_pag4 = VisualizadorPagina4()
    
    # Criar dicionários
    todos_visualizadores = {
        "pagina_1": vis_pag1,
        "pagina_2": vis_pag2,
        "pagina_3": vis_pag3,
        "pagina_4": vis_pag4
    }
    
    # Criar Rota primeiro (será atualizada depois)
    rota = Rota(vis_pag1, None, todos_visualizadores, {})
    
    # Criar instâncias dos controladores
    ctrl_pag1 = ControladorPagina1(rota)
    ctrl_pag2 = ControladorPagina2(rota)
    ctrl_pag3 = ControladorPagina3(rota)
    ctrl_pag4 = ControladorPagina4(rota)
    
    # Atualizar dicionário de controladores
    todos_controladores = {
        "pagina_1": ctrl_pag1,
        "pagina_2": ctrl_pag2,
        "pagina_3": ctrl_pag3,
        "pagina_4": ctrl_pag4
    }
    
    # Atualizar rota com os controladores
    rota._lista_controladores = todos_controladores
    rota._atual_controlador = ctrl_pag1
    
    # Associar controladores aos visualizadores
    vis_pag1.controlador = ctrl_pag1
    vis_pag2.controlador = ctrl_pag2
    vis_pag3.controlador = ctrl_pag3
    vis_pag4.controlador = ctrl_pag4
    
    # Configurar página na rota
    rota.set_page(page)
    
    # Mostrar página inicial
    vis_pag1.mostrar(page)

# Iniciar o app
if __name__ == "__main__":
    ft.app(target=main)