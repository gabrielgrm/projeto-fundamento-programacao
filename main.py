import os
from time import sleep

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
        print("Saindo...")
        sleep(1)
        clear()
        exit()
    else:
        clear()
        print("Digite um número entre [1] e [3]\n")
        sleep(1)
        clear()
        inicial()

def logar():
    print("Faça o login\n")
    login = input("Login: ").upper()
    password = input("Senha: ")
    arquivo = open('dados.csv', 'r', encoding='utf-8')
    for linha in arquivo:
        if login in linha:
            linha = linha.strip()
            linha = linha.split(', ')
            if login == linha[0]:
                if password == linha[1]:
                    print("Logado com sucesso!")
                    sleep(1)
                    clear()
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
    
    print("\nUsuário não encontrado")
    sleep(1)
    clear()
    inicial()
    arquivo.close()

def cadastrar():
    print("Registre-se\n")
    regLogin = input("Login: ").strip().upper()
    arquivo = open('dados.csv', 'r', encoding='utf-8')
    for linha in arquivo:
        if regLogin in linha:
            print("\nUsuário já cadastrado")
            sleep(1)
            clear()
            cadastrar()
    arquivo.close()
    regPassword = (input("Senha: ").strip())
    regPassword2 = (input("Confirmar senha: ").strip())
    if regPassword == regPassword2:
        print("\nUsuário cadastrado com sucesso!")
        sleep(1)
        clear()
        configurar(regLogin, regPassword)
    if regPassword != regPassword2:
        print("\nSenhas não coincidem")
        sleep(1)
        clear()
        cadastrar()

def configurar(login, password):
    print("Configurações do perfil\n")
    salario = float(input("Salário: "))
    confirmar = input(f"Pressione [ENTER] para confirmar o salário de R${salario}")
    if confirmar == '':
        print("\nSalário confirmado!")
        arquivo = open('dados.csv', 'a', encoding='utf-8')
        arquivo.write(f'{login}, {password}, {salario}\n')
        arquivo.close()
        sleep(1)
        clear()
        main(login)
    else:
        print("\nSalário não confirmado")
        sleep(1)
        clear()
        configurar(login, password)

def main(login):
    print("==== Sistema de Rastreamento de Despesas Pessoais =====\n")
    print(f"Olá, {login}!\n")
    menu = int(input("1. Registrar despesa\n2. Ver despesas\n3. Ver saldo\n4. Excluir\n5. LogOut\n\n"))
    if menu == 1:
        clear()
        registrar(login)
    elif menu == 2:
        clear()
        ver(login)
    elif menu == 3:
        clear()
        saldo(login)
    elif menu == 4:
        clear()
        excluir(login)
    elif menu == 5:
        print("Saindo...")
        sleep(1)
        clear()
        inicial()
    else:
        print("Digite um número entre [1] e [5]\n")
        sleep(1)
        clear()
        main(login)

def registrar(login):
    print("==== Sistema de Rastreamento de Despesas Pessoais =====\n")
    print(f"Olá, {login}!\n")
    print("Registrar despesa\n")
    despesa = input("Digite sua despesa: ").title()
    valor = float(input(f"Qual valor da(o) {despesa}: "))
    categoria = input(f"Qual a categoria da(o) {despesa}: ").title()
    arquivo = open('gastos.csv', 'a', encoding='utf-8')
    arquivo.write(f'{login}, {despesa}, {valor}, {categoria}\n')
    arquivo.close()
    print("\nDespesa registrada com sucesso!")
    sleep(1)
    clear()
    main(login)

def ver(login):
    print("==== Sistema de Rastreamento de Despesas Pessoais =====\n")
    print(f"Olá, {login}!\n")
    print("Ver despesas\n")
    categoria_filtro = input("Filtrar por categoria [ENTER para mostrar todas as despesas]: ").title()
    arquivo = open('gastos.csv', 'r', encoding='utf-8')
    for linha in arquivo:
        linha = linha.strip()
        linha = linha.split(', ')
        if login == linha[0]:
            if categoria_filtro == "" or categoria_filtro == linha[3]:
                print(f"{linha[1]}: R${linha[2]} - [{linha[3]}]")
    arquivo.close()
    print("\n")
    voltar = input("Pressione [ENTER] para voltar ao menu principal")
    clear()
    main(login)

def saldo(login):
    print("==== Sistema de Rastreamento de Despesas Pessoais =====\n")
    print(f"Olá, {login}!\n")
    print("Ver saldo\n")
    arquivo = open('dados.csv', 'r', encoding='utf-8')
    for linha in arquivo:
        linha = linha.strip()
        linha = linha.split(', ')
        if login == linha[0]:
            salario = float(linha[2])
    arquivo.close()
    arquivo = open('gastos.csv', 'r', encoding='utf-8')
    for linha in arquivo:
        linha = linha.strip()
        linha = linha.split(', ')
        if login == linha[0]:
            salario -= float(linha[2])
    arquivo.close()
    print(f"Saldo: R${salario}")
    print("\n")
    voltar = input("Pressione [ENTER] para voltar ao menu principal")
    clear()
    main(login)

def excluir(login):
    print("==== Sistema de Rastreamento de Despesas Pessoais =====\n")
    print(f"Olá, {login}!\n")
    print("Excluir despesa\n")
    arquivo = open('gastos.csv', 'r', encoding='utf-8')
    for linha in arquivo:
        linha = linha.strip()
        linha = linha.split(', ')
        if login == linha[0]:
            print(f"{linha[1]}: R${linha[2]} - [{linha[3]}]")
    arquivo.close()
    print("\n")
    despesa = input("Digite a despesa que deseja excluir: ").title()
    arquivo = open('gastos.csv', 'r', encoding='utf-8')
    linhas = arquivo.readlines()
    arquivo.close()
    arquivo = open('gastos.csv', 'w', encoding='utf-8')
    for linha in linhas:
        if despesa not in linha:
            arquivo.write(linha)
    arquivo.close()
    print("\nDespesa excluída com sucesso!")
    sleep(1)
    clear()
    main(login)

clear()
inicial()
