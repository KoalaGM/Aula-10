import random


def somar(x, y):
    return x + y


def subtrair(x, y):
    return x - y


def multiplicar(x, y):
    return x * y


def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: divisão por zero"


def obter_entrada():
    try:
        # x = float(input("Primeiro número: "))
        # y = float(input("Segundo número: "))
        y = random.randint(1, 10)
        x = random.randint(1, 10)
        print(f"Os numeros da vez são {x} e {y}")
        return x, y
    except ValueError:
        print("Erro: por favor, insira números válidos.")
        return None, None


def calculadora():
    print("Operações: + - * /")
    op = input("Escolha uma operação: ")

    x, y = obter_entrada()
    if op == '+':
            print("Resultado:", somar(x, y))
    elif op == '-':
            print("Resultado:", subtrair(x, y))
    elif op == '*':
            print("Resultado:", multiplicar(x, y))
    elif op == '/':
            print("Resultado:", dividir(x, y))
    else:
            print("Operação inválida. Escolha entre +, -, * ou /.")


calculadora()
