from datetime import datetime

def Teste():
    d_str = "2026-05-28"
    d_d = datetime.strptime(d_str.strip(), "%Y-%m-%d")
    print(type(d_d))

if __name__ == "__main__":
    Teste()