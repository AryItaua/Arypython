num_notas = int(input("Quantas notas você deseja inserir? "))
if num_notas <= 0:
      print("Por favor, insira um número positivo de notas.")
notas = []
for i in range(num_notas):
    while True:
        try:
          nota = float(input(f"Digite a nota {i+1}: "))
          if 0 <= nota <= 20:  #Considerando notas de 0 a 20
              notas.append(nota)
              break
          else:
              print("Nota inválida. Digite um valor entre 0 e 20.")
        except ValueError:
          print("Entrada inválida. Digite um número.")

    soma_notas = sum(notas)
    media = soma_notas / num_notas
    print(f"A média aritmética é: {media:.2f}")
    print("Entrada inválida. Digite um número inteiro para a quantidade de notas.")