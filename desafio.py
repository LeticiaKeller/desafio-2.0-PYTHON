import textwrap

def menu():
    menu = """/n
    ============MENU============
    [1] Depósito
    [2] saque
    [3] extrato
    [4] Novo usuário
    [5] Nova Conta
    [6] listar conta
    [7] Cancelar
    ============================
    """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
        if valor > 0:
            saldo += valor
            extrato += f"Depósito:\tR$ {valor: .2f}\n"
            print ("Depósito realizado com sucesso!")

def sacar(*, saldo, valor, extrato, limite, numero_saque, limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saque >= limite_saque
    saque = float(input("Quanto você gostaria de sacar? "))
    if excedeu_saldo:
        mensagem = str(input("Infelizmente você não tem esse valor disponivel!"))
    elif excedeu_saques:
        print ("Você atingiu o limite de saques diários, tente novamente amanhã!")
    elif excedeu_limite:
        print ("Operação falhou! O valor do saque excedeu o limite.")
    elif valor > 0:
        numero_saque +=1
        extrato = f"\nValor:\tR${valor: .2f}\n"
        saldo -= valor
        print ("Saque realizado com sucesso!")
    else:
         print ("O valor informado é inválido, tente novamente!")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
     print ("==============EXTRATO==============")
     print ("Não foram realizadas movimentações!") if not extrato else extrato
     print (f"Saldo:/tR$ {saldo: .2f}\n")
     print ("===================================")

def cria_usuario(usuarios):
    cpf = input("Informe o seu CPF (somente números):")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
         print("Esse CPF já está cadastrado em outra conta!")
         return
    
nome = input("Informe o seu nome: ")
data_nascimento = input ("informe sua data de nascimento: dd-mm-aa")
endereco = input("Informe o seu endereço: (rua, nro, bairro, cidade, estado)")

usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

print ("Usuário criado com sucesso!")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados= [usuario for usuario in usuarios if usuarios ["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = ("Informe o CPF do usuário:")
    usuario = filtrar_usuarios(cpf, usuarios)

    if cpf not in usuario:
        print("Não é possivel criar conta!")
    else:
        print("Conta criada com sucesso!")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario":usuario}
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t\t{conta ['agencia']}
            Conta Corrente:\t\t{conta ['numero_conta']}
            Titular:\t\t{conta ['usuarios']['nome']}
"""
        print ("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    conta = []

    while True:
        opcao = menu()

    if opcao == 1:
        valor = float(input("Insira o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)
    elif opcao == 2:
        valor = float(input("Qual o valor do saque? "))
        saldo, extrato = sacar(saldo, valor, extrato, limite, numero_saque, limite_saque)
    elif opcao == 3:
        exibir_extrato(saldo, extrato=extrato)
    elif opcao == 4:
        cria_usuario(usuarios)
    elif opcao == 5:
        numero_conta = len(contas) + 1
        criar_conta(agencia, numero_conta, usuarios)
        if conta:
            contas.append(conta)
    elif opcao == 6:
        listar_contas(contas)
    elif opcao == 7:
        exit()
    else:
        print("Opção inválida, tente novamente!")

main()