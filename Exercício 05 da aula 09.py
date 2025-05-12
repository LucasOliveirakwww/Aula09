#criar programa que peça 5 números e calcular a média aritmética
soma = 0
for x in range(1,6):
    num = float(input(f"Digite a {x}º nota:"))
    soma += num
media = soma/5
print(f"{media}")