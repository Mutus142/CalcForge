
def exibir_resultado(operacao, resultado):
    print(f"""
╔════════════════════════════════════════════╗
║              RESULTADO DA OPERAÇÃO         ║
╠════════════════════════════════════════════╣

  OPERAÇÃO: {operacao}
  RESULTADO: {resultado}

╚════════════════════════════════════════════╝
    """)


def somar():
    print("\n══════════════ ADIÇÃO ══════════════")

    try:
        numero1 = int(input("  Primeiro número: "))
        numero2 = int(input("  Segundo número: "))

    except ValueError:
        print("\n  [ERRO] Digite apenas números válidos!\n")
        return

    resultado = numero1 + numero2
    exibir_resultado("ADIÇÃO", resultado)


def sub():
    print("\n════════════ SUBTRAÇÃO ═════════════")

    try:
        numero1 = int(input("  Primeiro número: "))
        numero2 = int(input("  Segundo número: "))

    except ValueError:
        print("\n  [ERRO] Digite apenas números válidos!\n")
        return

    resultado = numero1 - numero2
    exibir_resultado("SUBTRAÇÃO", resultado)


def div():
    print("\n══════════════ DIVISÃO ═════════════")

    try:
        numero1 = int(input("  Primeiro número: "))
        numero2 = int(input("  Segundo número: "))

    except ValueError:
        print("\n  [ERRO] Digite apenas números válidos!\n")
        return

    try:
        resultado = numero1 / numero2
        exibir_resultado("DIVISÃO", resultado)

    except ZeroDivisionError:
        print("""
  ┌────────────────────────────────────────┐
  │ ERRO: Não é possível dividir por zero! │
  └────────────────────────────────────────┘
        """)


def mult():
    print("\n═══════════ MULTIPLICAÇÃO ══════════")

    try:
        numero1 = int(input("  Primeiro número: "))
        numero2 = int(input("  Segundo número: "))

    except ValueError:
        print("\n  [ERRO] Digite apenas números válidos!\n")
        return

    resultado = numero1 * numero2
    exibir_resultado("MULTIPLICAÇÃO", resultado)


def pot():
    print("\n════════════ POTENCIAÇÃO ═══════════")

    try:
        numero1 = int(input("  Digite o número: "))

    except ValueError:
        print("\n  [ERRO] Digite apenas números válidos!\n")
        return

    resultado = numero1 * numero1
    exibir_resultado("POTÊNCIA AO QUADRADO", resultado)


def calc():
    while True:
        print("""
╔════════════════════════════════════════════╗
║                                            ║
║             C A L C F O R G E              ║
║                  v1.0                      ║
║                                            ║
╠════════════════════════════════════════════╣
║             MENU DA CALCULADORA            ║
╠════════════════════════════════════════════╣
║                                            ║
║    [1]  ADIÇÃO                             ║
║    [2]  SUBTRAÇÃO                          ║
║    [3]  DIVISÃO                            ║
║    [4]  MULTIPLICAÇÃO                      ║
║    [5]  POTENCIAÇÃO                        ║
║    [6]  VOLTAR AO MENU PRINCIPAL           ║
║                                            ║
╚════════════════════════════════════════════╝
        """)

        try:
            escolha = int(input("  ➜ Selecione uma operação: "))

        except ValueError:
            print("\n  [ERRO] Digite uma opção numérica válida!\n")
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
            print("\n  Retornando ao menu principal...\n")
            break

        else:
            print("\n  [ERRO] Selecione uma opção de 1 a 6!\n")
