"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

import pandas as pd
import os
from typing import List, Dict, Optional
import unittest
#---------------------- Repositorio ---------------
class Repositorio:
    def __init__(self, caminho_arquivo: str):
        """
        Recebe como parâmetro o caminho do arquivo excel onde fica salvo os dados.
        Tem um atributo _planilhas que guarda as páginas do arquivo excel pelo nome da página.
        """
        self.caminho = caminho_arquivo
        self._planilhas: Dict[str, pd.DataFrame] = {}
        self._carregar_dados()

    def _carregar_dados(self):
        """Carrega todas as planilhas do arquivo Excel em um dicionário de DataFrames."""
        if not os.path.exists(self.caminho):
            raise FileNotFoundError(f"Arquivo {self.caminho} não encontrado.")
        # Lê todas as planilhas de uma vez
        with pd.ExcelFile(self.caminho) as xls:
            for sheet_name in xls.sheet_names:
                self._planilhas[sheet_name] = pd.read_excel(xls, sheet_name=sheet_name, dtype=str)

    # ------------------ Usuários ------------------
    def buscar_usuario_por_email(self, email: str) -> Optional[Dict]:
        """Busca um usuário pelo email na planilha 'Usuarios'. Retorna um dicionário ou None."""
        df = self._planilhas.get('Usuarios')
        if df is None:
            return None
        resultado = df[df['email'] == email]
        if resultado.empty:
            return None
        return resultado.iloc[0].to_dict()

    # ------------------ Eventos ------------------
    def buscar_eventos_por_usuario(self, id_user: str) -> List[Dict]:
        """
        Retorna uma lista de dicionários com todos os eventos de um usuário.
        Cada dicionário representa uma linha da planilha 'Eventos'.
        """
        df = self._planilhas.get('Eventos')
        if df is None:
            return []
        registros = df[df['id_user'] == id_user]
        return registros.to_dict('records')

    # ------------------ Semestres ------------------
    def buscar_semestres_por_usuario(self, id_user: str) -> List[Dict]:
        """
        Retorna uma lista de dicionários com todos os semestres de um usuário.
        Cada dicionário representa uma linha da planilha 'Semestres'.
        """
        df = self._planilhas.get('Semestres')
        if df is None:
            return []
        registros = df[df['id_user'] == id_user]
        return registros.to_dict('records')

    # ------------------ Matérias ------------------
    def buscar_materias_por_semestre_usuario(self, id_user: str, id_semestre: str) -> List[Dict]:
        """
        Retorna uma lista de dicionários com todas as matérias de um usuário em um semestre específico.
        Cada dicionário representa uma linha da planilha 'Materias'.
        """
        df = self._planilhas.get('Materias')
        if df is None:
            return []
        registros = df[(df['id_user'] == id_user) & (df['id_semestre'] == id_semestre)]
        return registros.to_dict('records')

    # ------------------ Provas ------------------
    def buscar_provas_por_materia_semestre_usuario(self, id_user: str, id_semestre: str, id_materia: str) -> List[Dict]:
        """
        Retorna uma lista de dicionários com todas as provas de um usuário, em um semestre e matéria específicos.
        Cada dicionário representa uma linha da planilha 'Provas'.
        """
        df = self._planilhas.get('Provas')
        if df is None:
            return []
        registros = df[(df['id_user'] == id_user) & 
                       (df['id_semestre'] == id_semestre) & 
                       (df['id_materia'] == id_materia)]
        return registros.to_dict('records')
    
    # ------------------ Provas ------------------
    def buscar_trabalhos_por_materia_semestre_usuario(self, id_user: str, id_semestre: str, id_materia: str) -> List[Dict]:
        """
        Retorna uma lista de dicionários com todas os trabalhos de um usuário, em um semestre e matéria específicos.
        Cada dicionário representa uma linha da planilha 'Trabalhos'.
        """
        df = self._planilhas.get('Trabalhos')
        if df is None:
            return []
        registros = df[(df['id_user'] == id_user) & 
                       (df['id_semestre'] == id_semestre) & 
                       (df['id_materia'] == id_materia)]
        return registros.to_dict('records')
    

#--------------------- Teste -----------------------
class TestRepositorioMultiSheet(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Cria um arquivo Excel temporário com múltiplas planilhas
        cls.temp_file = "test_database.xlsx"
        with pd.ExcelWriter(cls.temp_file) as writer:
            pd.DataFrame({
                'id_user': ['U001', 'U002'],
                'email': ['ana@ufmg.br', 'joao@email.com'],
                'senha': ['123', '456'],
                'nome': ['Ana', 'João']
            }).to_excel(writer, sheet_name='Usuarios', index=False)

            pd.DataFrame({
                'id_semestre': ['S001', 'S002', 'S003'],
                'id_user': ['U001', 'U001', 'U002'],
                'descricao': ['2024/1', '2024/2', '2023/2'],
                'ano': ['2024', '2024', '2023'],
                'periodo': ['1', '2', '2']
            }).to_excel(writer, sheet_name='Semestres', index=False)

            pd.DataFrame({
                'id_materia': ['M001', 'M002'],
                'id_user': ['U001', 'U001'],
                'id_semestre': ['S001', 'S001'],
                'nome': ['Cálculo I', 'Física I'],
                'professor': ['Carlos', 'Mariana']
            }).to_excel(writer, sheet_name='Materias', index=False)

            pd.DataFrame({
                'id_prova': ['P001', 'P002'],
                'id_user': ['U001', 'U001'],
                'id_semestre': ['S001', 'S001'],
                'id_materia': ['M001', 'M001'],
                'data': ['2024-03-15', '2024-04-20'],
                'nota': ['8.5', '7.0']
            }).to_excel(writer, sheet_name='Provas', index=False)

        cls.repo = Repositorio(cls.temp_file)

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.temp_file)

    def test_buscar_usuario_por_email_existente(self):
        user = self.repo.buscar_usuario_por_email('ana@ufmg.br')
        self.assertIsNotNone(user)
        self.assertEqual(user['id_user'], 'U001')

    def test_buscar_semestres_por_usuario(self):
        semestres = self.repo.buscar_semestres_por_usuario('U001')
        self.assertEqual(len(semestres), 2)
        self.assertEqual(semestres[0]['id_semestre'], 'S001')

    def test_buscar_materias_por_semestre_usuario(self):
        materias = self.repo.buscar_materias_por_semestre_usuario('U001', 'S001')
        self.assertEqual(len(materias), 2)
        self.assertEqual(materias[0]['nome'], 'Cálculo I')

    def test_buscar_provas_por_materia_semestre_usuario(self):
        provas = self.repo.buscar_provas_por_materia_semestre_usuario('U001', 'S001', 'M001')
        self.assertEqual(len(provas), 2)
        self.assertEqual(provas[0]['nota'], '8.5')

    def test_buscar_semestres_usuario_inexistente(self):
        semestres = self.repo.buscar_semestres_por_usuario('U999')
        self.assertEqual(semestres, [])

def Teste(num):
    repo = Repositorio("Arquivo.xlsx")
    teste_0 = repo.buscar_usuario_por_email('ana.souza@ufmg.br')
    teste_1 = repo.buscar_eventos_por_usuario('U001')
    teste_2 = repo.buscar_materias_por_semestre_usuario('U001','2026-1')
    teste_3 = repo.buscar_provas_por_materia_semestre_usuario('U001','2026-1', 'DCC001')
    todos_testes = [teste_0,teste_1,teste_2,teste_3]
    if num < len(todos_testes):
        for linha in todos_testes[num]:
            print(linha)
    else:
        print('teste não encontrado')

if __name__ == '__main__':
    #unittest.main()
    Teste(3)