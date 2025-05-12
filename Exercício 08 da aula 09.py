#Escrever programa que leia um número e diga se é positivo, negativo ou zero usando if, else e elif
num = int(input("Digite um número: "))
if num > 0:
    print(f"O número {num} é positivo.")
elif num < 0:
    print(f"O número {num} é negativo")
else:
    print(f"O número é zero")