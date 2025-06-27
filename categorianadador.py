idade = int(input("Digite a idade do nadador: "))
if idade < 5:
    print("Não há categoria para esta idade.")
elif 5 <= idade <= 7:
    print("Categoria: Infantil 1")
elif 8 <= idade <= 11:
    print("Categoria: Infantil 2")
elif 12 <= idade <= 13:
    print("Categoria: Juvenil 1")
elif 14 <= idade <= 17:
    print("Categoria: Juvenil 2")
else:
    print("Categoria: Adulto")