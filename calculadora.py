def somar():
    try:
        numero1 = int(input('Qual é o primeiro número? '))
        numero2 = int(input('Qual é o segundo número? '))
    except ValueError:
        print('Escolha um valor válido!')
        return
    
    resultado = numero1 + numero2
    print('O Resultado da soma é: ', resultado)

def sub():
    try:
        numero1 = int(input('Qual é o primeiro número? '))
        numero2 = int(input('Qual é o segundo número? '))
    except ValueError:
        print('Escolha um valor válido!')
        return

    resultado = numero1 - numero2
    print('O Resultado da subtração é: ', resultado)

def div():
    try:
        numero1 = int(input('Qual é o primeiro número? '))
        numero2 = int(input('Qual é o segundo número? '))
    except ValueError:
        print('Escolha um valor válido!')
        return
    
    try:
        resultado = numero1 / numero2
        print('O Resultado da divisão é: ', resultado)
    except ZeroDivisionError:
        print('Você não pode dividir um número por zero!')

def mult():
    try:
        numero1 = int(input('Qual é o primeiro número? '))
        numero2 = int(input('Qual é o segundo número? '))
    except ValueError:
        print('Escolha um valor válido!')
        return

    resultado = numero1 * numero2
    print('O Resultado da multiplicação é: ', resultado)

def pot():
    try:
        numero1 = int(input('Qual é o primeiro número? '))
        numero2 = int(input('Qual é o segundo número? '))
    except ValueError:
        print('Escolha um valor válido!')
        return

    resultado = numero1 ** numero2
    print('O Resultado da potência é: ', resultado)

def calc():
    while True:
        print('''
            BEM VINDO A CALCFORGE 1.0
        SELECIONE A OPÇÃO DE CONTA:
        
        1 - SOMA
        2 - SUBTRAÇÃO
        3 - DIVISÃO
        4 - MULTIPLICAÇÃO
        5 - POTÊNCIA
        6 - VOLTAR AO MENU INICIAL
        ''')

        try:
            escolha = int(input('Selecione uma opção: '))
        except ValueError:
            print('Selecione um valor válido!')
            continue

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