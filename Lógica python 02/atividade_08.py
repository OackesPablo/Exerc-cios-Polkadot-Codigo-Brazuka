# -*- coding: utf-8 -*-
"""atividade 08.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rKrmZKbK4FnNj9RxVcTJojeTjeQZU2_A
"""

print("Sequência de Fibonacci")
num = []
n = int(input("Digite a quantidade de termos: "))
t1 = 0
t2 = 1
for i in range(n):
    t3 = t1 + t2
    num.append(t3)
    t1 = t2
    t2 = t3
print(num)
print("FIM")