#Pedir digitação de um número inteiro e usar para mostrar tabuada de 1 a 10
num = int(input("Digite um número: "))
for i in range (1,11):
    resultado = num * i
    print(f"{num}X{i}={resultado}")