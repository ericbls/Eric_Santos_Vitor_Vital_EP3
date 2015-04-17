# -*- coding: utf-8 -*-

# variável com a informação do usuário
arquivo_usuario = open('usuario.csv','r+')

# variável com as informações dos alimentos
arquivo_alimentos = open('alimentos.csv','r')

# arquivo que conterá o índice de massa corporal do usuário e a indicação se este está saudável
arquivo_resultado = open('resultado.csv','r+')



def IMC(massa,altura):
    return massa/altura**2
    
def calcula_harris(altura,massa,idade,sexo):
    if sexo == 'F':
        return 447.6+(9.2*massa)+(3.1*altura)-(4.3*idade)
    else:
        return 88.36+(13.4*massa)+(4.8*altura)-(5.7*idade)


'''
Criará um dicionário com o nome do usuário e as informações fisícas associadas a ele
'''
lista_usuario = arquivo_usuario.readlines()			# Lista com todas as informações do usuário
descricao_usuario = lista_usuario[1].split(',')			# Lista temporaria contendo as informações da 2° linha do arquivo "usuarios.csv"
info_usuario = dict()			# Dicionário contendo as informações do usuário sobre o físico e hábitos apenas
info_usuario[descricao_usuario[0]] = [descricao_usuario[1],descricao_usuario[2],descricao_usuario[3],descricao_usuario[4],descricao_usuario[5]]


'''
Criará um dicionário com todos os  alimentos e as informações associadas a eles
'''
dict_alimentos = dict()			# Dicionário que conterá todas as informações dos alimentos
lista_alimentos = arquivo_alimentos.readlines()
for i in range(1, len(lista_alimentos)):
    linha_alimentos = lista_alimentos[i].split(',')
    dict_alimentos[linha_alimentos[0]] = [linha_alimentos[1],linha_alimentos[2],linha_alimentos[3],linha_alimentos[4],linha_alimentos[5]]

    
'''
Criará um dicionário com as informações nutricionais do usuário
'''
dict_ingestao = dict()         # Dicionário com as informações daquilo que o usuário ingeriu por dia
lista_ingestao = list()         # Uma lista em que cada elemento é uma lista com outros 3 elementos (a data, o alimento e a quantidade)
datas = list()          # Lista com todas as datas consideradas

for e in range(3,len(lista_usuario)):
    linha_ingestao = lista_usuario[e].split(',')
    lista_ingestao.append(linha_ingestao)

for y in lista_ingestao:
    if y[0] not in datas:
        datas.append(y[0])
        
for x in datas:
    dict_ingestao[x] = []
    for z in lista_ingestao:
        if x == z[0]:      
            dict_ingestao[x].append([z[1],z[2]])
            
            
print(datas)
print(' ')
print(lista_ingestao)
print(' ')
print(dict_ingestao)


arquivo_alimentos.close
arquivo_usuario.close
arquivo_resultado.close