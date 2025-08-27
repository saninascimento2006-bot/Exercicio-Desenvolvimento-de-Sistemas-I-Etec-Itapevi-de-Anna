#um professor quer sortear um dos seus quatro alunos para apagar o quadro. faca um programa que o ajude a fazer esse sorteio

import random

aluno1 = str (input ("Digite o primeiro aluno: "))
aluno2 = str (input ("Digite o segundo aluno: "))
aluno3 = str (input ("Digite o terceiro aluno: "))
aluno4 = str (input ("Digite o quarto aluno: "))

alunos = [aluno1, aluno2, aluno3, aluno4]

print(f"\nO aluno escolhido para apagar a lousa é o: {random.choice(alunos)}")


