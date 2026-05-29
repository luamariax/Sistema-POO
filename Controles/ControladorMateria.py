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

class ControladorMateria(ControladorAbstrato):
    def __init__(self, rota, repositorio):
        """
        O Controlador precisa conhecer a Rota (para mudar de tela) 
        e o Repositorio (para buscar os dados do Excel).
        """
        self.rota = rota
        self.repositorio = repositorio

    def carregar_dados_para_tela(self, id_user: str, id_semestre: str, id_materia: str, visualizador):
        """
        Busca os dados puros no Excel, transforma em Objetos (TADs) e injeta no Visualizador.
        Deve ser chamado pelo sistema ANTES de dar o .mostrar() na tela.
        """
        # 1. Puxar a matéria do Excel
        todas_materias = self.repositorio.buscar_materias_por_semestre_usuario(id_user, id_semestre)
        dados_materia = next((m for m in todas_materias if m['id_materia'] == id_materia), None)

        if not dados_materia:
            print("[Erro] Matéria não encontrada no repositório.")
            return

        # 2. Puxar provas e trabalhos do Excel
        provas = self.repositorio.buscar_provas_por_materia_semestre_usuario(id_user, id_semestre, id_materia)
        trabalhos = self.repositorio.buscar_trabalhos_por_materia_semestre_usuario(id_user, id_semestre, id_materia)

        # 3. Empacotar tudo no formato Orientado a Objetos
        materia_objeto = self._montar_objeto_materia(dados_materia, provas, trabalhos)

        # 4. Injetar a matéria real e o controlador no visualizador
        visualizador.materia = materia_objeto
        visualizador.controlador = self

    def _montar_objeto_materia(self, dados_materia: dict, provas: list, trabalhos: list):
        """
        Converte os dicionários do Pandas nas classes de domínio (TAD) do projeto.
        """
        # Classes temporárias (Mock) até você importar os arquivos TAD reais da sua equipe
        class TADMateria: pass
        class TADAtividade: pass

        materia = TADMateria()
        materia.id = dados_materia.get('id_materia')
        materia.nome = dados_materia.get('titulo', 'Sem Título')
        materia.professor = dados_materia.get('professor', 'Não informado')
        materia.horario = dados_materia.get('horario', 'Não informado')
        
        materia.atividades = []
        
        # Converte dicionários de Provas em objetos
        for p in provas:
            ativ = TADAtividade()
            ativ.id = p.get('id_prova')
            ativ.titulo = p.get('titulo', 'Prova')
            ativ.valor = float(p.get('valor_nota', 0.0))
            ativ.nota_obtida = p.get('nota_obtida', 'Aguardando')
            
            # Lógica para definir o status a aparecer na tela
            ativ.status = "Aguardando nota" if ativ.nota_obtida in [None, '', 'nan'] else f"Nota: {ativ.nota_obtida}"
            materia.atividades.append(ativ)

        # Converte dicionários de Trabalhos em objetos
        for t in trabalhos:
            ativ = TADAtividade()
            ativ.id = t.get('id_trabalho')
            ativ.titulo = t.get('titulo', 'Trabalho')
            ativ.valor = float(t.get('valor_nota', 0.0))
            ativ.nota_obtida = t.get('nota_obtida', 'Não entregue')
            
            ativ.status = "Não entregue" if ativ.nota_obtida in [None, '', 'nan'] else f"Entregue ({ativ.nota_obtida} pts)"
            materia.atividades.append(ativ)

        return materia

    def processar_acao(self, acao: str, dados: dict = None):
        """
        Intercepta os cliques do Visualizador e decide o que fazer.
        """
        # Se for um comando genérico de navegação (como "0" ou "1"), a Rota cuida disso!
        if acao in ["0", "1"]:
            self.rota.atualizar_estado(acao)
            
        # Se for um clique específico em um cartão de atividade (ex: "dar_nota_P001")
        elif acao.startswith("dar_nota_"):
            id_atividade_clicada = acao.replace("dar_nota_", "")
            
            print(f"[Controlador] O usuário quer abrir a atividade: {id_atividade_clicada}")
            
            # Aqui você pode colocar o ID no dicionário 'dados' e mandar a rota abrir a tela de edição
            if dados is None:
                dados = {}
            dados['id_atividade'] = id_atividade_clicada
            
            # Supondo que a sua Rota entenda um comando "editar_atividade"
            # self.rota.atualizar_estado("editar_atividade", dados)
        else:
            # Qualquer outra ação não prevista, delegamos para a Rota padrão
            self.rota.atualizar_estado(acao)