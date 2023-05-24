import os
from time import sleep
from twilio.rest import Client
account_sid = "AC9295cf4ab9293bb6760c0f0757ebadd0"
auth_token = "0ed0845d79bfca6b976fe437bd8ea72d"
verify_sid = "VA6842b4d5f396d9b3c5fd37b4c56be886"
def clear():
    os.system('cls')
def inicial():
    try:
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
    except (ValueError, KeyboardInterrupt):
        clear()
        print("Digite um número entre [1] e [3]\n")
        sleep(1)
        clear()
        inicial()
    except EOFError:
        clear()
        print("Fechando aplicativo...")
        sleep(1)
        clear()
        exit()
def logar():
    try:
        print("Faça o login\n")
        login = input("Login: ").upper()
        password = input("Senha: ")
        try:
            arquivo = open('dados.csv', 'r', encoding='utf-8')
        except FileNotFoundError:
            print("Arquivo não encontrado")
            sleep(1)
            clear()
            inicial()
        for linha in arquivo:
            if login in linha:
                linha = linha.strip()
                linha = linha.split(', ')
                if login == linha[0]:
                    if password == linha[1]:
                        sleep(1)
                        token(login)
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
    except KeyboardInterrupt:
        clear()
        print("Comando Inválido\n")
        sleep(1)
        clear()
        inicial()
    except EOFError:
        clear()
        print("Fechando aplicativo...")
        sleep(1)
        clear()
        exit()
def token(login):
    client = Client(account_sid, auth_token)
    arquivo = open('dados.csv', 'r', encoding='utf-8')
    for linha in arquivo:
        if login in linha:
            linha = linha.strip()
            linha = linha.split(', ')
            numero = linha[3]
    verification = client.verify.v2.services(verify_sid) \
    .verifications \
    .create(to=numero, channel='whatsapp')
    while True:
        otp_code = input(f"\033[30menviado para {numero}\033[0;0m\nInsira o TOKEN: ")
        try:
            verification_check = client.verify.v2.services(verify_sid) \
            .verification_checks \
            .create(to=numero, code=otp_code)
        except:
            print("\nToken incorreto")
            sleep(1)
            clear()
            continue
        if verification_check.status != 'approved':
            print("\nToken incorreto")
            sleep(1)
            clear()
        else:
            print("\nLogado com sucesso")
            sleep(1)
            clear()
            break
    arquivo.close()
    clear()
    main(login)
def cadastrar():
    try:
        print("Registre-se\n")
        regLogin = input("Nome: ").strip().upper()
        while True:
            numero = input("\033[30mex: +5581999999999\033[0;0m \nNúmero de telefone: ")
            if len(numero) == 14:
                if numero[0] == '+':
                    if numero[1:3] == '55':
                        if numero[6].isnumeric() and numero[7].isnumeric() and numero[8].isnumeric() and numero[9].isnumeric() and numero[10].isnumeric():
                            break
                        else:
                            print("\nNúmero inválido")
                    else:
                        print("\nNúmero inválido")
                else:
                    print("\nNúmero inválido")

            else:
                print("\nNúmero inválido")
        client = Client(account_sid, auth_token)

        verification = client.verify.v2.services(verify_sid) \
        .verifications \
            .create(to=numero, channel='whatsapp')

        while True:
            otp_code = input("Insira o TOKEN: ")
            try:
                verification_check = client.verify.v2.services(verify_sid) \
                .verification_checks \
                .create(to=numero, code=otp_code)
            except:
                print("\nToken incorreto")
                sleep(1)
                clear()
                continue
            if verification_check.status != 'approved':
                print("\nToken incorreto")
                sleep(1)
                clear()
            else:
                break
        try:
            arquivo = open('dados.csv', 'r', encoding='utf-8')
        except FileNotFoundError:
            print("Arquivo não encontrado")
            sleep(1)
            clear()
            inicial()
        for linha in arquivo:
            if regLogin in linha:
                print("\nUsuário já cadastrado")
                sleep(1)
                clear()
                cadastrar()
        arquivo.close()
        print("Número confirmado com sucesso!\n")
        regPassword = (input("Senha: ").strip())
        regPassword2 = (input("Confirmar senha: ").strip())
        if regPassword == regPassword2:
            print("\nUsuário cadastrado com sucesso!")
            sleep(1)
            clear()
            configurar(regLogin, regPassword, numero)
        if regPassword != regPassword2:
            print("\nSenhas não coincidem")
            sleep(1)
            clear()
            cadastrar()
    except KeyboardInterrupt:
        clear()
        print("Comando Inválido\n")
        sleep(1)
        clear()
        cadastrar()
    except EOFError:
        clear()
        print("Fechando aplicativo...")
        sleep(1)
        clear()
        exit()
def configurar(login, password, numero):
    try:
        print("Configurações do perfil\n")
        salario = float(input("Salário: "))
        confirmar = input(f"Pressione [ENTER] para confirmar o salário de R${salario}")
        if confirmar == '':
            print("\nSalário confirmado!")
            try:
                arquivo = open('dados.csv', 'a', encoding='utf-8')
            except FileNotFoundError:
                print("Arquivo não encontrado")
                sleep(1)
                clear()
                inicial()
            arquivo.write(f'{login}, {password}, {salario}, {numero}\n')
            arquivo.close()
            sleep(1)
            clear()
            main(login)
        else:
            print("\nSalário não confirmado")
            sleep(1)
            clear()
            configurar(login, password)
    except (ValueError, KeyboardInterrupt):
        clear()
        print("Digite um número válido\n")
        sleep(1)
        clear()
        configurar(login, password)
    except  EOFError:
        clear()
        print("Fechando aplicativo...")
        sleep(1)
        clear()
        exit()
def main(login):
    print("==== Sistema de Rastreamento de Despesas Pessoais =====\n")
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
    print(f"Olá, {login}!\t\t\t\tSaldo: R${salario}\n")
    menu = int(input("1. Registrar despesa\n2. Ver despesas\n3. Ver saldo\n4. Registrar ganho\n5. Excluir\n6. LogOut\n\n"))
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
        ganho(login)
    elif menu == 5:
        clear()
        excluir(login)
    elif menu == 6:
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
    try:
        print("==== Sistema de Rastreamento de Despesas Pessoais =====\n")
        print(f"Olá, {login}!\n")
        print("Registrar despesa\n")
        despesa = input("Digite sua despesa: ").title()
        valor = float(input(f"Qual valor da(o) {despesa}: "))
        categoria = input(f"Qual a categoria da(o) {despesa}: ").title()
        try:
            arquivo = open('gastos.csv', 'a', encoding='utf-8')
        except FileNotFoundError:
            print("Arquivo não encontrado")
            sleep(1)
            clear()
            inicial()
        arquivo.write(f'{login}, {despesa}, {valor}, {categoria}\n')
        arquivo.close()
        print("\nDespesa registrada com sucesso!")
        sleep(1)
        clear()
        main(login)
    except (ValueError, KeyboardInterrupt):
        clear()
        print("Digite um valor válido\n")
        sleep(1)
        clear()
        registrar(login)
    except EOFError:
        clear()
        print("Fechando aplicativo...")
        sleep(1)
        clear()
        exit()
def ver(login):
    try:
        print("==== Sistema de Rastreamento de Despesas Pessoais =====\n")
        print(f"Olá, {login}!\n")
        print("Ver despesas\n")
        categoria_filtro = input("Filtrar por categoria [ENTER para mostrar todas as despesas]: ").title()
        try:
            arquivo = open('gastos.csv', 'r', encoding='utf-8')
        except FileNotFoundError:
            print("Arquivo não encontrado")
            sleep(1)
            clear()
            inicial()
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
    except EOFError:
        clear()
        print("Fechando aplicativo...")
        sleep(1)
        clear()
        exit()
    except KeyboardInterrupt:
        clear()
        print("Comando Inválido\n")
        sleep(1)
        clear()
        ver(login)
def saldo(login):
    try:
        print("==== Sistema de Rastreamento de Despesas Pessoais =====\n")
        print(f"Olá, {login}!\n")
        print("Ver saldo\n")
        try:
            arquivo = open('dados.csv', 'r', encoding='utf-8')
        except FileNotFoundError:
            print("Arquivo não encontrado")
            sleep(1)
            clear()
            inicial()
        for linha in arquivo:
            linha = linha.strip()
            linha = linha.split(', ')
            if login == linha[0]:
                salario = float(linha[2])
        arquivo.close()
        try:
            arquivo = open('gastos.csv', 'r', encoding='utf-8')
        except FileNotFoundError:
            print("Arquivo não encontrado")
            sleep(1)
            clear()
            inicial()
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
    except KeyboardInterrupt:
        clear()
        print("Comando Inválido\n")
        sleep(1)
        clear()
        saldo(login)
    except EOFError:
        clear()
        print("Fechando aplicativo...")
        sleep(1)
        clear()
        exit()
def ganho(login):
    try:
        print("==== Sistema de Rastreamento de Despesas Pessoais =====\n")
        print(f"Olá, {login}!\n")
        print("Registrar ganho\n")
        try:
            arquivo = open('dados.csv', 'r', encoding='utf-8')
        except FileNotFoundError:
            print("Arquivo não encontrado")
            sleep(1)
            clear()
            inicial()
        for linha in arquivo:
            linha = linha.strip()
            linha = linha.split(', ')
            if login == linha[0]:
                salario = float(linha[2])
        arquivo.close()
        ganho = float(input("Digite o valor do ganho: "))
        salario += ganho
        try:
            arquivo = open('dados.csv', 'r', encoding='utf-8')
        except FileNotFoundError:
            print("Arquivo não encontrado")
            sleep(1)
            clear()
            inicial()
        dados = []
        for linha in arquivo:
            linha = linha.strip()
            linha = linha.split(', ')
            if login == linha[0]:
                linha[2] = str(salario)
            dados.append(linha)
        arquivo.close()
        try:
            arquivo = open('dados.csv', 'w', encoding='utf-8')
        except FileNotFoundError:
            print("Arquivo não encontrado")
            sleep(1)
            clear()
            inicial()
        for linha in dados:
            arquivo.write(f'{linha[0]}, {linha[1]}, {linha[2]}, {linha[3]}\n')
        arquivo.close()
        print("\nGanho registrado com sucesso!")
        sleep(1)
        clear()
        main(login)
    except (ValueError, KeyboardInterrupt):
        clear()
        print("Digite um valor válido\n")
        sleep(1)
        clear()
        ganho(login)
    except EOFError:
        clear()
        print("Fechando aplicativo...")
        sleep(1)
        clear()
        exit()
def excluir(login):
    try:
        print("==== Sistema de Rastreamento de Despesas Pessoais =====\n")
        print(f"Olá, {login}!\n")
        print("Excluir despesa\n")
        try:
            arquivo = open('gastos.csv', 'r', encoding='utf-8')
        except FileNotFoundError:
            print("Arquivo não encontrado")
            sleep(1)
            clear()
            inicial()
        for linha in arquivo:
            linha = linha.strip()
            linha = linha.split(', ')
            if login == linha[0]:
                print(f"{linha[1]}: R${linha[2]} - [{linha[3]}]")
        arquivo.close()
        print("\n")
        despesa = input("Digite a despesa que deseja excluir: ").title()
        try:
            arquivo = open('gastos.csv', 'r', encoding='utf-8')
        except FileNotFoundError:
            print("Arquivo não encontrado")
            sleep(1)
            clear()
            inicial()
        linhas = arquivo.readlines()
        arquivo.close()
        try:
            arquivo = open('gastos.csv', 'w', encoding='utf-8')
        except FileNotFoundError:
            print("Arquivo não encontrado")
            sleep(1)
            clear()
            inicial()
        for linha in linhas:
            if despesa not in linha:
                arquivo.write(linha)
        arquivo.close()
        print("\nDespesa excluída com sucesso!")
        sleep(1)
        clear()
        main(login)
    except KeyboardInterrupt:
        clear()
        print("Comando Inválido\n")
        sleep(1)
        clear()
        excluir(login)
    except EOFError:
        clear()
        print("Fechando aplicativo...")
        sleep(1)
        clear()
        exit()
clear()
inicial()