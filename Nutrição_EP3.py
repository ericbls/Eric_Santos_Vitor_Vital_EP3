# -*- coding: utf-8 -*-

''' Importa os arquivos e funções usadas nesta programação '''

arquivo_usuario = open('usuario.csv','r+')

arquivo_alimentos = open('alimentos.csv','r')

from funcao_nutricao import *


'''
Criará uma lista com o nome do usuário e as informações fisícas associadas a ele
'''
lista_usuario = arquivo_usuario.readlines()                                    # Lista com todas as informações do usuário
descricao_usuario = lista_usuario[1].split(',')                                # Lista temporaria contendo as informações da 2° linha do arquivo "usuarios.csv"


'''
Criará um dicionário com todos os  alimentos e as informações associadas a eles
'''
dict_alimentos = dict()		                                             # Dicionário que conterá todas as informações dos alimentos
lista_alimentos = arquivo_alimentos.readlines()
for i in range(1, len(lista_alimentos)):
    linha_alimentos = lista_alimentos[i].split(',')
    dict_alimentos[linha_alimentos[0]] = [linha_alimentos[1],linha_alimentos[2],linha_alimentos[3],linha_alimentos[4],linha_alimentos[5]]

    
'''
Criará um dicionário com as informações nutricionais do usuário (o que ele consumiu em cada dia considerado)
'''
dict_ingestao = dict()                                                         # Dicionário com as informações daquilo que o usuário ingeriu por dia
lista_ingestao = list()                                                        # Uma lista em que cada elemento é uma lista com outros 3 elementos (a data, o alimento e a quantidade)
datas = list()                                                                 # Lista com todas as datas consideradas

for e in range(3,len(lista_usuario)):
    linha_ingestao = lista_usuario[e].split(',')
    lista_ingestao.append(linha_ingestao)

for y in lista_ingestao:                                                       # Esse loop adicionará em uma lista as datas do arquivo "usuario.csv" (a lista não conterá duas datas repetidas)
    if y[0] not in datas:
        datas.append(y[0])
        
for x in datas:                                                                # Esse loop criará uma chave no dicionário "dict_ingestao" para cada data da lista "datas" e associará uma lista vazia como valor de cada chave
    dict_ingestao[x] = []
    for z in lista_ingestao:                                                   # Esse loop adicionará à lista-valor, associada à chave do dicionário, uma outra lista contendo o nome do alimento consumido e a quantidade.
        if x == z[0]:                                                          # Estabelece uma condição: somente realizará a função descrita acima se a data em que o alimento foi consumido for igual a data da chave no dicionário
            dict_ingestao[x].append([z[1],z[2]])
            

'''
Criará um dicionário com as informações de quantas calorias (em Kcal) e quanto de proteínas, carboidratos e gorduras (em gramas) ele consumiu em cada dia
'''
dict_dadosnutri = dict()                                                       # Diciánario com os valores nutricionais consumidos a cada dia (calorias, proteínas, carboidratos,. Exemplo: {'07/04/15': [1553.50, 36.53, 223.57, 57.07], '06/04/15': [462.50, 7.22, 62.85, 20.25]}


for a in datas: 
    cal = 0
    prot = 0
    carb = 0
    gord = 0
    for b in range(len(dict_ingestao[a])):
        prop = float(dict_ingestao[a][b][1])/float(dict_alimentos[dict_ingestao[a][b][0]][0])   # fração de quanto o usuário consumiu de uma porção do alimento (quantidade no arquivo "alimentos.csv").
                                                                                                # Dict_ingestao[a][b][1] equivale a porção ([1]) consumida de um alimento [b] no dia [a]
                                                                                                # Dict_alimentos[dict_ingestao[a][b][0]][0] equivale a porção usada como base para os valores nutricionais do "alimentos.csv"       
        cal = cal + (float(dict_alimentos[dict_ingestao[a][b][0]][1])*prop)    # Adiciona a quantidade de calorias consumidas no alimento à quantidade de calorias já consumida no dia
                                                                               # float(dict_alimentos[dict_ingestao[a][b][0]][1]) equivale a quantidade de calorias que uma porção do alimento [b] possui        
        prot = prot + (float(dict_alimentos[dict_ingestao[a][b][0]][2])*prop)  # Adiciona a quantidade de proteínas consumidas no alimento à quantidade de proteínas já consumida no dia
                                                                               # float(dict_alimentos[dict_ingestao[a][b][0]][3]) equivale a quantidade de proteínas que uma porção do alimento [b] possui           
        carb = carb + (float(dict_alimentos[dict_ingestao[a][b][0]][3])*prop)  # Adiciona a quantidade de carboidratos consumidas no alimento à quantidade de carboidratos já consumida no dia
                                                                               # float(dict_alimentos[dict_ingestao[a][b][0]][3]) equivale a quantidade de carboidratos que uma porção do alimento [b] possui     
        gord = gord + (float(dict_alimentos[dict_ingestao[a][b][0]][4])*prop)  # Adiciona a quantidade de gorduras consumidas no alimento à quantidade de gorduras já consumida no dia
                                                                               # float(dict_alimentos[dict_ingestao[a][b][0]][4]) equivale a quantidade de gorduras que uma porção do alimento [b] possui   
    dict_dadosnutri[a] = [cal,prot,carb,gord]                                  # Coloca o valor total de calorias, proteínas, carboidratos e gorduras consumidas no dia no dicionário (como um valor), associado a uma chave, que será a data (o dia em que tudo foi consumido)

'''
Criará uma lista com as datas consideradas, só que em ordem cronológica
'''
datas_crono = sorted(datas)

'''
Criará uma lista com a quantidade calórica que usuário deveria consumir por dia, segundo a fórmula de Harris-Benedict
(considerará o mesmo número de dias que em "usuario.csv". Em outras palavras,por exemplo, se no arquivo só foi informado o que o usuário consumiu em duas datas, a lista criada só possuirá dois valores - a quantidade de calorias que ele deveria consumir nas duas datas)
'''

calorias_necessarias = [0]*len(datas_crono)
for g in range(len(calorias_necessarias)):
    calorias_necessarias[g] = calcula_harris(float(descricao_usuario[1]),float(descricao_usuario[2]),descricao_usuario[3],float(descricao_usuario[4]),descricao_usuario[5])


'''
Escreverá as informações necessárias no arquivo "resultado.csv"
'''
resultado = open('resultado.txt','w',encoding='utf8')

resultado.write('Abaixo estão o seu índice de massa corporal (IDM), a quantidade de calorias que você consumiu\ne o quanto foi consumido a mais ou a menos segundo a fórmula de Harris-Benedict em cada dia e,\npor fim, se você está subnutrido, saudável, possui sobrepeso, ou obesidade de graus I, II ou III\n\n')

imc = IMC(float(descricao_usuario[2]),float(descricao_usuario[4]))

calorias_recomendadas = calcula_harris(float(descricao_usuario[1]),float(descricao_usuario[2]),descricao_usuario[3],float(descricao_usuario[4]),descricao_usuario[5])

resultado.write('Dia, calorias consumidas e quantas calorias você consumiu a mais ou a menos do que deveria:\n\n')

for h in datas_crono:
    calorias_consumidas = dict_dadosnutri[h][0]
    resultado.write('dia %s   '%h)
    resultado.write('calorias consumidas: %f   '%calorias_consumidas)
    resultado.write('calorias consumidas a mais/menos: %f\n\n'%(calorias_consumidas-calorias_recomendadas))

if imc<18.5:
    resultado.write('Você está subnutrido, segundo o seu IMC (calculado através de sua massa e altura)\n')
elif imc>=18.5 and imc<=24.9:
    resultado.write('Você está saudável, segundo o seu IMC (calculado através de sua massa e altura)\n')
elif imc>=25 and imc<=29.9:
    resultado.write('Você está um pouco acima do peso, segundo o seu IMC (calculado através de sua massa e altura)\n')
elif imc>=30 and imc<=34.9:
    resultado.write('Você possui um grau I de obesidade, segundo o seu IMC (calculado através de sua massa e altura)\n')
elif imc>=35 and imc<=39.9:
    resultado.write('Você possui um grau II de obesidade, segundo o seu IMC (calculado através de sua massa e altura)\n')
else:
    resultado.write('Você possui um sério caso de obesidade, segundo o seu IMC (calculado através de sua massa e altura)\n')


'''
Plotará os gráficos das calorias
'''

import matplotlib.pyplot as plt
import numpy as np
    
calorias_consumidas = []
for a in datas_crono:
    calorias_consumidas.append(dict_dadosnutri[a][0])
     
todos_elementos = calorias_consumidas + calorias_necessarias
     
y = calorias_consumidas
k = calorias_necessarias
    
ax = plt.subplot(111)
ax.bar(np.arange(0,len(datas_crono))+0.8, y,width=0.2,color='b')
ax.bar(np.arange(0,len(datas_crono))+1.0, k,width=0.2,color='r')
ax.set_xticks(np.arange(len(datas_crono))+1)
ax.set_xticklabels(datas_crono)
plt.axis([0,len(datas_crono)+1,0,max(todos_elementos)+200])
legenda="Calorias ingeridas(Kcal)","Calorias recomendadas(Kcal)"
plt.legend(legenda,bbox_to_anchor=(1.0, -0.15),ncol=2,fancybox=True, shadow=True)
plt.show()


''' 
Plotará os gráficos do consumo dos outros nutrientes
'''

import matplotlib.pyplot as plt
import numpy as np
    
proteinas = list()
carboidratos = list()
gorduras = list()

for a in datas_crono:
    proteinas.append(dict_dadosnutri[a][1])
    carboidratos.append(dict_dadosnutri[a][2])
    gorduras.append(dict_dadosnutri[a][3])        

todos_elementos = proteinas + carboidratos + gorduras    
    
y = proteinas
z = carboidratos
k = gorduras
    
ax = plt.subplot(111)
ax.bar(np.arange(0,len(datas_crono))+0.7, y,width=0.2,color='b')
ax.bar(np.arange(0,len(datas_crono))+0.9, z,width=0.2,color='g')
ax.bar(np.arange(0,len(datas_crono))+1.1, k,width=0.2,color='r')
ax.set_xticks(np.arange(len(datas_crono))+1)
ax.set_xticklabels(datas_crono)
plt.axis([0,len(datas_crono)+1,0,max(todos_elementos)+5])
legendas="Proteínas","Carboidratos","Gorduras"
plt.legend(legendas,bbox_to_anchor=(1.0, -0.15),ncol=2,fancybox=True, shadow=True)
plt.show()


arquivo_alimentos.close
arquivo_usuario.close
resultado.close