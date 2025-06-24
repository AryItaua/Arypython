num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
divisao_inteira = num1 // num2
modulo = num1 % num2
exponenciacao = num1 ** num2

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Divisão Inteira: {divisao_inteira}")
print(f"Módulo: {modulo}")
print(f"Exponenciação: {exponenciacao}")

print("Erro: Por favor, insira apenas números inteiros.")
print("Erro: Divisão por zero não é permitida.")
