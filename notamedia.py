nota1=float(input())
nota2=float(input())
media=(nota1+nota2)/2
if media >=7:
    print(f"Sua média final é {media}, e você foi aprovado!")
elif media >4:
    print(f"Sua média final é {media}, e você está de recuperação!")
else:
    print(f"Sua média final é {media}, e você foi reprovado!")
