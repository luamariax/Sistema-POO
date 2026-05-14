"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""
from classes.interface import Interface
from classes.repositorio import Repositorio
from classes.visualizador import Visualizador
from classes.controlador import Controlador

from abc import ABC, abstractmethod
import datetime
import os
import openpyxl
import pandas

pd = pandas

"""
def funiciona_app(self):
    while self.sessao_ativa:
        self.acesso_visualizador.mostrar_exibicao()
        self.acesso_visualizador.mostrar_erro()
        entrada = self.acesso_interface.capiturar_comando_usuario()
        self.atualizar_app(entrada)
"""        

def main():
    usuario = "123"
    olhos = Visualizador("endereco")
    ouvido = Interface()
    memoria = Repositorio()
    caminho = Controlador(usuario, olhos, ouvido, memoria)
    caminho.funiciona_app()
        
        
if __name__ == "__main__":
    main()