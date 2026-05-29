from datetime import datetime
import pandas as pd

def Teste():
    

    # Criando um DataFrame de exemplo
    df = pd.DataFrame({
        'Nome': ['Ana', 'Bruno', 'Carlos'],
        'Idade': [23, 34, 45]
    }, index=[10, 20, 30])

    # Nova linha recém-criada (pode ser uma lista, dicionário ou Series)
    nova_linha = ['Beatriz', 28]

    # Substituindo a linha de index 20 (onde estava o Bruno)
    df.loc[20] = nova_linha

    print(df)

if __name__ == "__main__":
    Teste()