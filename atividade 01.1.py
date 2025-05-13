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
        x = float(input("Primeiro número: "))
        y = float(input("Segundo número: "))
        return x, y
    except ValueError:
        print("Erro: por favor, insira números válidos.")
        return None, None


def calculadora():
    print("Operações: + - * /")
    op = input("Escolha uma operação: ")

    x, y = obter_entrada()
    if x is not None and y is not None:
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
