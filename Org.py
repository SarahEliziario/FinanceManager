movimentações = []

while True:
    print("\n=== CONTROLE FINANCEIRO ===")
    print("1 - Adicionar receita")
    print("2 - Adicionar despesas")
    print("3 - Ver extrato")
    print("4 - Ver saldo")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome da receita: ")

        try:
            valor = float(input("Valor da receita: "))
        except ValueError:
            print("Valor inválido")
            continue

        movimento = {
            "nome": nome,
            "valor": valor,
            "tipo": "receita"
        }

        movimentações.append(movimento)
        print("Receita cadastrada com sucesso!")

    elif opcao == "2":
        nome = input("Nome da despesa: ")

        try:
            valor = float(input("Valor da despesa: "))
        except ValueError:
            print("Valor inválido")
            continue

        movimento = {
            "nome": nome,
            "valor": valor,
            "tipo": "despesa"
        }

        movimentações.append(movimento)
        print("Despesa cadastrada com sucesso!")

    elif opcao == "3":
        if len(movimentações) == 0:
            print("Nenhum movimento encontrado")

        else:
            print("\n=== EXTRATO ===")

            for movimento in movimentações:
                print(
                    f"{movimento['tipo'].capitalize()} | "
                    f"{movimento['nome']} | "
                    f"R${movimento['valor']:.2f}"
                )

    elif opcao == "4":
        saldo = 0

        for movimento in movimentações:
            if movimento["tipo"] == "receita":
                saldo += movimento["valor"]
            else:
                saldo -= movimento["valor"]

        print(f"\nSaldo atual: R${saldo:.2f}")

    elif opcao == "5":
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida!")
