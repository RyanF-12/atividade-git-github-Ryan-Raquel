def calculadora():
    print("=== CALCULADORA BÁSICA ===")

    while True:
        try:
            num1 = float(input("\n Digite o primeiro número: "))
            operador = input("\n Digite a operação (+, -, *, /): ")
            num2 = float(input("\n Digite o segundo número: "))

            if operador == "+":
                resultado = num1 + num2

            elif operador == "-":
                resultado = num1 - num2

            elif operador == "*":
                resultado = num1 * num2

            elif operador == "/":
                if num2 == 0:
                    print("\n Erro: divisão por zero não é permitida.")
                    continue
                resultado = num1 / num2

            else:
                print("\n Operador inválido.")
                continue

            print(f"\n Resultado: {resultado}")

            continuar = input("\n Deseja fazer outra conta? (s/n): ").lower()

            if continuar != "s":
                print("\n Calculadora encerrada.")
                break

        except ValueError:
            print("\n Erro: digite apenas números válidos.")

calculadora()