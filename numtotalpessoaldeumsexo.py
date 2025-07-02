total_pessoas = int(input("Informe a quantidade total de pessoas no grupo: "))
masculino = 0
for indice in range(0,total_pessoas,1):
    sexo = input(f"Informe o sexo da pessoa {indice+1} (m/M para masculino, f/F para feminino): ")
    if sexo =="m" or sexo == "M":
        masculino +=1
print(f"Total de pessoas do sexo masculino; {masculino}")