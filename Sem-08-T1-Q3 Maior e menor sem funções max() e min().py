#Escreva um programa que leia 5 números inteiros e escreva o maior e o menor deles. Considere que todos os valores são diferentes. NÃO use as funções min() e max().

a=input()
b=input()  
c=input()
d=input()
e=input()

T=[a,b,c,d,e]
mínima = T[0]
máxima = T[0]
for e in T:
    if e < mínima:
       mínima = e
    if e > máxima:
        máxima = e

print (int(máxima))
print (int(mínima))
