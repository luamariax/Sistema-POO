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

#id_retornado = autenticar_usuarios("Usuarios.xlsx")
#print(f"ID do usuário autenticado: {id_retornado}")


data_frame = pd.read_excel("Arquivo.xlsx", sheet_name="Materias", dtype=str)
usuario = "U001"
titularidade = "2026-1"
id_materia = "DCC001"
lista_de_semestre = data_frame[data_frame["id_user"] == usuario]
lista_de_materias = lista_de_semestre[lista_de_semestre["id_semestre"] == titularidade]
materia = lista_de_materias[lista_de_materias["id_materia"] == id_materia]
id_usuario = materia["id_user"][0] 
if materia.empty:
    print(f"Nenhuma materia encontrada para o usuário {id_usuario}.")
print(f"\nMateria do usuario {id_usuario}:")

for indice, linha in lista_de_materias.iterrows():
    numero_da_escolha = indice+1
    titulo_materia = linha["titulo"]
    print(f"{numero_da_escolha} -semestre de {titulo_materia}.")
numero_da_escolha_especifica = materia.index[0]+1
titulo_materia_especifica = materia["titulo"][0]
print(f"{numero_da_escolha_especifica} -semestre de {titulo_materia_especifica}.")