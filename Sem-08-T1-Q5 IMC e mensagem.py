#O índice de massa corporal (IMC) é uma medida internacional usada para calcular se uma pessoa está no peso ideal. O IMC é determinado pela divisão da massa do indivíduo pelo quadrado de sua altura, em que a massa está em quilogramas e a altura em metros. Escreva um programa que leia a massa (o peso) e a altura de uma pessoa e calcula o IMC de uma pessoa, e depois, mostra uma das seguintes mensagens:

def imc(massa, altura):
    imc = massa / (altura ** 2)
    return imc

massa=float(input())
altura=float(input())
imc = imc(massa, altura)

if imc < 18.5:
    print (f'{imc:.2f}')
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print (f'{imc:.2f}')
    print('Peso normal')
elif imc >= 25 and imc < 30:
    print (f'{imc:.2f}')
    print('Sobrepeso')
elif imc >= 30 and imc < 35:
    print (f'{imc:.2f}')
    print('Obeso leve')
elif imc >= 35 and imc < 40:
    print (f'{imc:.2f}')
    print('Obeso moderado')
elif imc >= 40:
    print (f'{imc:.2f}')
    print('Obeso mórbido')