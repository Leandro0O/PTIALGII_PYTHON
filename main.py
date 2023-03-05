
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