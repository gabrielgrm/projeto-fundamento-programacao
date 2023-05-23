import os
from time import sleep

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
def cadastrar():
    try:
        print("Registre-se\n")
        regLogin = input("Login: ").strip().upper()
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
def configurar(login, password):
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
    try:
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
    except (ValueError, KeyboardInterrupt):
        clear()
        print("Digite um número entre [1] e [5]\n")
        sleep(1)
        clear()
        main(login)
    except EOFError:
        clear()
        print("Fechando aplicativo...")
        sleep(1)
        clear()
        exit()
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