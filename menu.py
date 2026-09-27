from calculadora import calc
from historico import hist

def menu_inicial():

    while True:

        print('''
            MENU INICIAL 
        ESCOLHA UMA OPÇÃO PARA CONTINUAR
        
        1 - CALCULADORA
        2 - HISTORICO DE CONTAS
        3 - FECHAR PROGRAMA
        ''')

        try:
            escolha = int(input('Escolha uma opção: '))
        except ValueError:
            print('Escolha um valor válido!')

        if escolha == 1:
            calc()

        elif escolha == 2:
            hist()

        elif escolha == 3:
            print('Fechando programa..')
            break

        else:
            print('Escolha uma opção valida!')
            continue

        
        