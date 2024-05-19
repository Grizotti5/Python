menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor que deseja depositar: "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor: .2f}\n"
            print("Depoitado realizado com sucesso!")
        else:
            print("Valor inválido, tente novamente com um outro valor.")
    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar: "))
        if valor < saldo and LIMITE_SAQUES > numero_saques and valor < limite:
            numero_saques += 1
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            print("Saque realizado com sucesso!")
        elif valor < saldo and numero_saques > LIMITE_SAQUES:
            print("Limite diário de saques atingido")
        elif limite < valor:
            print("O valor é maior que o limite de saque, por favor solicite um valor menor!")
        else:
            print("Valor inválido, tente novamente!")
            
    elif opcao == "e":
        if extrato != '':
            print("**************Extrato**************")
            print(extrato)
            print(f"Saldo em conta: R$ {saldo}")
            print("**************Extrato**************")
        else:
            print("Nenhuma operação realizada")
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")