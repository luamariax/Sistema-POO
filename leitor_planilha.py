import pandas
pd = pandas

def autenticar_usuarios(caminho_arquivo:str = "Arquivo.xlsx"):
    
    data_frame = pd.read_excel("Arquivo.xlsx", sheet_name="Usuarios")

    input_email = input("Digite seu e-mail: ").strip().lower()

    id_user_encontrado = data_frame[data_frame["email"].str.lower() == input_email]
    if id_user_encontrado.empty:
        print("E-mail não encontrado")
        return None

    input_senha = input("Digite sua senha: ")

    linha = id_user_encontrado[id_user_encontrado["senha"] == input_senha]
    if linha.empty:
        print("Senha incorreta.")
        return None
    
    id_user = linha.iloc[0]["id_user"]
    print(f"Login bem-sucedido! Bem-vind@ {linha.iloc[0]['nome']}!")
    return id_user

id_retornado = autenticar_usuarios("Usuarios.xlsx")
print(f"ID do usuário autenticado: {id_retornado}")
