#Faça um programa que use while para pedir senha 1234 ao usuário até estar correto e liberar acesso
senha = 1234
cont = 0
tentativa = int(input("Digite a senha: "))
while tentativa != senha:
    print("Não correspondente.")
    break
if tentativa == senha:
    print(f"Acesso liberado!")
