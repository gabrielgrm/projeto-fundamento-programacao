import os; from time import sleep
usuario = {'ADMIN': 'admin'}
salarios = {}
alugueis = {}
luzes = {}
aguas = {}
gases = {}
internets = {}
telefones = {}
outros1 = {}
despesas = {}
valores = {}
qntd = {'ADMIN': 0}
def clear():
    os.system('cls')
def inicial():
    print("==== Sistema de Rastreamento de Despesas Pessoais =====\n")
    inicio = int(input("1. Login\n2. Cadastrar\n3. Sair\n\n"))
    clear()
    if inicio == 1:
        logar()
    elif inicio == 2:
        cadastrar()
    elif inicio == 3:
        exit()
    else:
        print("Opção inválida\n")
        inicial()
def logar():
    print("Faça o login\n")
    login = input("Login: ").upper()
    password = input("Senha: ")
    if login in usuario:
        if password == usuario[login]:
            print("Logado com sucesso!")
            sleep(1)
            qntd[login] += 1
            clear()
            if qntd[login] == 1:
                salario(login)
            else:
                main(login)
        else:
            print("\nSenha incorreta")
            sleep(1)
            clear()
            logar()
    else:
        print("\nUsuário não encontrado")
        sleep(1)
        clear()
        inicial()
def cadastrar():
    print("Registre-se\n")
    regLogin = input("Login: ").strip().upper()
    regPassword = input("Senha: ").strip()
    regPassword2 = input("Confirmar senha: ").strip()
    if regPassword == regPassword2:
        usuario[regLogin] = regPassword
        print("\nUsuário cadastrado com sucesso!")
        qntd[regLogin] = 0
        sleep(1)
        clear()
        
        inicial()
    if regPassword != regPassword2:
        print("\nSenhas não coincidem")
        sleep(1)
        clear()
        cadastrar()
def salario(login):
    print("==== Configurando perfil ====\n")
    salario = float(input("Salário: "))
    salarios[login] = salario
    despesas = int(input("\nVocê possui alguma despesa fixa?\n\n1. Sim\n2. Não\n\n"))
    if despesas == 1:
        clear()
        despesaFixa(login)
    elif despesas == 2:
        clear()
        main(login)
def despesaFixa(login):
    while True:
        print("==== Despesa fixa ====")
        despesa = int(input("\n1. Aluguel\n2. Luz\n3. Água\n4. Gás\n5. Internet\n6. Telefone\n7. Outros\n8. Finalizar\n\n"))
        if despesa == 1:
            aluguel = float(input("\nValor do aluguel: "))
            alugueis[login] = aluguel
            clear()
        elif despesa == 2:
            luz = float(input("\nValor da luz: "))
            luzes[login] = luz
            clear()
        elif despesa == 3:
            agua = float(input("\nValor da água: "))
            aguas[login] = agua
            clear()
        elif despesa == 4:
            gas = float(input("\nValor do gás: "))
            gases[login] = gas
            clear()
        elif despesa == 5:
            internet = float(input("\nValor da internet: "))
            internets[login] = internet
            clear()
        elif despesa == 6:
            telefone = float(input("\nValor do telefone: "))
            telefones[login] = telefone
            clear()
        elif despesa == 7:
            outros = float(input("\nOutros: "))
            outros1[login] = outros
            clear()
        elif despesa == 8:
            clear()
            main(login)
            break
        else:
            print("\nOpção inválida")
            sleep(1)
            clear()
            despesaFixa(login)
def main(login):
    print("==== Menu ====\n")
    menu = int(input("1. Adicionar despesa\n2. Ver extrato\n3. Excluir despesa\n4. Sair\t\t\t\tSaldo:\n\n"))
    if menu == 1:
        clear()
        adicionar(login)
    elif menu == 2:
        clear()
        ver(login)
    elif menu == 3:
        clear()
        excluir(login)
    elif menu == 4:
        clear()
        inicial()
    else:
        print("Opção inválida\n")
        main(login)
    saldo = salarios[login]
    if login in alugueis:
        saldo -= alugueis[login]
    if login in luzes:
        saldo -= luzes[login]
    if login in aguas:
        saldo -= aguas[login]
    if login in gases:
        saldo -= gases[login]
    if login in internets:
        saldo -= internets[login]
    if login in telefones:
        saldo -= telefones[login]
    if login in outros1:
        saldo -= outros1[login]
    print(f"Saldo: {saldo}\n")
def adicionar(login):
    print("==== Adicionar despesa ====\n")
    nova = int(input("1. Adicionar uma nova despesa\n2. Atualizar despesas fixas\n3. Voltar\n\n"))
    if nova == 1:
        despesa1 = (input("Qual foi sua despesa? ")).title()
        despesa2 = float(input(f"\nQual foi o valor do(a) {despesa1.lower()}? "))
        despesas[login] = despesa1
        valores[login] = despesa2   
        clear()
        print(f"{despesa1} de R${despesa2:.2f} adicionada com sucesso!\n")
        sleep(2)
        clear()
        main(login)
    elif nova == 2:
        despesa = int(input("1. Aluguel\n2. Luz\n3. Água\n4. Gás\n5. Internet\n6. Telefone\n7. Outros\n8. Voltar\n\n"))
        if despesa == 1:
            aluguel = float(input("\nValor do aluguel: "))
            alugueis[login] = aluguel
            clear()
        elif despesa == 2:
            luz = float(input("\nValor da luz: "))
            luzes[login] = luz
            clear()
        elif despesa == 3:
            agua = float(input("\nValor da água: "))
            aguas[login] = agua
            clear()
        elif despesa == 4:
            gas = float(input("\nValor do gás: "))
            gases[login] = gas
            clear()
        elif despesa == 5:
            internet = float(input("\nValor da internet: "))
            internets[login] = internet
            clear()
        elif despesa == 6:
            telefone = float(input("\nValor do telefone: "))
            telefones[login] = telefone
            clear()
        elif despesa == 7:
            outros = float(input("\nOutros: "))
            outros1[login] = outros
            clear()
        elif despesa == 8:
            clear()
            main(login)
        else:
            print("\nOpção inválida")
            sleep(1)
            clear()
            adicionar(login)
    elif nova == 3:
        clear()
        main(login)
    else:
        print("\nOpção inválida")
        sleep(1)
        clear()
        adicionar(login)
def ver(login):
    print("==== Ver despesas por categoria ====\n")
    if login in despesas:
        print(f"{despesas[login]}: R${valores[login]:.2f}")
    else:
        print("Nenhuma despesa adicionada")
    if login in alugueis:
        print(f"Aluguel: R${alugueis[login]:.2f}")
    if login in luzes:
        print(f"Luz: R${luzes[login]:.2f}")
    if login in aguas:
        print(f"Água: R${aguas[login]:.2f}")
    if login in gases:
        print(f"Gás: R${gases[login]:.2f}")
    if login in internets:
        print(f"Internet: R${internets[login]:.2f}")
    if login in telefones:
        print(f"Telefone: R${telefones[login]:.2f}")
    if login in outros1:
        print(f"Outros: R${outros1[login]:.2f}")
    sleep(5)
    clear()
    main(login)
def excluir(login):
    print("==== Excluir despesa ====\n")
    if login in despesas:
        print(f"{despesas[login]}: R${valores[login]:.2f}\n")
        excluir = int(input("1. Excluir despesa\n2. Voltar\n\n"))
        if excluir == 1:
            del despesas[login]
            del valores[login]
            clear()
            print("Despesa excluída com sucesso!\n")
            sleep(2)
            clear()
            main(login)
        elif excluir == 2:
            clear()
            main(login)
        else:
            print("Opção inválida\n")
            sleep(1)
            clear()
            excluir(login)
    else:
        print("Nenhuma despesa adicionada\n")
        sleep(2)
        clear()
        main(login)
clear()
inicial()