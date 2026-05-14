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

class Interface:
    def __init__(self):
        self.exbicao_atual = "pagina_inicial.txt"
    
    def capiturar_comando_usuario(self):
        resposta = input("Digite aqui o comando: ")
        if resposta.strip():
            return f"VALIDO#{resposta}"
        else:
            return f"ERRADO# vazio é uma resposta invalida"
