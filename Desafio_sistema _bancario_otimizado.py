import textwrap


def menu():
    menu = """\n
    ==========MENU==========
    O que deseja fazer hoje?

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova Conta
    [5] Listar Contas
    [6] Novo Usuario
    [0] Sair

    """
    return input(textwrap.dedent(menu))


def saque (*, saldo, valor_saque, extrato, limite, numero_saques, LIMITE_SAQUES):
    if numero_saques >= LIMITE_SAQUES:
        print("Você já atingiu o limite de saques por hoje.")

    elif valor_saque > saldo or saldo == 0:
        print(f"Não foi possível realizar o saque de R${valor_saque:.2f}, seu saldo atual é insuficiente.")
    elif valor_saque > limite:
        print(f"Limite por saque é de: R$ {limite:.2f}")
    else:
        saldo -= valor_saque
        numero_saques += 1
        extrato += f"Saque: R${valor_saque:.2f}\n"
        print(f"Saque de R$ {valor_saque:.2f}, realizado com sucesso!")
    return (saldo, extrato, numero_saques)


def extrato_resumo (saldo, / , *, extrato):
    print('\n==========EXTRATO==========')
    print('Não foram realizados movimentações.' if not extrato else extrato)
    print(f'\nSaldo atual de: R${saldo:.2f}')
    print('\n===========================')
    return saldo, extrato


def deposito (saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print("Depósito realizado com sucesso.")
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato


def criar_usuario (usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Usuário já cadastrado com esse CPF. ")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (Logradouro, nro - bairro - cidade/sigla estado): ")

    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    usuarios.append(novo_usuario)
    print("Usuário criado com sucesso!")
    return novo_usuario

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_cc (agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso")
        return {"conta": numero_conta, "agencia": agencia, "usuario": usuario}
    print("Usuario não encontrado, fluxo de criação de conta encerrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta["agencia"]}
            C/C:\t{conta["conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    agencia = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == '1':

            try:
                valor = int(input('Qual valor deseja depositar? R$ '))
                saldo, extrato = deposito(saldo, valor, extrato)
                print(f"Saldo: R${saldo}\nDepósito: R${valor}")
            except ValueError:
                print("Por favor, digite um número válido.", menu)

        elif opcao == '2':
            valor_saque = float(input("Quanto deseja sacar?"))
            saldo, extrato, numero_saques = saque(
                saldo=saldo,
                valor_saque=valor_saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES)


        elif opcao == '3':
           extrato_resumo(saldo, extrato=extrato)

        elif opcao == '4':
            numero_conta = len(contas) +1
            conta = criar_cc(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == '5':
            listar_contas(contas)

        elif opcao == '6':
           criar_usuario(usuarios)


        elif opcao == '0':
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()

