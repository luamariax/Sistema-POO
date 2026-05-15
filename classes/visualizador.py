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
        self.dados_necessarios = pd.DataFrame()

    def mostrar_exibicao(self):
        os.system('clear')
        try:
            with open(f"classes/paginas/{self.exbicao_atual}", 'r', encoding='utf-8') as texto:
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
        self.exibicao_erro = erro_capiturado
        
    
    def atualizar_dados(self, dados_coletados: pd.DataFrame):
        self.dados_necessarios = dados_coletados

    def exibir_dados(self):
        if not self.dados_necessarios.empity():
            if self.exbicao_atual == "pagina_todos_eventos.txt":
                lista_de_eventos  = self.dados_necessarios
                id_usuario = lista_de_eventos["id_user"][0]
                if lista_de_eventos.empty:
                    print(f"Nenhum evento encontrado para o usuário {id_usuario}.")
                print(f"\nEventos do usuario {id_usuario}:")
                for indice, linha in lista_de_eventos.iterrows():
                    numero_da_escolha = indice+1
                    nome_do_evento = linha["titulo"]
                    print(f"{numero_da_escolha} -semestre de {nome_do_evento}.")
            
            elif self.exbicao_atual == "pagina_todos_semestres.txt":
                lista_de_semestres  = self.dados_necessarios
                id_usuario = lista_de_semestres["id_user"][0]
                if lista_de_semestres.empty:
                    print(f"Nenhum semestre encontrado para o usuário {id_usuario}.")
                print(f"\nSemestres do usuario {id_usuario}:")
                for indice, linha in lista_de_semestres.iterrows():
                    numero_da_escolha = indice+1
                    id_semestre = linha["titulo"]
                    descricao_do_semestre = linha["descricao"]
                    print(f"{numero_da_escolha} -semestre de {id_semestre} do curso de {descricao_do_semestre}.")

            elif self.exbicao_atual == "pagina_evento_especifico.txt":
                evento  = self.dados_necessarios
                id_usuario = evento["id_user"][0]
                if evento.empty:
                    print(f"Nenhum evento encontrado para o usuário {id_usuario}.")
                print(f"\nDestalhamento do evento:")
                indice_do_evento = evento.index[0]
                nome_do_evento_atual = evento["titulo"][0]
                descricao_do_evento = evento["descricao"][0]
                data_inicio_do_evento = evento["data_inicio"][0]
                data_final_do_evento = evento["data_final"][0]
                horario_do_evento = evento["horario"][0]
                local_do_evento = evento["local"][0]
                organizador_do_evento = evento["organizador"][0]
                print(f"indice_do_evento -- {indice_do_evento}.")
                print(f"descricao_do_evento -- {descricao_do_evento}")
                print(f"data_inicio_do_evento -- {data_inicio_do_evento}")
                print(f"nome_do_evento_atual -- {nome_do_evento_atual}")
                print(f"data_final_do_evento -- {data_final_do_evento}")
                print(f"horario_do_evento -- {horario_do_evento}")
                print(f"local_do_evento -- {local_do_evento}")
                print(f"organizador_do_evento -- {organizador_do_evento}")

            elif self.exbicao_atual == "pagina_semestre_especifico.txt":
                lista_de_materias  = self.dados_necessarios
                id_usuario = lista_de_materias["id_user"][0]
                if lista_de_materias.empty:
                    print(f"Nenhuma materia encontrada nesse semestre para o usuário {id_usuario}.")
                print(f"\nO semestre de {id_semestre} do curso de {descricao_do_semestre}")
                print(f"tem as seguintes materias cursadas pelo usuario {id_usuario}:")
                for indice, linha in lista_de_materias.iterrows():
                    numero_da_escolha = indice+1
                    titulo_materia = linha["titulo"]
                    print(f"{numero_da_escolha} - {titulo_materia}.")

            elif self.exbicao_atual == "pagina_materia.txt":
                materia = self.dados_necessarios
                id_user_da_materia = materia["id_user"][0]
                id_semestre_da_materia = materia["id_semestre"][0]
                id_materia_da_materia = materia["id_materia"][0]
                titulo_da_materia = materia["titulo"][0]
                descricao_da_materia = materia["descricao"][0]
                professor_da_materia = materia["professor"][0]
                sala_da_materia = materia["sala"][0]
                horario_da_materia = materia["horario"][0]
                print(f"id_user_da_materia - {id_user_da_materia}.")
                print(f"id_semestre_da_materia - {id_semestre_da_materia}.")
                print(f"id_materia_da_materia - {id_materia_da_materia}.")
                print(f"titulo_da_materia - {titulo_da_materia}.")
                print(f"descricao_da_materia - {descricao_da_materia}.")
                print(f"professor_da_materia - {professor_da_materia}.")
                print(f"sala_da_materia - {sala_da_materia}.")
                print(f"horario_da_materia - {horario_da_materia}.")