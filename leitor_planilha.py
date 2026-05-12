import pandas
pd = pandas

def autenticar_usuarios(caminho_arquivo:str):
    
    data_frame = pd.read_excel(caminho_arquivo, dtype=str)

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
    print(f"Login bem-sucedido! Bem-vind@")
    return id_user

id_retornado = autenticar_usuarios("Usuarios.xlsx")
print(f"ID do usuário autenticado: {id_retornado}")
