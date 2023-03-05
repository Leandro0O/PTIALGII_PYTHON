
# Escreva um programa que leia uma sequência N de números inteiros
# (negativos, positivos e o zero) para um vetor. No início do programa é solicitado ao
# usuário (pelo teclado) qual é a quantidade de elementos que serão lidos para o vetor
# e depois disso os números são lidos para o vetor.
# Em seguida você deve implementar para cada um dos itens abaixo uma função:
# a) Calcule e retorna o valor da maior diferença entre dois elementos distintos no
# vetor.
# b) Verifica se o vetor está em ordem crescente, e retorna true caso esteja e false
# caso contrário.


def cria_vetor():
    v = []
    n = int(input('Informe quantos valores deseja armazenar:\n'))
    for i in range(n):
        x = int(input(f'Informe o {i + 1}° valor:\n'))
        v.append(x)
    return v

def maior_dif(v):
    maior = max(v)
    menor = min(v)
    dif = maior - menor
    return print(f'A maior diferença é {dif}')

def ordem_crescente(v):
    for i in range(1, len(v)):
        if v[i] < v[i - 1]:
            return False
    return True

v = cria_vetor()
maior_dif(v)
print(ordem_crescente(v))