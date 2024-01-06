temp_cel = int(input("Qual é a temperatura da carne?"))

if temp_cel < 48:
    print("Cozinhar por mais tempo")

elif temp_cel in range(40, 53):
    print("Selada")

elif temp_cel in range(54, 59):
    print("Ao ponto para o mal")

elif temp_cel in range(60, 64):
    print("Ao ponto")

elif temp_cel in range(65, 70):
    print("Ao ponto para o bem")

else:
    print("Bem passada")

