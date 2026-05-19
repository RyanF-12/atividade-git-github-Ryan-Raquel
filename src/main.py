def mostrar_menu():
    print("\n=== CALCULADORA BÁSICA ===")
    print("Operações disponíveis:")
    print("[+] Soma")
    print("[-] Subtração")
    print("[*] Multiplicação")
    print("[/] Divisão")


def calculadora():
    while True:
        mostrar_menu()

        try:
            num1 = float(input("\nDigite o primeiro número: "))
            operador = input("Digite a operação: ")
            num2 = float(input("Digite o segundo número: "))

            if operador == "+":
                resultado = num1 + num2

            elif operador == "-":
                resultado = num1 - num2

            elif operador == "*":
                resultado = num1 * num2

            elif operador == "/":
                if num2 == 0:
                    print("Erro: divisão por zero não é permitida.")
                    continue
                resultado = num1 / num2

            else:
                print("Operador inválido.")
                continue

            print(f"\nResultado: {num1} {operador} {num2} = {resultado}")

            continuar = input("\nDeseja fazer outra conta? (s/n): ").lower()

            if continuar != "s":
                print("\nCalculadora encerrada.")
                break

        except ValueError:
            print("Erro: digite apenas números válidos.")


calculadora()