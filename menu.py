
from calculadora import calc
from historico import hist


def menu_inicial():
    while True:
        print("""
╔════════════════════════════════════════════╗
║                                            ║
║             C A L C F O R G E              ║
║                  v1.0                      ║
║                                            ║
╠════════════════════════════════════════════╣
║               MENU PRINCIPAL               ║
╠════════════════════════════════════════════╣
║                                            ║
║    [1]  CALCULADORA                        ║
║    [2]  HISTÓRICO DE CONTAS                ║
║    [3]  FECHAR PROGRAMA                    ║
║                                            ║
╚════════════════════════════════════════════╝
        """)

        try:
            escolha = int(input("  ➜ Selecione uma opção: "))

        except ValueError:
            print("""
  ┌────────────────────────────────────────┐
  │ ERRO: Digite uma opção numérica válida.│
  └────────────────────────────────────────┘
            """)
            continue

        if escolha == 1:
            calc()

        elif escolha == 2:
            hist()

        elif escolha == 3:
            print("""
╔════════════════════════════════════════════╗
║                                            ║
║       ENCERRANDO O CALCFORGE...            ║
║                                            ║
║       Obrigado por utilizar!               ║
║                                            ║
╚════════════════════════════════════════════╝
            """)
            break

        else:
            print("""
  ┌────────────────────────────────────────┐
  │ ERRO: Selecione uma opção de 1 a 3.    │
  └────────────────────────────────────────┘
            """)


if __name__ == "__main__":
    menu_inicial()
