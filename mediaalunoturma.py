total_alunos = 0
turma_atual = 1
alunos = 0
media = ""
quantidade_turma = int(input("Digite a quantidade de turmas: "))
while quantidade_turma <= 0:
    print("Valor inválido! Digite um número positivo e válido")
    quantidade_turma = int(input("Digite uma quantidade de turmas válidas: "))
while turma_atual <= quantidade_turma:
    print(f"Digite a quantidade de alunos na turma {turma_atual}")
    alunos_input = input("--->")
    if not alunos_input.isdigit():
        print("Digite apenas números inteiros")
    else:
        alunos = int(alunos_input)
        if alunos < 0:
            print("Não pode ser negativo")
        elif alunos > 40:
            print("Máximo d alunos permitidos por turma é 40")
        else:
            total_alunos += alunos
            turma_atual +=1
            if quantidade_turma > 0:
                media = total_alunos / quantidade_turma
                print(f"Média de alunos por turma: {media:.2f}")
            else:
                print("Nenhuma turma foi informada") 