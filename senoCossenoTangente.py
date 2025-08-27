#faca um programa que leia o angulo qualquer e mostre na tela o seno o cosseno e a tangente desse angulo
import math

numero = float (input ("Digite o angulo: "))
numero = math.radians(numero)

print(f"\nSeu seno é: {math.sin(numero):.2f}")
print(f"\nSeu cosseno é: {math.cos(numero):.2f}")
print(f"\nSeu tangente é: {math.tan(numero):.2f}")

