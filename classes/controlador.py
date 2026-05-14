"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""
from .interface import Interface
from .repositorio import Repositorio
from .visualizador import Visualizador

from abc import ABC, abstractmethod
import datetime
import os
import openpyxl
import pandas

pd = pandas


class Controlador:
    def __init__(self, id_usuario: str, janela_para_ver:Visualizador, ouvido_para_ouvir:Interface, memoria_para_lembrar: Repositorio):
        self.user = id_usuario
        self.sessao_ativa = True
        self.acesso_visualizador = janela_para_ver
        self.acesso_interface = ouvido_para_ouvir
        self.acesso_repositorio = memoria_para_lembrar

    def interpretar_comando(self, validade):
        if validade == "VALIDO#":      
            return True
        elif validade == "ERRADO#":
            return False

    def navegar_pelo_app(self, comando):
        estado_atual = self.acesso_visualizador.exbicao_atual
        if estado_atual == "pagina_inicial.txt":
            if comando == "ok":
                return "pagina_segunda.txt"
        elif estado_atual == "pagina_segunda.txt":
            if comando == "ok":
                return "pagina_inicial.txt"
        return " "

    def atualizar_app(self, entrada):
        validade = entrada[:7]
        comando = entrada[7:]
        if self.interpretar_comando(validade):
            if comando == "desliga":
                self.sessao_ativa = False
            else:
                proxima_exibicao = self.navegar_pelo_app(comando)
                if proxima_exibicao.strip():
                    self.acesso_visualizador.atualizar_exibicao(proxima_exibicao, " ")
                else:
                    self.acesso_visualizador.atualizar_exibicao(proxima_exibicao, f"comando '{comando}' não encontrado")
        else:
            self.acesso_visualizador.atualizar_exibicao(" ", comando)


    def funiciona_app(self):
        while self.sessao_ativa:
            self.acesso_visualizador.mostrar_exibicao()
            self.acesso_visualizador.mostrar_erro()
            entrada = self.acesso_interface.capiturar_comando_usuario()
            self.atualizar_app(entrada)
