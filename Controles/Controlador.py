from .User import User  # Garante a importação do modelo da Isabela


class Controlador:
    def __init__(self, repositorio, visualizador, autenticador, interface):
        # Atributos protegidos do padrão MVC seguindo exatamente o UML do grupo
        self._acessoRepositorio = repositorio
        self._acessoVisualizador = visualizador
        self._acessoAutenticador = autenticador
        self._acessoInterface = interface
        self.usuario_logado = None

    def processar_acao(self, comando: str, dados: dict = None) -> None:
        """
        Este é o método maestro. Ele intercepta o clique da Luana (ex: 'login') 
        e decide o fluxo do sistema.
        """
        if comando == "login" and dados:
            email = dados.get("email", "")
            senha = dados.get("senha", "")

            # Chama o seu autenticador passando o repositório do Itamar
            sucesso = self._acessoAutenticador.login(
                email, senha, self._acessoRepositorio)

            if sucesso:
                # Recupera os dados do Excel para preencher o objeto User da Isabela [cite: 176, 202]
                dados_usuario = self._acessoRepositorio.buscar_usuario_por_email(
                    email)

                # Instancia a classe de negócio User da Isabela
                self.usuario_logado = User(
                    identificacao=str(dados_usuario.get('id', '1')),
                    endereco_eletronico=dados_usuario.get('email'),
                    nome_do_usuario=dados_usuario.get('nome')
                )

                # Avisa a interface que deu tudo certo e muda de página
                print(f"[Controlador] Logado como: {self.usuario_logado.nome}")
                self.navegar_para("pagina_home", "sucesso")
            else:
                # Se der erro, você aciona o método de erro que a Luana criou na tela!
                if hasattr(self._acessoVisualizador, 'mostrar_erro'):
                    self._acessoVisualizador.mostrar_erro(
                        "Email ou senha inválidos.")

    def navegar_para(self, exibicao_atual: str, comando: str) -> None:
        """Controla a transição de telas do app."""
        print(
            f"[Controlador] Navegando de: {exibicao_atual} -> Ação: {comando}")
        # Aqui ficará a lógica com a Luana para alternar as páginas em Flet [cite: 417]

    def criar_objeto(self, id_user, objeto) -> None:
        pass

    def editar_objeto(self, id_user, id_objeto, dados) -> None:
        pass

    def deletar_objeto(self, id_user, id_objeto) -> None:
        pass
