num = int(input("Digite um número de 0 a 10: "))
while True:
    if not(num >= 0 and num <= 10):
        num= int(input("Você digitou um número inválido, tente novamente"))
    else:
        break
    print(f"Você digitou o número {num} - Fim de Programa")