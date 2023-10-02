#Escreva um programa que leia, separadamente, dia, mês e ano da data atual. Leia, da mesma forma, a data de nascimento de uma pessoa, calcule e escreva a idade exata em anos

dia_at = int(input())
mes_at =int(input())
ano_at = int(input())

data_atual=((dia_at)+((mes_at)*30)+((ano_at)*365))

dia_ani=int(input())
mes_ani=int(input())
ano_ani=int(input())

data_aniversario= ((dia_ani)+((mes_ani)*30)+((ano_ani)*365))

idade = (data_atual - data_aniversario)//365

print(idade)