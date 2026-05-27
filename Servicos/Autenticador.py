class Autenticador:
    def __init__(self):
        # Atributo privado encapsulado de acordo com os requisitos [cite: 45]
        self.__sessao_ativa = False

    def login(self, email: str, senha: str, repositorio) -> bool:
        """Busca o usuário no banco e valida o login."""
        # Busca os dados puros do usuário na planilha usando a função do Itamar
        dados_usuario = repositorio.buscar_usuario_por_email(email)

        if dados_usuario is None:
            print("[Autenticador] Email não cadastrado no sistema.")
            return False

        # IMPORTANTE: Como a Isabela escreveu no User.py que não precisa guardar a senha,
        # validamos comparando com o campo que está na planilha Excel (ajuste o nome se a coluna for diferente)
        senha_banco = dados_usuario.get('senha')

        if senha_banco == senha:
            self.__sessao_ativa = True
            print(f"[Autenticador] Login efetuado com sucesso para {email}!")
            return True

        print("[Autenticador] Senha incorreta.")
        return False

    def logout(self) -> None:
        """Encerra a sessão atual do usuário."""
        self.__sessao_ativa = False
        print("[Autenticador] Sessão finalizada.")

    def validar_senha(self, senha: str) -> bool:
        """Tratamento de erro simples: não aceita senhas vazias."""
        if not senha or not senha.strip():
            return False
        return len(senha) >= 4  # Exemplo: mínimo de 4 caracteres
