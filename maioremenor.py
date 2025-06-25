num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num1 > num2:
    print(f"O maior número é: {num1} e o menor número é: {num2}")
elif num2 > num1:
    print(f"O maior número é: {num2} e o menor número é: {num1}")
else:
    print("Os números são iguais.")