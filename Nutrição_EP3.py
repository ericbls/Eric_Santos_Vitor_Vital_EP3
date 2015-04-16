# -*- coding: utf-8 -*-

# variável com a informação do usuário
arquivo_usuario = open('usuario.csv','r')

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
criará um dicionário com o nome do usuário e as informações fisícas associadas a ele
'''
lista_usuario = arquivo_usuario.readlines()
descrição_usuario = lista_usuario[1].split(',')
info_usuario = dict()
info_usuario[descrição_usuario[0]] = [descrição_usuario[1],descrição_usuario[2],descrição_usuario[3],descrição_usuario[4],descrição_usuario[5]]


'''
criará um dicionário com todos os  alimentos e as informações associadas a eles
'''
dict_alimentos = dict()
lista_alimentos = arquivo_alimentos.readlines()
for i in range(1, len(lista_alimentos)):
    linha_alimentos = lista_alimentos[i].split(',')
    dict_alimentos[linha_alimentos[0]] = [linha_alimentos[1],linha_alimentos[2],linha_alimentos[3],linha_alimentos[4],linha_alimentos[5]]
  