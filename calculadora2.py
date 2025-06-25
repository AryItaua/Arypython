num1=float(input(f"Digite um numero a ser calculado: "))
num2=float(input(f"Digite um numero a ser calculado: "))
calculo=input(f"Digite o simbolo referente ao calculo desejado (+,-,*,/)")
soma=num1+num2
subtracao=num1-num2
multiplicacao=num1*num2
divisao=num1/num2
if calculo == "+":
    print(f"Você escolheu soma: {num1}+{num2}={soma}")
elif calculo == "-":
    print(f"Você escolheu subtracao: {num1}-{num2}={subtracao}")
elif calculo == "*":
    print(f"Você escolheu multiplicacao: {num1}*{num2}={multiplicacao}")
elif calculo == "/":
    print(f"Você escolheu divisao: {num1}/{num2}={divisao}")
else:
    print(f"Nenhuma operação selecionada: ")
