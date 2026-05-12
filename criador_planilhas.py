from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Usuarios"

# Cabeçalhos
ws.append(["id_user", "email", "senha", "nome"])

# Dados
users = [
    ("001", "teste@ufmg.br", "123", "Teste"),
    ("002",   "adm@ufmg.br", "123", "Administrador"),
    ("007", "abin@ufmg.br", "007", "Tiago Bond"),
    ("101", "auau@ufmg.br", "101", "Dalmatas"),
]

for linha, (id_user, email, senha, nome) in enumerate(users, start=2):
    ws.append([id_user, email, senha, nome])  

wb.save("Usuarios.xlsx")
print("Arquivo criado!")