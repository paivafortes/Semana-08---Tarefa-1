#Escreva um programa que leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano) e escreva qual delas é a mais recente.
def data_1(dia, mes, ano):
    data_1 = dia + (mes *30) + (ano * 365)
    return data_1

def data_2(dia_2, mes_2, ano_2):
    data_2= dia_2 + (mes_2 * 30) + (ano_2 * 365)
    return data_2
def data_recente(data_1, data_2):
    if data_1 >= data_2:
        print(f'{dia}/{mes}/{ano}')
    elif data_1 < data_2:
        print(f'{dia_2}/{mes_2}/{ano_2}')
        
dia=int(input())
mes=int(input())
ano=int(input())

dia_2=int(input())
mes_2=int(input())
ano_2=int(input())

valor_1=data_1(dia,mes,ano)
valor_2=data_2(dia_2, mes_2,ano_2)
data_r=data_recente(valor_1,valor_2)

        