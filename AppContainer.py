"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

from abc import ABC, abstractmethod
import datetime
import os


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
        
    
class Interface:
    def __init__(self):
        self.exbicao_atual = "pagina_inicial.txt"
    
    def capiturar_comando_usuario(self):
        resposta = input("Digite aqui o comando: ")
        if resposta.strip():
            return f"VALIDO#{resposta}"
        else:
            return f"ERRADO# vazio é uma resposta invalida"


class Controlador:
    def __init__(self, id_usuario: str, janela_para_ver:Visualizador, ouvido_para_ouvir:Interface):
        self.user = id_usuario
        self.sessao_ativa = True
        self.acesso_visualizador = janela_para_ver
        self.acesso_interface = ouvido_para_ouvir

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
        

def main():
    usuario = "123"
    janela = Visualizador("endereco")
    ouvido = Interface()
    caminho = Controlador(usuario, janela, ouvido)
    caminho.funiciona_app()
        
        
if __name__ == "__main__":
    main()