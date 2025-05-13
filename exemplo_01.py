import random
import os


os.system('cls')


#Exemplo 01
# n = random.randint(1, 10)


# print(f'O numero aleatório é {n}')


# lst_numeros = [random.randint(1, 10) for i in range(5)]
# print(f'A lista de números é {lst_numeros}')


#Exemplo 02 
def gerar_numeros(i, f, q):
    lst_num = [random.randint(i, f) for num in range(q)]
    return lst_num



ini = int(input('Informe o primeiro número: '))
fin = int(input('Informe o último número: '))
qtd = int(input('Quantos numeros?: '))

numeros = gerar_numeros(ini, fin, qtd)
print(numeros)