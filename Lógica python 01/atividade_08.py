# -*- coding: utf-8 -*-
"""=atividade 08.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vF3qCJ3dnpvZ2IdfU4yRDs9eWAuN8vgV
"""

def par_ou_impar(num):
    if num % 2 == 0:
        print(f"O número {num} é par!!!")
        return "Par"
    else:
        return "Impar"

num = int(input("Digite um número:"))

result = par_ou_impar(num)
print("O seu número é : ", result)