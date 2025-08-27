#faca um programa que leia o cumprimento do cateto oposto e do adjacente de um triangulo 
# retangulo, calcule e mostre o comprimento da hipotenusa
import math

catetoOposto = float (input ("Digite o cateto oposto do triângulo retangulo: "))
catetoAdjacente = float (input ("Digite o cateto adjacente do triângulo retangulo: "))

print(f"\nA hipotenusa do triângulo é: {math.hypot(catetoOposto, catetoAdjacente)}")