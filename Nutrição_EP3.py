# -*- coding: utf-8 -*-

# variável com a informação do usuário
arquivo_usuario = open('usuario.csv','r')

# variável com as informações dos alimentos
arquivo_alimentos = open('alimentos.csv','r')

# arquivo que conterá o índice de massa corporal do usuário e a indicação se este está saudável
arquivo_resultado = open('resultado.csv','r+')


usuario = arquivo_usuario.readlines()

def IMC(massa,altura):
    return massa/altura**2
    
def calcula_harris(altura,massa,idade,sexo):
    if sexo == 'F':
        return 447.6+(9.2*massa)+(3.1*altura)-(4.3*idade)
    else:
        return 88.36+(13.4*massa)+(4.8*altura)-(5.7*idade)

# passa as informações do usuário do arquivo para um dicioário
lista_usuario = usuario[1].split(',')
dict_usuario = dict()
dict_usuario[lista_usuario[0]] = [lista_usuario[1],lista_usuario[2],lista_usuario[3],lista_usuario[4],lista_usuario[5]]

lista_alimentos = arquivo_alimentos.readlines()
dict_alimento = dict()
for i in range(1,len(lista_alimentos)):
    linha_alimento = lista_alimentos[i].split(',')
    dict_alimento[linha_alimento[0]] = [linha_alimento[1],linha_alimento[2],linha_alimento[3],linha_alimento[4],linha_alimento[5]]
