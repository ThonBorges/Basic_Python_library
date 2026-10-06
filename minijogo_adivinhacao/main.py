import random

randomNumber = random.randint(1, 75)
contador_de_tentativas = 0

while True:
    userNumber = int(input('Tente adivinhar qual o numero, entre 1 a 10: '))
    if userNumber > randomNumber:
        print(f'Muito alto!')
        contador_de_tentativas += 1

    elif userNumber < randomNumber:
        print(f'Muito baixo!')
        contador_de_tentativas += 1

    else:
        print(f'Acertou! O numero sorteado foi {randomNumber}')
        break

print(f'A quantidade de tentativas foi de {contador_de_tentativas} palpites.')