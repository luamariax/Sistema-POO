"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

import pandas as pd #biblioteca para manipular dados tabulares
import os #biblioteca para interagir com sistema operacional
import re #biblioteca para padrão de texto
from typing import List, Dict, Optional #biblioteca para anotar tipos no código
import unittest #biblioteca para testes automatizados

#------------------ Novo tipo de erro -------------
class PlanilhaInexistenteError(Exception):
    """Exceção lançada quando se tenta inserir em uma planilha que não existe no arquivo."""
    pass

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
        with pd.ExcelFile(self.caminho) as xls:
            for sheet_name in xls.sheet_names:
                self._planilhas[sheet_name] = pd.read_excel(xls, sheet_name=sheet_name, dtype=str)

    #------ Métodos para gerenciar a planilha ------
    def _salvar_todas_planilhas(self):
        """Sobrescreve o arquivo Excel com todos os DataFrames atuais."""
        with pd.ExcelWriter(self.caminho, engine='openpyxl') as writer:
            for sheet_name, df in self._planilhas.items():
                df.to_excel(writer, sheet_name=sheet_name, index=False)

    def _obter_planilha_obrigatoria(self, nome: str) -> pd.DataFrame:
        """Retorna o DataFrame da planilha especificada ou lança exceção se não existir."""
        df = self._planilhas.get(nome)
        if df is None:
            raise PlanilhaInexistenteError(f"CLASSE:repositorio.py//A planilha '{nome}' não existe no arquivo.")
        return df

    def _gerar_proximo_id(self, df: pd.DataFrame, coluna_id: str, prefixo: str) -> str:
        """
        Gera um novo ID com o prefixo fornecido, baseado no maior valor numérico existente.
        Exemplo: para prefixo 'U', se houver U001, U002, gera 'U003'.
        """
        if df.empty:
            return f"{prefixo}001"
        ids = df[coluna_id].dropna().astype(str)
        numeros = []
        for valor in ids:
            match = re.search(r'\d+', valor)
            if match:
                numeros.append(int(match.group()))
        if not numeros:
            return f"{prefixo}001"
        proximo = max(numeros) + 1
        return f"{prefixo}{proximo:03d}"

    # ------------------- Buscas -------------------
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
    
    # ------------------ MÉTODOS DE CRIAÇÃO ------------------
    # ----------------------- Usúario ------------------------
    def criar_usuario(self, dados: dict) -> str:
        """
        Insere um novo usuário na planilha 'Usuarios'.
        Espera um dicionário com as chaves: email, senha, nome.
        """
        #o criar semestre explica melhor
        obrigatorias = { 'email', 'senha', 'nome'}
        if not obrigatorias.issubset(dados.keys()):
            raise ValueError(f"CLASSE:repositorio.py//Dados incompletos. Campos obrigatórios: {obrigatorias}")
        df = self._planilhas.get('Usuarios')
        if df is None:
            raise ValueError(f"CLASSE:repositorio.py//Planilha não existente.")
        gerada_id_user = self._gerar_proximo_id(df,'id_user','U')
        dados['id_user'] = gerada_id_user
        if dados['id_user'] in df['id_user'].values:
            raise ValueError(f"CLASSE:repositorio.py//Usuário com id_user '{dados['id_user']}' já existe.")
        nova_linha = pd.DataFrame([dados])
        self._planilhas['Usuarios'] = pd.concat([df, nova_linha], ignore_index=True)
        self._salvar_todas_planilhas()
        return gerada_id_user
        
    # ----------------------- Evento ------------------------
    def criar_evento(self, dados: dict) -> str:
        """
        Insere um novo evento na planilha 'Evento'.
        Espera: id_user, descricao, titulo, descrição, data_inicio, data_final, local, organizador.
        """
        #define e verifica se tem os parametros mínimos para criar.
        obrigatorias = { 'id_user', 'titulo', 'descricao', 'data_inicio', 'data_final', 'local', 'organizador'}  
        if not obrigatorias.issubset(dados.keys()):
            raise ValueError(f"CLASSE:repositorio.py//Campos mínimos obrigatórios: {obrigatorias}")
        #pega a planilha geral e verifica se ela existe.
        df_geral = self._planilhas.get('Evento')
        if df_geral is None:
            raise ValueError(f"CLASSE:repositorio.py//Planilha não existente.")
        #Vai especificando o DataFrame pelas ids. 
        df_especifico = df_geral[df_geral['id_user'] == dados['id_user']]
        #Usa o DataFrame específico para gerar a id nova e coloca nos dados.
        gerada_id_evento = self._gerar_proximo_id(df_especifico,'id_evento','E')
        dados['id_evento'] = gerada_id_evento
        #Verifica se a id criada já existe no DataFrame específico.
        if dados['id_evento'] in df_especifico['id_evento'].values:
            raise ValueError(f"CLASSE:repositorio.py//Evento com id_evento '{dados['id_evento']}' já existe.")
        #Cria uma nova linha do DataFrame geral para ser salva como uma nova linha no excel.
        nova_linha = pd.DataFrame([dados])
        self._planilhas['Evento'] = pd.concat([df_geral, nova_linha], ignore_index=True)
        self._salvar_todas_planilhas()
        return gerada_id_evento

    # ----------------------- Semestre ------------------------
    def criar_semestre(self, dados: dict) -> str:
        """
        Insere um novo semestre na planilha 'Semestres'.
        Espera: id_user, titulo (ano-semestre), descrição, ano, semestre_num, ativo.
        """
        #define e verifica se tem os parametros mínimos para criar.
        obrigatorias = { 'id_user', 'titulo', 'descricao', 'ano', 'semestre_num', 'ativo'}  
        if not obrigatorias.issubset(dados.keys()):
            raise ValueError(f"CLASSE:repositorio.py//Campos mínimos obrigatórios: {obrigatorias}")
        #pega a planilha geral e verifica se ela existe.
        df_geral = self._planilhas.get('Semestres')
        if df_geral is None:
            raise ValueError(f"CLASSE:repositorio.py//Planilha não existente.")
        #Vai especificando o DataFrame pelas ids. 
        df_especifico = df_geral[df_geral['id_user'] == dados['id_user']]
        #Usa o DataFrame específico para gerar a id nova e coloca nos dados.
        gerada_id_semestre = self._gerar_proximo_id(df_especifico,'id_semestre','S')
        dados['id_semestre'] = gerada_id_semestre
        #Verifica se a id criada já existe no DataFrame específico.
        if dados['id_semestre'] in df_especifico['id_semestre'].values:
            raise ValueError(f"CLASSE:repositorio.py//Semestre com id_semestre '{dados['id_semestre']}' já existe.")
        #Cria uma nova linha do DataFrame geral para ser salva como uma nova linha no excel.
        nova_linha = pd.DataFrame([dados])
        self._planilhas['Semestres'] = pd.concat([df_geral, nova_linha], ignore_index=True)
        self._salvar_todas_planilhas()
        return gerada_id_semestre

    # ----------------------- Materia ------------------------
    def criar_materia(self, dados: dict) -> str:
        """
        Insere uma nova matéria na planilha 'Materias'.
        Espera no mínimo: id_user, id_semestre, titulo, descricao, professor, sala ,horario.
        """
        #define e verifica se tem os parametros mínimos para criar.
        obrigatorias = { 'id_user', 'id_semestre', 'titulo', 'descricao', 'professor', 'sala' ,'horario'}
        if not obrigatorias.issubset(dados.keys()):
            raise ValueError(f"CLASSE:repositorio.py//Campos mínimos obrigatórios: {obrigatorias}")
        #pega a planilha geral e verifica se ela existe.
        df_geral = self._planilhas.get('Materias')
        if df_geral is None:
            raise ValueError(f"CLASSE:repositorio.py//Planilha não existente.")
        #Vai especificando o DataFrame pelas ids. 
        df_especifico = df_geral[(df_geral['id_user'] == dados['id_user']) & (df_geral['id_semestre'] == dados['id_semestre'])]
        #Usa o DataFrame específico para gerar a id nova e coloca nos dados.
        gerada_id_materia = self._gerar_proximo_id(df_especifico,'id_materia','M')
        dados['id_materia'] = gerada_id_materia
        #Verifica se a id criada já existe no DataFrame específico.
        if dados['id_materia'] in df_especifico['id_materia'].values:
            raise ValueError(f"CLASSE:repositorio.py//Matéria com id_materia '{dados['id_materia']}' já existe.")
        #Cria uma nova linha do DataFrame geral para ser salva como uma nova linha no excel.
        nova_linha = pd.DataFrame([dados])
        self._planilhas['Materias'] = pd.concat([df_geral, nova_linha], ignore_index=True)
        self._salvar_todas_planilhas()
        return gerada_id_materia

    # ----------------------- Prova ------------------------
    def criar_prova(self, dados: dict) -> str:
        """
        Insere uma nova prova na planilha 'Provas'.
        Espera no mínimo: id_user, id_semestre, id_materia, valor_nota, 
        nota_obtida, titulo, dia , conteudo, sala, duracao.
        """
        #define e verifica se tem os parametros mínimos para criar.
        obrigatorias = { 'id_user', 'id_semestre', 'id_materia', 'valor_nota', 'nota_obtida', 'titulo', 'dia' , 'conteudo', 'sala', 'duracao'}
        if not obrigatorias.issubset(dados.keys()):
            raise ValueError(f"CLASSE:repositorio.py//Campos mínimos obrigatórios: {obrigatorias}")
        #pega a planilha geral e verifica se ela existe.
        df_geral = self._planilhas.get('Provas')
        if df_geral is None:
            raise ValueError(f"CLASSE:repositorio.py//Planilha não existente.")
        #Vai especificando o DataFrame pelas ids. 
        df_especifico = df_geral[(df_geral['id_user'] == dados['id_user']) & 
                       (df_geral['id_semestre'] == dados['id_semestre']) & 
                       (df_geral['id_materia'] == dados['id_materia'])]
        #Usa o DataFrame específico para gerar a id nova e coloca nos dados.
        gerada_id_prova = self._gerar_proximo_id(df_especifico,'id_prova','P')
        dados['id_prova'] = gerada_id_prova
        #Verifica se a id criada já existe no DataFrame específico.
        if dados['id_prova'] in df_especifico['id_prova'].values:
            raise ValueError(f"CLASSE:repositorio.py//Provas com id_prova '{dados['id_prova']}' já existe.")
        #Cria uma nova linha do DataFrame geral para ser salva como uma nova linha no excel.
        nova_linha = pd.DataFrame([dados])
        self._planilhas['Provas'] = pd.concat([df_geral, nova_linha], ignore_index=True)
        self._salvar_todas_planilhas()
        return gerada_id_prova
    
    # --------------------- Trabalho ------------------------
    def criar_trabalho(self, dados: dict) -> str:
        """
        Insere uma novo trabalho na planilha 'Trabalhos'.
        Espera no mínimo: id_user, id_semestre, id_materia, valor_nota, 
        nota_obtida, titulo, data_entrega, descricao_tarefa, grupo, entregue.
        """
        #define e verifica se tem os parametros mínimos para criar.
        obrigatorias = { 'id_user', 'id_semestre', 'id_materia','valor_nota', 'nota_obtida', 'titulo','data_entrega', 'descricao_tarefa', 'grupo', 'entregue'}
        if not obrigatorias.issubset(dados.keys()):
            raise ValueError(f"CLASSE:repositorio.py//Campos mínimos obrigatórios: {obrigatorias}")
        #pega a planilha geral e verifica se ela existe.
        df_geral = self._planilhas.get('Trabalhos')
        if df_geral is None:
            raise ValueError(f"CLASSE:repositorio.py//Planilha não existente.")
        #Vai especificando o DataFrame pelas ids. 
        df_especifico = df_geral[(df_geral['id_user'] == dados['id_user']) & 
                       (df_geral['id_semestre'] == dados['id_semestre']) & 
                       (df_geral['id_materia'] == dados['id_materia'])]
        #Usa o DataFrame específico para gerar a id nova e coloca nos dados.
        gerada_id_trabalho = self._gerar_proximo_id(df_especifico,'id_trabalho','T')
        dados['id_trabalho'] = gerada_id_trabalho
        #Verifica se a id criada já existe no DataFrame específico.
        if dados['id_trabalho'] in df_especifico['id_trabalho'].values:
            raise ValueError(f"CLASSE:repositorio.py//Trabalho com id_trabalho '{dados['id_trabalho']}' já existe.")
        #Cria uma nova linha do DataFrame geral para ser salva como uma nova linha no excel.
        nova_linha = pd.DataFrame([dados])
        self._planilhas['Trabalhos'] = pd.concat([df_geral, nova_linha], ignore_index=True)
        self._salvar_todas_planilhas()
        return gerada_id_trabalho


    #------------------------- Editar -------------------------
    # ----------------------- Usúario ------------------------
    def editar_usuario(self, dados: dict):#Não ta pronto
        pass
        
    # ----------------------- Evento ------------------------
    def editar_evento(self, dados: dict):#Não ta pronto
        pass

    # ----------------------- Semestre ------------------------
    def editar_semestre(self, dados: dict): # Tá PRONTISSIMO
        """
        Modifica os valores de um semestre já existente na planilha 'Semestres'.
        Espera: id_user, id_semestre, titulo (ano-semestre), descrição, ano, semestre_num, ativo.
        """
        #define e verifica se tem os parametros mínimos para criar.
        obrigatorias = { 'id_user', 'id_semestre', 'titulo', 'descricao', 'ano', 'semestre_num', 'ativo'}  
        if not obrigatorias.issubset(dados.keys()):
            raise ValueError(f"CLASSE:repositorio.py//Campos mínimos obrigatórios: {obrigatorias}")
        #pega a planilha geral e verifica se ela existe.
        df_geral = self._planilhas.get('Semestres')
        if df_geral is None:
            raise ValueError(f"CLASSE:repositorio.py//Planilha não existente.")
        #Vai especificando o DataFrame pelas ids. 
        df_especifico = df_geral[(df_geral['id_user'] == dados['id_user']) & 
                                 (df_geral['id_semestre'] == dados['id_semestre'])]
        #Verifica se o semestre não existe no DataFrame específico.
        if not df_especifico:
            raise ValueError(f"CLASSE:repositorio.py//Semestre com id_semestre '{dados['id_semestre']}' não existe.")
        #modifica item por item no DataFrame original para ser salva no excel.
        self._planilhas['Semestres'][(self._planilhas['Semestres']['id_user'] == dados['id_user']) & 
                                     (self._planilhas['Semestres']['id_semestre'] == dados['id_semestre'])]['titulo'] = dados['titulo']
        
        self._planilhas['Semestres'][(self._planilhas['Semestres']['id_user'] == dados['id_user']) & 
                                     (self._planilhas['Semestres']['id_semestre'] == dados['id_semestre'])]['ano'] = dados['ano']
        
        self._planilhas['Semestres'][(self._planilhas['Semestres']['id_user'] == dados['id_user']) & 
                                     (self._planilhas['Semestres']['id_semestre'] == dados['id_semestre'])]['semestre_num'] = dados['semestre_num']
        
        self._planilhas['Semestres'][(self._planilhas['Semestres']['id_user'] == dados['id_user']) & 
                                     (self._planilhas['Semestres']['id_semestre'] == dados['id_semestre'])]['descricao'] = dados['descricao']
        
        self._planilhas['Semestres'][(self._planilhas['Semestres']['id_user'] == dados['id_user']) & 
                                     (self._planilhas['Semestres']['id_semestre'] == dados['id_semestre'])]['ativo'] = dados['ativo']
        
        self._salvar_todas_planilhas()

    # ----------------------- Materia ------------------------
    def editar_materia(self, dados: dict):#Não ta pronto
        pass

    # ----------------------- Prova ------------------------
    def editar_prova(self, dados: dict):#Não ta pronto
        pass
    
    # --------------------- Trabalho ------------------------
    def editar_trabalho(self, dados: dict): #Não ta pronto
        pass



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
    teste_1 = repo.buscar_semestres_por_usuario('U001')
    teste_2 = repo.buscar_materias_por_semestre_usuario('U001','S001')
    teste_3 = repo.buscar_provas_por_materia_semestre_usuario('U001','S001', 'M001')
    teste_4 = repo._planilhas['Usuarios']
    todos_testes = [teste_0,teste_1,teste_2,teste_3, teste_4]
    if num < len(todos_testes):
        for linha in todos_testes[num]:
            print(linha)
    else:
        print('teste não encontrado')

def TesteSaida(num):
    repo = Repositorio("Arquivo.xlsx")
    teste_0 = repo.buscar_materias_por_semestre_usuario('U001','S001')[0]['id_materia']
    teste_1 = repo.buscar_usuario_por_email('ana.souza@ufmg.br')['id_user']
    teste_2 = repo.buscar_semestres_por_usuario('U001')[0]['id_semestre']
    todos_testes = [teste_0, teste_1, teste_2]
    print(todos_testes[num])

def TesteCadastro():
    repo = Repositorio("Arquivo.xlsx")
    dic_usuario = {
        "nome": "Testador",
        "email": "teste@ufmg.br",
        "senha": "1234"
    }
    repo.criar_usuario(dic_usuario)
    id_usuario = repo.buscar_usuario_por_email(dic_usuario['email'])['id_user']
    dic_semestre = { 'id_user': id_usuario, 
                    'titulo': '2026-1', 
                    'descricao': 'Engenharia de Sistemas', 
                    'ano': '2026', 
                    'semestre_num': '1', 
                    'ativo': 'True'}
    repo.criar_semestre(dic_semestre)
    id_sem = repo.buscar_semestres_por_usuario(id_usuario)[0]['id_semestre']
    dic_materia = { 'id_user': id_usuario, 
                   'id_semestre': id_sem, 
                   'titulo': 'APPOO', 
                   'descricao': 'Análise e Projeto em Programação Orientada a Objetos', 
                   'professor': 'Luiza', 
                   'sala': '3015 BL3',
                   'horario': 'TER-19h/QUI-20h55'}
    repo.criar_materia(dic_materia)
    id_mat = repo.buscar_materias_por_semestre_usuario(id_usuario,id_sem)[0]['id_materia']
    dic_prova = { 'id_user': id_usuario, 
                    'id_semestre': id_sem, 
                    'id_materia': id_mat, 
                    'valor_nota': 20, 
                    'nota_obtida': None, 
                    'titulo': 'Prova 1', 
                    'dia': '2026-07-04', 
                    'conteudo': 'Herança, Polimorfia, Classe Abstrata', 
                    'sala': '3015 BL3', 
                    'duracao': '1h40'}
    repo.criar_prova(dic_prova)
    id_pro = repo.buscar_provas_por_materia_semestre_usuario(id_usuario,id_sem,id_mat)[0]['id_prova']
    todos_id = [id_usuario, id_sem, id_mat, id_pro]
    print(todos_id)



if __name__ == '__main__':
    #unittest.main()
    Teste(3)