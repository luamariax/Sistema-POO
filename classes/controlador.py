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

    def criar_sessao(self, nova_id_usuario: str):
        self.user = nova_id_usuario

    def navegar_pelo_app(self, input_cliente: str):
        comando =int(input_cliente)
        estado_atual = self.acesso_visualizador.exbicao_atual
        
        if estado_atual == "pagina_inicial.txt":
            if comando == 1:
                return "pagina_cadastro.txt"
            elif comando == 2:
                return "pagina_login.txt"
        
        elif estado_atual == "pagina_login.txt":
            if comando == 0:
                return "pagina_inicial.txt"
            elif comando == 1:
                return "pagina_entrada.txt"
        
        elif estado_atual == "pagina_cadastro.txt":
            if comando == 0:
                return "pagina_inicial.txt"
            elif comando == 1:
                return "pagina_inicial.txt"
        
        elif estado_atual == "pagina_entrada.txt":
            if comando == 0:
                return "pagina_login.txt"
            elif comando == 1 :
                return "pagina_todos_semestres.txt"
            elif comando == 2:
                return "pagina_todos_eventos.txt"
            
        elif estado_atual == "pagina_todos_semestres.txt":
            if comando == 0:
                return "pagina_entrada.txt"
            elif comando > 0:
                return "pagina_semestre_especifico.txt"
        
        elif estado_atual == "pagina_todos_eventos.txt":
            if comando == 0:
                return "pagina_entrada.txt"
            elif comando > 0 :
                return "pagina_evento_especifico.txt"
        
        elif estado_atual == "pagina_evento_especifico.txt":
            if comando == 0:
                return "pagina_todos_eventos.txt"
        
        elif estado_atual == "pagina_semestre_especifico.txt":
            if comando == 0:
                return "pagina_todos_semestres.txt"
            elif comando :
                return "pagina_materia.txt"
        
        elif estado_atual == "pagina_materia.txt":
            if comando == 0:
                return "pagina_semestre_especifico.txt"

        
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
