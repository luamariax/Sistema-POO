"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

""""
from .ControladorAbstrato import ControladorAbstrato

#import dos servicos
from Controles.ControladorAbstrato import ControladorAbstrato
class ControladorMateria(ControladorAbstrato):
    def processar_acao(self, acao: str, dados: dict = None):
        self.rota.atualizar_estado(acao)
"""

"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""

from Controles.ControladorAbstrato import ControladorAbstrato
from Negocio.Materia import Materia
from Negocio.Prova import Prova
from Negocio.Trabalho import Trabalho
from Servicos.Servico import Servico

class ControladorMateria(ControladorAbstrato):
    def __init__(self, rota, servico: Servico, visualizador):
        super().__init__(rota, servico, visualizador)
        self.repositorio = servico.repositorio
        self.materia_selecionada_id = None # <--- MEMÓRIA
        self.id_user_logado = None
        self.id_semestre_ativo = None

    def definir_materia_ativa(self, id_materia):
        self.materia_selecionada_id = id_materia # <--- Onde guardamos a escolha

    
    def carregar_dados_para_tela(self, visualizador):
        """
        Busca os dados puros no Excel, transforma em Objetos reais e injeta no Visualizador.
        """
        # 1. Pega o ID da matéria direto da memória
        id_user = self.id_user_logado
        id_semestre = self.id_semestre_ativo
        id_materia = self.materia_selecionada_id

        if not id_user or not id_semestre or not id_materia:
            print(f"[Erro] Faltam dados na memória: User={id_user}, Semestre={id_semestre}, Materia={id_materia}")
            return

        # 2. Puxar a matéria do Excel
        todas_materias = self.repositorio.buscar_materias_por_semestre_usuario(id_user, id_semestre)
        dados_materia = next((m for m in todas_materias if m['id_materia'] == id_materia), None)

        if not dados_materia:
            print("[Erro] Matéria não encontrada no repositório.")
            return

        # 3. Puxar provas e trabalhos do Excel
        provas = self.repositorio.buscar_provas_por_materia_semestre_usuario(id_user, id_semestre, id_materia)
        trabalhos = self.repositorio.buscar_trabalhos_por_materia_semestre_usuario(id_user, id_semestre, id_materia)

        # 4. Empacotar em objetos reais
        materia_objeto = self._montar_objeto_materia(dados_materia, provas, trabalhos)

        # 5. Injetar a matéria real e o controlador no visualizador
        visualizador.materia = materia_objeto
        visualizador.controlador = self

    def _montar_objeto_materia(self, dados_materia: dict, provas: list, trabalhos: list):
        # 1. Instancia a SUA classe Materia
        materia = Materia()
        materia.id = dados_materia.get('id_materia')
        materia.nome = dados_materia.get('titulo', 'Sem Título')
        materia.professor = dados_materia.get('professor', 'Não informado')
        materia.horario = dados_materia.get('horario', 'Não informado')
        materia.atividades = []
        
        # 2. Instancia as SUAS classes de Prova
        for p in provas:
            prova = Prova()
            prova.id = p.get('id_prova')
            prova.titulo = p.get('titulo', 'Prova')
            prova.valor = float(p.get('valor_nota', 0.0))
            prova.nota_obtida = p.get('nota_obtida')
            
            # Lógica de exibição 
            prova.status = "Aguardando nota" if not prova.nota_obtida else f"Nota: {prova.nota_obtida}"
            materia.atividades.append(prova)

        # 3. Instancia as SUAS classes de Trabalho
        for t in trabalhos:
            trab = Trabalho()
            trab.id = t.get('id_trabalho')
            trab.titulo = t.get('titulo', 'Trabalho')
            trab.valor = float(t.get('valor_nota', 0.0))
            trab.nota_obtida = t.get('nota_obtida')
            
            trab.status = "Não entregue" if not trab.nota_obtida else f"Entregue ({trab.nota_obtida} pts)"
            materia.atividades.append(trab)

        return materia

    def processar_acao(self, acao: str, dados: dict = None):
        if acao in ["0", "1"]:
            self.rota.atualizar_estado(acao)
            
        elif acao.startswith("dar_nota_"):
            id_atividade_clicada = acao.replace("dar_nota_", "")
            print(f"[Controlador] O usuário quer abrir a atividade: {id_atividade_clicada}")
            
            if dados is None:
                dados = {}
            dados['id_atividade'] = id_atividade_clicada
            # self.rota.atualizar_estado("editar_atividade", dados)
        else:
            self.rota.atualizar_estado(acao)