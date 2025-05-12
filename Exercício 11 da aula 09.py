#Criar programa que leia 10 números e conte quantos são maiores que 50 usando for e if
quanti = 0
for i in range (10):
    num = int(input("Digite um número: "))
    if num > 50:
        quanti +=1
print(quanti)