"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""
from classes.interface import Interface
from classes.repositorio import Repositorio
from classes.visualizador import Visualizador
from classes.controlador import Controlador
from classes.user import User

from abc import ABC, abstractmethod
import datetime
import os

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

class AppContainer():
    def __init__(self):
        usuario = User
        olhos = Visualizador("endereco")
        ouvido = Interface()
        memoria = Repositorio()
        caminho = Controlador(usuario, olhos, ouvido, memoria)
        caminho.funiciona_app()

def main():
    usuario = User("U001","ana.souza@ufmg.br", "Ana Souza")
    olhos = Visualizador("endereco")
    ouvido = Interface()
    memoria = Repositorio()
    caminho = Controlador(usuario, olhos, ouvido, memoria)
    caminho.funiciona_app()
        
        
if __name__ == "__main__":
    main()