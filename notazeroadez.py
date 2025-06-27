nota = ""
while nota < 0 > 10:
	nota = float(input("Digite uma nota de 0 a 10: "))
	print("Nota inválida, digite apenas uma nota de 0 a 10.")

print("Nota: %.1f" %nota)