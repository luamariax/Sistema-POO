import pandas as pd
import os

class Repositorio:
    def __init__(self, caminho_arquivo: str):
        self.caminho = caminho_arquivo
        self.data_frame = None
        self._carregar_dados()

    def _carregar_dados(self):
        if not os.path.exists(self.caminho):
            raise FileNotFoundError(f"Arquivo {self.caminho} não encontrado.")
        self.data_frame = pd.read_excel(self.caminho, dtype=str)  # tudo como string

    def buscar_usuario_por_email(self, email: str) -> dict | None:
        """Retorna um dicionário com os dados do usuário ou None se não encontrado."""
        data_frame_usuarios = pd.read_excel(self.caminho, sheet_name="Usuarios")
        resultado = data_frame_usuarios[data_frame_usuarios['email'] == email]
        if resultado.empty:
            return None
        return resultado.iloc[0].to_dict()
    
def Teste():
    repo = Repositorio("Arquivo.xlsx")
    dicionario = repo.buscar_usuario_por_email("ana.souza@ufmg.br")
    print(dicionario)

if __name__ == "__main__":
    Teste()