#faca um sorteio da megasena

import random

chute1 = int(input("Digite o primeiro número de 0 a 60: "))
(0 <= chute1 <= 60) or exit("Número inválido")

chute2 = int(input("Digite o segundo número de 0 a 60: "))
(0 <= chute2 <= 60) or exit("Número inválido")

chute3 = int(input("Digite o terceiro número de 0 a 60: "))
(0 <= chute3 <= 60) or exit("Número inválido")

chute4 = int(input("Digite o quarto número de 0 a 60: "))
(0 <= chute4 <= 60) or exit("Número inválido")

chute5 = int(input("Digite o quinto número de 0 a 60: "))
(0 <= chute5 <= 60) or exit("Número inválido")

chute6 = int(input("Digite o sexto número de 0 a 60: "))
(0 <= chute6 <= 60) or exit("Número inválido")

jogada = [chute1, chute2, chute3, chute4, chute5, chute6]

certo1 = random.randrange(0, 60)
certo2 = random.randrange(0, 60)
certo3 = random.randrange(0, 60)
certo4 = random.randrange(0, 60)
certo5 = random.randrange(0, 60)
certo6 = random.randrange(0, 60)

resultado = [certo1, certo2, certo3, certo4, certo5, certo6]

print(f"\nSua jogada foi: {jogada}")

print(f"\nO resultado é: {resultado}")