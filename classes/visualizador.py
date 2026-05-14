"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

from abc import ABC, abstractmethod
import datetime
import os
import openpyxl
import pandas

pd = pandas

class Visualizador:
    def __init__(self, endereco_exbicoes : str):
        self.endereco_exbicoes = endereco_exbicoes
        self.exbicao_atual = "pagina_inicial.txt"
        self.exibicao_erro = " "
        if not os.path.exists(self.exbicao_atual):
            with open(self.exbicao_atual, 'w', encoding='utf-8') as texto:
                pass
    
    def mostrar_exibicao(self):
        os.system('clear')
        try:
            with open(self.exbicao_atual, 'r', encoding='utf-8') as texto:
                for linha in texto:
                    print(linha)
        except Exception as erro:
            print(f"Erro ao ler arquivo: {erro}")
    
    def mostrar_erro(self):
        if self.exibicao_erro.strip():
            print(self.exibicao_erro)
    
    def atualizar_exibicao(self, proxima_exbicao: str, erro_capiturado:str):
        if proxima_exbicao.strip():
            self.exbicao_atual = proxima_exbicao
            if not os.path.exists(proxima_exbicao):
                with open(proxima_exbicao, 'w', encoding='utf-8') as texto:
                    pass
        self.exibicao_erro = erro_capiturado