
"""
padrões de escrita
classe usa PascalCase
função e variáveis usa snake_case
"""

from .ControladorAbstrato import ControladorAbstrato
from Modelos.Servico import Servico


class ControladorMateria(ControladorAbstrato):
    def __init__(self, rota, servico: Servico, visualizador):
        super().__init__(rota, servico, visualizador)
        self.visualizador.controlador = self 

    def carregar_dados_para_tela(self):
        materia = self.servico._objetos_do_usuario
        if not materia:
            return

        self.visualizador.titulo_materia = materia.titulo
        self.visualizador.professor = materia.professor
        self.visualizador.sala = materia.sala
        self.visualizador.horarios = materia.horarios

        # Busca as Provas
        try:
            self.visualizador.lista_provas = self.servico.repositorio.buscar_provas_por_materia_semestre_usuario(
                self.servico.id_user_logado,
                self.servico.id_semestre_logado,
                self.servico.id_materia_logado
            )
        except Exception as e:
            self.visualizador.lista_provas = []

        # Busca os Trabalhos
        try:
            self.visualizador.lista_trabalhos = self.servico.repositorio.buscar_trabalhos_por_materia_semestre_usuario(
                self.servico.id_user_logado,
                self.servico.id_semestre_logado,
                self.servico.id_materia_logado
            )
        except Exception as e:
            self.visualizador.lista_trabalhos = []

        #Função calcular_nota() executada dinamicamente
        soma_notas = 0.0
        
        # Soma as notas das provas
        for p in self.visualizador.lista_provas:
            nota = p.get('nota_obtida')
            # Garante que não é vazio, nulo ou a string 'None'
            if nota and str(nota).strip() not in ['None', '', 'nan']:
                try: soma_notas += float(nota)
                except ValueError: pass # Ignora se houver algum erro de digitação no Excel
                
        # Soma as notas dos trabalhos
        for t in self.visualizador.lista_trabalhos:
            nota = t.get('nota_obtida')
            if nota and str(nota).strip() not in ['None', '', 'nan']:
                try: soma_notas += float(nota)
                except ValueError: pass

        # Envia o total para a tela!
        self.visualizador.nota_total = soma_notas

    def processar_acao(self, acao: str, dados: dict = None):
        if acao == "0":
            self.servico.retirar_objeto('Materia')
            self.rota.atualizar_estado("0")
            
        elif acao == "salvar_nova_prova":
            if dados:
                dados['id_user'] = self.servico.id_user_logado
                dados['id_semestre'] = self.servico.id_semestre_logado
                dados['id_materia'] = self.servico.id_materia_logado
                dados['nota_obtida'] = None
                
                self.servico.repositorio.criar_prova(dados)
                self.carregar_dados_para_tela()
                if self.rota.page:
                    self.visualizador.mostrar(self.rota.page)
                    
        elif acao == "salvar_novo_trabalho":
            if dados:
                dados['id_user'] = self.servico.id_user_logado
                dados['id_semestre'] = self.servico.id_semestre_logado
                dados['id_materia'] = self.servico.id_materia_logado
                dados['nota_obtida'] = None
                dados['entregue'] = "False"
                
                self.servico.repositorio.criar_trabalho(dados)
                self.carregar_dados_para_tela()
                if self.rota.page:
                    self.visualizador.mostrar(self.rota.page)