# -*- coding: utf-8 -*-

''' variável com a informação do usuário '''
arquivo_usuario = open('usuario.csv','r+')

''' variável com as informações dos alimentos '''
arquivo_alimentos = open('alimentos.csv','r')

''' arquivo que conterá o índice de massa corporal do usuário e a indicação se este está saudável '''
arquivo_resultado = open('resultado.csv','r+')



def IMC(massa,altura):
    return massa/altura**2
    
def calcula_harris(idade,massa,sexo,altura,exercicio):                         # Define a função que calculará o TMB e o grau de atividade
    if sexo == 'F':
        if exercicio == 'minimo':
            return (447.6+(9.2*massa)+(3.1*altura)-(4.3*idade))*1.2
        elif exercicio == 'baixo':
            return (447.6+(9.2*massa)+(3.1*altura)-(4.3*idade))*1.375
        elif exercicio == 'alto':
            return (447.6+(9.2*massa)+(3.1*altura)-(4.3*idade))*1.725
        elif exercicio == 'muito alto':
            return (447.6+(9.2*massa)+(3.1*altura)-(4.3*idade))*1.9
        else:
            return (447.6+(9.2*massa)+(3.1*altura)-(4.3*idade))*1.55
    if sexo == 'M':
        if exercicio == 'minimo':
            return (88.36+(13.4*massa)+(4.8*altura)-(5.7*idade))*1.2
        elif exercicio == 'baixo':
            return (88.36+(13.4*massa)+(4.8*altura)-(5.7*idade))*1.375
        elif exercicio == 'alto':
            return (88.36+(13.4*massa)+(4.8*altura)-(5.7*idade))*1.725
        elif exercicio == 'muito alto':
            return (88.36+(13.4*massa)+(4.8*altura)-(5.7*idade))*1.9
        else:
            return (88.36+(13.4*massa)+(4.8*altura)-(5.7*idade))*1.55
    else:
        print('Este programa não se aplica a você, seja lá o que você for')


'''
Criará um dicionário com o nome do usuário e as informações fisícas associadas a ele
'''
lista_usuario = arquivo_usuario.readlines()                                    # Lista com todas as informações do usuário
descricao_usuario = lista_usuario[1].split(',')                                # Lista temporaria contendo as informações da 2° linha do arquivo "usuarios.csv"
info_usuario = dict()                                                          # Dicionário contendo as informações do usuário sobre o físico e hábitos apenas
info_usuario[descricao_usuario[0]] = [descricao_usuario[1],descricao_usuario[2],descricao_usuario[3],descricao_usuario[4],descricao_usuario[5]]


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
cal = 0
prot = 0
carb = 0
gord = 0
for a in datas:                                                                
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
Criará uma lista com as datas consideradas, só que em ordem cronológica1
'''
datas_crono = list()                                                           # Lista com as datas em ordem cronológica
temp = list()

for c in range(len(datas)):                                                    # A lista "temp", conterá cada data, separando o dia, mês e ano como um elemento de uma lista. Exemplo: 06/04/15 se tornará ['06','04','15']
    temp.append(datas[c].split('/'))    
    
for d in range(len(datas)):                                                    # Esse loop adicionará as datas em ordem cronológica à lista "datas_crono"
    for e in range(len(datas)):    
        if datas[d] in datas_crono:                                            # Garantirá que não adicione datas repetidas na lista "datas_crono"
            break
        if temp[d][2] <= temp[e][2]:                                           # Essa e as próximas três linhas comparam um elemento com um outro, checando primeiramente o ano, depois o mês e só então a data.
            if temp[d][1] <= temp[e][1]:                                       # Essas quatro linhas, portanto, são as que adicionam as datas em ordem cronológicas
                if temp[d][0] < temp[e][0]:                                    # Aqui é adicionado a data.
                    datas_crono.append(datas[d])
for f in datas:                                                                # A última data não é adicionada à lista pelos loops anteriores, portanto este loop serve para adicioná-lo
    if f not in datas_crono:
        datas_crono.append(f)


'''
Criará uma lista com a quantidade calórica que usuário deveria consumir por dia, segundo a fórmula de Harris-Benedict
(considerará o mesmo número de dias que em "usuario.csv". Em outras palavras,por exemplo, se no arquivo só foi informado o que o usuário consumiu em duas datas, a lista criada só possuirá dois valores - a quantidade de calorias que ele deveria consumir nas duas datas)
'''
calorias_necessarias = [0]*len(datas_crono)
for g in range(len(calorias_necessarias)):
    calorias_necessarias[g] = calcula_harris(float(descricao_usuario[1]),float(descricao_usuario[2]),descricao_usuario[3],float(descricao_usuario[4]),descricao_usuario[5])

print(calorias_necessarias)

arquivo_alimentos.close
arquivo_usuario.close
arquivo_resultado.close