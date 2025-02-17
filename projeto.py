import csv

def criar_arquivo():
    try:
        with open("financas.csv", "x", newline="") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["Tipo", "Descrição", "Valor"])
    except FileExistsError:
        pass

def adicionar_transacao(tipo, descricao, valor):
    with open("financas.csv", "a", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([tipo, descricao, valor])
    print("Transação adicionada com sucesso!")

def listar_transacoes():
    try:
        with open("financas.csv", "r") as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)  # Pular cabeçalho
            for linha in leitor:
                print(f"{linha[0]} - {linha[1]}: R$ {linha[2]}")
    except FileNotFoundError:
        print("Nenhuma transação encontrada.")

def calcular_saldo():
    saldo = 0.0
    try:
        with open("financas.csv", "r") as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)  # Pular cabeçalho
            for linha in leitor:
                valor = float(linha[2])
                if linha[0] == "Receita":
                    saldo += valor
                else:
                    saldo -= valor
        print(f"Saldo atual: R$ {saldo:.2f}")
    except FileNotFoundError:
        print("Nenhuma transação encontrada.")

if __name__ == "__main__":
    criar_arquivo()
    while True:
        print("\n1. Adicionar Receita")
        print("2. Adicionar Despesa")
        print("3. Listar Transações")
        print("4. Exibir Saldo")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Descrição: ")
            valor = input("Valor: ")
            adicionar_transacao("Receita", descricao, valor)
        elif opcao == "2":
            descricao = input("Descrição: ")
            valor = input("Valor: ")
            adicionar_transacao("Despesa", descricao, valor)
        elif opcao == "3":
            listar_transacoes()
        elif opcao == "4":
            calcular_saldo()
        elif opcao == "5":
            break
        else:
            print("Opção inválida! Tente novamente.")
