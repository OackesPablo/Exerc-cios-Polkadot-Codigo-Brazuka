# -*- coding: utf-8 -*-
"""atividade 20.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oc0hy-A97yhG2mbjTWXA9yaqBX3wdDe_
"""

print("_"*50)
print("Calculando a média ponderada com os pesos 2, 3 e 5")
print("_"*50)

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1*2 + nota2*3 + nota3*5)/10
print(f"A média ponderada final é de {media} pontos ")