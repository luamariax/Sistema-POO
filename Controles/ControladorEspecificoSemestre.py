

"""
padrões de escrita
classe usa PascalCase
função e variaveis usa snake_case
"""
from .ControladorAbstrato import ControladorAbstrato
from Modelos.Servico import Servico

class ControladorEspecificoSemestre(ControladorAbstrato):
    def __init__(self, rota, servico: Servico, visualizador):
        super().__init__(rota, servico, visualizador)

    def carregar_dados_para_tela(self):
        # Busca o semestre pelo ID
        semestre = self.servico._objetos_do_usuario
        if not semestre:
            return

        lista_materias_dict = self.servico.repositorio.buscar_materias_por_semestre_usuario(
            self.servico._id_user_logado, 
            semestre.id
        )
        
        self.visualizador.titulo_semestre = semestre.titulo
        self.visualizador.lista_materias = lista_materias_dict

    def processar_acao(self, acao: str, dados: dict = None):
        if acao == "0":
            # Botão Voltar: Limpa o foco e volta
            self.servico.retirar_objeto('Semestre')
            self.rota.atualizar_estado("0")
        
        elif "-" in acao:
            # Comando "1-0" para abrir a matéria na posição 0
            partes = acao.split("-")
            posicao = int(partes[1])
            self.servico.instanciar_objeto('Materia', posicao)
            self.rota.atualizar_estado("1") # Vai para a página da Matéria
            
        elif acao == "salvar_novo":
            if dados:
                dados['id_user'] = self.servico.id_user_logado
                dados['id_semestre'] = self.servico._id_semestre_logado
                # Usa o método de criar_dependente do Semestre (Objeto)
                self.servico._objetos_do_usuario.criar_dependente(dados, self.servico.repositorio)
                self.carregar_dados_para_tela()
                if self.rota.page:
                    self.visualizador.mostrar(self.rota.page)