#o mesmo professor quer sortear a ordem de apresentacao do trabalho dos alunos. faca um programa que le o nome dos 4 alunos e mostre a ordem de cada um.

import random

aluno1 = str (input ("Digite o primeiro aluno: "))
aluno2 = str (input ("Digite o segundo aluno: "))
aluno3 = str (input ("Digite o terceiro aluno: "))
aluno4 = str (input ("Digite o quarto aluno: "))

alunos = [aluno1, aluno2, aluno3, aluno4]

ordem = random.sample(alunos, len(alunos))

print(f"\nA ordem escolhida é: {ordem}")
