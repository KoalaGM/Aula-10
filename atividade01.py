import random


def calculadora():
    print("Operações: + - * /")
    op = input("Escolha uma operação: ")

    try:
        x = float(input("Primeiro número: "))
        y = float(input("Segundo número: "))
        

        if op == '+':
            print("Resultado:", x + y)
        elif op == '-':
            print("Resultado:", x - y)
        elif op == '*':
            print("Resultado:", x * y)
        elif op == '/':
            if y != 0:
                print("Resultado:", x / y)
            else:
                print("Erro: divisão por zero")

    except ValueError:
        print("Erro: por favor, insira números válidos.")


calculadora()
