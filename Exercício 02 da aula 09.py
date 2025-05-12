#Criar número simulando jogo de adivinhação, utilizando while e dando dicas de proximidade (1 a 100)
numSecreto = 48
chute = 0
while chute != numSecreto:
    chute = int(input("Digite um número: "))
    if chute > numSecreto:
        print("Valor incorreto! O número  digitado é menor do que o número aleatório.")
    elif chute < numSecreto:
        print("Valor incorreto! O número digitado é maior que do número aleatório.")
    else:
        print("Parabéns! Você encontrou o número aleatório!")