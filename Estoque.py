import time
import os


ESTOQUE = {}
LOGIN = {}

def salvar1():
    try:
        with open('senha.csv', 'w') as arquivo:

            for login in LOGIN:
                senha = LOGIN[login]['senha']
                arquivo.write("{},{}\n".format(login, senha))

    except Exception as error:
        print('>>>> Algum erro ocorreu ao exportar')
        print(error)

def carregar1():
    try:
        with open('senha.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                login = detalhes[0]
                senha = detalhes[1]
                cadastrar_user(login, senha)
    except FileNotFoundError:
        print('>>>> Arquivo não encontrado')
    except Exception as error:
        print('>>>> Algum erro inesperado ocorreu')
        print(error)

def mostrar_user():
    if LOGIN:
        for login in LOGIN:
            nick(login)
    else:
        print('>>>> Usuario nao cadastrado')


def nick(login):
    try:
        print('Usuario:', login)
        print('--------------------------------------------')
    except KeyError:
        print('>>>> Usuario inexistente')
    except Exception as error:
        print('>>>> Um erro inesperado ocorreu')
        print(error)


def cadastrar_user(login, senha):
    LOGIN[login] = {
        'senha': senha,
    }
    salvar1()

def log():
    print("Logue no Sistema")
    print("----------------")
    print("1 - Cadastrar: ")
    print("2 - Logar: ")
    print("3 - Usuarios Cadastrados: ")
    print("4 - Sair: ")

def menu():
    print("__________________")
    print("SISTEMA DE ESTOQUE")
    print("1 - Mostar Estoque")
    print("2 - Buscar Item")
    print("3 - Inserir Item")
    print("4 - Remover Item")
    print("5 - Saida de Item do Estoque")
    print("6 - Adicionar Item ao Estoque")
    print("0 - Sair")

carregar1()

ip = ''

while ip < '5':
    log()
    id = input('Escolha: ')

    if id == '1':
        login = input('Cadastre um Usuario: ')

        if login == nick(login):
            senha = input('Cadastre uma Senha: ')
            cadastrar_user(login, senha)
            salvar1()
            os.system('pause')
            os.system('cls')

        else:
            print('Usuario ja Existente no SISTEMA.')
            os.system('pause')
            os.system('cls')


    elif id == '2':
            user = input('Inserira o login: ')
            pas = input('Inserira a senha: ')
            login = user
            if user == login and pas == LOGIN[login]['senha']:
                ip = '7'
                os.system('cls')

            else:
                print("Usuario ou senha invalido.")
                os.system('pause')
                os.system('cls')


    elif id == '3':
        print(mostrar_user())
        os.system('pause')
        os.system('cls')

    elif id == '4':
        exit()

    else:
        print("Opcao invalida")


def mostrar_estoque():
    if ESTOQUE:
        for estoque in ESTOQUE:
            buscar(estoque)
    else:
        print('>>>> ESTOQUE VAZIO')


def buscar(estoque):
    try:
        print('Nome:', estoque,' - ','Qnt:', ESTOQUE[estoque]['quantidade'])
        print('--------------------------------------------')
    except KeyError:
        print('>>>> Item inexistente')
    except Exception as error:
        print('>>>> Um erro inesperado ocorreu')
        print(error)


def inserir_item(estoque, quantidade):
    ESTOQUE[estoque] = {
        'quantidade': quantidade,
    }
    salvar()


def remover_item():
    try:
        ESTOQUE.pop(estoque)
        salvar()
        print()
        print('>>>> O item {} excluido com sucesso'.format(estoque))
        print()
    except KeyError:
        print('>>>> Item inexistente')
    except Exception as error:
        print('>>>> Um erro inesperado ocorreu')
        print(error)


def saida_item(estoque):
    try:
        ESTOQUE[estoque]['quantidade'] = int(ESTOQUE[estoque]['quantidade']) - quantidade1
    except KeyError:
        print('>>>> Item inexistente')
    except Exception as error:
        print('>>>> Um erro inesperado ocorreu')
        print(error)
        salvar()
        print()
        print('>>>> Estoque do {} atualizado com sucesso'.format(estoque))
        print()


def adicionar_item(estoque):
    try:
        ESTOQUE[estoque]['quantidade'] = int(ESTOQUE[estoque]['quantidade']) + quantidade1
    except KeyError:
        print('>>>> Item inexistente' )
    except Exception as error:
        print('>>>> Um erro inesperado ocorreu')
        print(error)
        salvar()
        print()
        print('>>>> Estoque do {} atualizado com sucesso'.format(estoque))
        print()


def salvar():
    try:
        with open('database.csv', 'w') as arquivo:
            for estoque in ESTOQUE:
                quantidade = ESTOQUE[estoque]['quantidade']
                arquivo.write("{},{}\n".format(estoque, quantidade))

    except Exception as error:
        print('>>>> Algum erro ocorreu ao exportar')
        print(error)


def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                estoque = detalhes[0]
                quantidade = detalhes[1]
                inserir_item(estoque, quantidade)
    except FileNotFoundError:
        print('>>>> Arquivo não encontrado')
    except Exception as error:
        print('>>>> Algum erro inesperado ocorreu')
        print(error)


carregar()


while True:
    menu()
    opcao = input('Escolha uma opção: ')


    if opcao == '1':
        mostrar_estoque()
        os.system('pause')
        os.system('cls')


    elif opcao == '2':
        estoque = input('Inserir o Item do Estoque: ')
        buscar(estoque)
        os.system('pause')
        os.system ('cls')


    elif opcao == '3':
        estoque = input('Inserir o Item no Estoque: ')
        quantidade = int(input('Inserir a quantidade no Estoque: '))
        inserir_item(estoque, quantidade)
        os.system('pause')
        os.system('cls')


    elif opcao =='4':
        estoque = input('Inserir o item a ser removido do Estoque: ')
        remover_item()
        os.system('pause')
        os.system('cls')


    elif opcao =='5':
        estoque = input('Inserir o item: ')
        quantidade1 = int(input('Informe a quantidade de {} a ser removido do Estoque: '.format(estoque)))
        saida_item(estoque)
        os.system('pause')
        os.system('cls')


    elif opcao =='6':
        estoque = input('Inserir o item: ')
        quantidade1 = int(input('Informe a quantidade de {} a ser adicionado ao Estoque: '.format(estoque)))
        adicionar_item(estoque)
        os.system('pause')
        os.system('cls')


    elif opcao == '0':
         break


    else:
        print("Opcao invalida")




