# -*- coding: utf-8 -*-
"""atividade 06.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_5SMZCqFKrL5l1If12i-_YeLm2aidD-V
"""

print("Contandor de vogais")
texto = input("Digite uma frase, uma palavra ou um texto :")
vogais = "aeiouAEIOU"
total_vogais = 0
for letra in texto:
    if letra in vogais:
        total_vogais += 1
print(f"Aparecem o total de {total_vogais} vogais ")