# -*- coding: utf-8 -*-
"""atividade 10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p16292UF6sHMgQtKsjHVDN69BIB7IyKC
"""

def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
numero= int(input("Digite um número:"))
if eh_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo")