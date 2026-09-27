from menu import calc


def somar():
    try:
        numero1 = int(input('Qual é o primeiro número? '))
        numero2 = int(input('Qual é o segundo número? '))
    except ValueError:
        print('Escolha um valor válido!')
    
        resultado =  numero1 + numero2
        print('O Resultado da soma é: ', resultado)

def sub():
    try:
        numero1 = int(input('Qual é o primeiro número? '))
        numero2 = int(input('Qual é o segundo número? '))
    except ValueError:
        print('Escolha um valor válido!')

        resultado = numero1 - numero2
        print('O Resultado da subtração é: ', resultado)

def div():
    try:
        numero1 = int(input('Qual é o primeiro número? '))
        numero2 = int(input('Qual é o segundo número? '))
    except ValueError:
        print('Escolha um valor válido!')
    
    try:
        resultado = numero1 / numero2
    except ZeroDivisionError:
        print('Voce não pode dividar um número por zero!')
    
        print('O Resultado da divisão é: ', resultado)

def mult():
    try:
        numero1 = int(input('Qual é o primeiro número? '))
        numero2 = int(input('Qual é o segundo número? '))
    except ValueError:
        print('Escolha um valor válido!')

        resultado = numero1 * numero2
        print('O Resultado da multiplicação é: ', resultado)

def pot():
    try:
        numero1 = int(input('Qual é o primeiro número? '))
        numero2 = int(input('Qual é o segundo número? '))
    except ValueError:
        print('Escolha um valor válido!')

        resultado = numero1 ** numero2
        print('O Resultado da potencia é: ', resultado)

def calc():

    while True:

        print('''
            BEM VINDO A CALCFORGE 1.0
        SELECIONE A OPÇÃO DE CONTA:]
        
        1 - SOMA
        2 - SUBTRAÇÃO
        3 - DIVISÃO
        4 - MULTIPLICAÇÃO
        5 - POTENCIA

        6 - SE QUISER VOLTAR AO MENU INICIAL
        ''')

        try:
            escolha = int(input('Selecione uma opção: '))
        except ValueError:
            print('Selecione um valor válido!')


            if escolha == 1:
                somar()

            elif escolha == 2:
                sub()

            elif escolha == 3:
                div()

            elif escolha == 4:
                mult()

            elif escolha == 5:
                pot()

            elif escolha == 6:
                print('Voltando...')
                break
            
            else:
                print('Escolha uma opção válida!')
