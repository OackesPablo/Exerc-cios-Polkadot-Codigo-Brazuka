# -*- coding: utf-8 -*-
"""Atividade 14.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UXzzmNBKjAEA3K3MJfEoZHRdrApAZBAu
"""

print("_"*50)
print("Calculadora simples de 2 números")
print("_"*50)
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número:"))
soma = num1 + num2
sub = num1 - num2
div = num1 / num2
prod = num1 * num2
operacao = [soma, sub, div, prod]
operacao_escolhida = input("Digite o tipo de operação a ser feita com os dois números, + para soma,\n - para subtração, / para divisão, x para multiplicação : ")
if operacao_escolhida == "+":
  print(soma)
if operacao_escolhida == "-":
  print(sub)
if operacao_escolhida == "/":
  print(div)
if operacao_escolhida == "x":
  print(prod)
print("_"*50)