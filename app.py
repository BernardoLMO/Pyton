import os

restaurantes = [{'Nome':'Catatau', 'Categoria': 'Japonesa','Ativo':False}, {'Nome':'Ze Colmeia','Categoria':'Italiano','Ativo':True}]

def exibeNome():
    print('*******************************************')
    print('****************APP DE PEDIDOS*************')
    print('*******************************************')

def defineOpcoes():
    print('1. Cadastrar restaurante')
    print('2. Listrar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar():
    os.system('cls')
    print('Encerrando o programa')

def voltarAoMenu():
    input('Aperte uma tecla para retornar ao menu principal')
    main()

def cadastrar_Restaurante():
    print('Catastro de novos restaurantes')
    Restaurante = input("Nome do restaurante: ")
    categoria = input(f'Digite o nome da categoria do restaurante {Restaurante}: ')
    dadosDoRestaurante = {'nome': Restaurante, 'Categoria': categoria, 'Ativo': False}
    restaurantes.append(dadosDoRestaurante)
    print(f'O restaurante {Restaurante} foi cadastrado com sucesso')
    voltarAoMenu()

def opcap_invalida():
     print("Opcao invalida")
     voltarAoMenu()

def listarRestaurante():
    print('Listando os restaurantes')

    for Restaurante in restaurantes:
        nomeRestaurante = Restaurante['Nome']
        categoria = Restaurante['Categoria']
        ativo = 'ativado' if Restaurante['Ativo'] else 'desativado'
        print(f'-{nomeRestaurante} | {categoria} | {ativo}')
    voltarAoMenu()

def alterandoEstado():
    nomeRestaurante = input('Digite o nome do restaurante que desejaa alterar o estado: ')
    restauranteEncontrado = False

    for restaurante in restaurantes:
        if restaurante['Nome'] == nomeRestaurante:
            restauranteEncontrado = True
            restaurante['Ativo'] = not restaurante['Ativo']
            print('Estado alternado com sucesso')
    voltarAoMenu()

def finalizacao():
    print('**************************')

def escolherOpcao():
    try:
        opcao = int(input('Escolha uma opcao: '))
        if opcao == 1:
            cadastrar_Restaurante()
        elif opcao == 2:
            listarRestaurante()
        elif opcao == 3:
            alterandoEstado()
        elif opcao == 4:
            finalizar()
        else:
            opcap_invalida()
    except ValueError:
        opcap_invalida()

def main():
    os.system('cls')
    exibeNome()
    defineOpcoes()
    escolherOpcao()
    finalizacao()
    
if __name__ == '__main__':
    main()
