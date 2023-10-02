# Escreva um programa que leia 5 números inteiros, calcule e mostre a média e escreva os que são maiores que a média. Considere duas casas decimais.

def media(a,b,c,d,e):
    media_ = (a + b + c + d + e)/5
    return media_

a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
media_ = media(a,b,c,d,e)
x=media_
print(f'{x:.2f}')

if a>x:
    print(f'{a:.2f}')
if b>x:
    print(f'{b:.2f}')
if c>x:
    print(f'{c:.2f}')
if d>x:
    print(f'{d:.2f}')
if e>x:
    print(f'{e:.2f}')