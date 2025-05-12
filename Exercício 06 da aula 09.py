#criar programa que peça 5 números e calcular a média aritmética (<7 aprovado, >4 reprovado
soma = 0
for x in range(1,6):
    num = float(input(f"Digite a {x}º nota:"))
    soma += num
media = soma/5
if media >= 7 and media <= 10:
    print(f"Aprovado! Sua média é {media}.")
if media <=6 and media >=4:
    print(f"Recuperação! Sua média é {media}.")
elif media < 4  and media > 0:
    print(f"Reprovado! Sua média é {media}.")
elif media >10 or media < 0:
    print("Número inválido")