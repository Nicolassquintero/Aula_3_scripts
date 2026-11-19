atual = 2
soma = 1
proximo = 0

while soma <= 40000:
    print(soma)

    proximo = soma + atual
    soma = proximo
    atual = atual + 1
