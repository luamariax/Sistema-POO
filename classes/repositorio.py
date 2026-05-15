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

class Repositorio():
    def __init__(self):
        self.base_de_dados = "Arquivo.xlsx"

    def buscar_dados(self, tipo_de_classe:str, ids_referentes):
        """
            a ids_referentes pode variar de tamanho, sendo de 1 a 4
            e pode assumir os seguintes valores nessa ordem específica
            ["id_user", "id_semestre", "id_materia", "titulo"]
        """
        resposta_da_funcao = pd.DataFrame()
        tipos_possiveis_de_classe = ["Eventos", "Semestres", "Materias", "Provas", "Trabalhos"]
        id_user = ids_referentes[0]
        if not tipo_de_classe in tipos_possiveis_de_classe:
            erro = [{"erro": "ERRADO# no buscar_dados o tipo_de_classe invalido"}]
            resposta_da_funcao = pd.DataFrame(erro)
        
        if len(ids_referentes) == 1:
            if tipo_de_classe == "Eventos":
                data_frame = pd.read_excel(self.base_de_dados, sheet_name="Eventos") 
                resposta_da_funcao = data_frame[data_frame["id_user"] == id_user]
            elif tipo_de_classe == "Semestres":
                data_frame = pd.read_excel(self.base_de_dados, sheet_name="Semestres")
                resposta_da_funcao = data_frame[data_frame["id_user"] == id_user]
        
        elif len(ids_referentes) == 2:
            if tipo_de_classe == "Materias":
                data_frame = pd.read_excel(self.base_de_dados, sheet_name="Materias")
                resposta_da_funcao = data_frame[data_frame["id_user"] == id_user]
        
        elif len(ids_referentes) == 3:
            if tipo_de_classe == "Provas":
                data_frame = pd.read_excel(self.base_de_dados, sheet_name="Provas")
                resposta_da_funcao = data_frame[data_frame["id_user"] == id_user]
            elif tipo_de_classe == "Trabalhos":
                data_frame = pd.read_excel(self.base_de_dados, sheet_name="Trabalhos")
                resposta_da_funcao = data_frame[data_frame["id_user"] == id_user]

        return resposta_da_funcao
                    
    def login(self, input_email: str, input_senha: str):
        data_frame = pd.read_excel("Arquivo.xlsx", sheet_name="Usuarios")

        id_user_encontrado = data_frame[data_frame["email"].str.lower() == input_email]
        if id_user_encontrado.empty:
            print("E-mail não encontrado")
            return None

        linha = id_user_encontrado[id_user_encontrado["senha"] == input_senha]
        if linha.empty:
            print("Senha incorreta.")
            return None
        
        id_user = linha.iloc[0]["id_user"]
        print(f"Login bem-sucedido! Bem-vind@ {linha.iloc[0]['nome']}!")
        return id_user
    


def teste_de_classe():
    teste_id_user = "U001"
    teste_ids = [teste_id_user]
    classe_a_ser_testada = Repositorio()
    teste_data_frame_1 = classe_a_ser_testada.buscar_dados("Semestres",teste_ids)
    print(teste_data_frame_1)

teste_de_classe()