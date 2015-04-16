# -*- coding: utf-8 -*-

# variável com a informação do usuário
arquivo_usuario = open('usuario.csv','r')

# variável com as informações dos alimentos
arquivo_alimentos = open('alimentos.csv','r')

# arquivo que conterá o índice de massa corporal do usuário e a indicação se este está saudável
arquivo_resultado = open('resultado.txt','r+')


usuario = arquivo_usuario.readlines()

print (usuario)

def IDM(massa,altura):
    return massa/altura**2
    
def calcula_harris(altura,massa,idade,sexo):
    if sexo == 'F':
        return 447.6+(9.2*massa)+(3.1*altura)-(4.3*idade)
    else:
        return 88.36+(13.4*massa)+(4.8*altura)-(5.7*idade)

# passo intermediário para transformar as informações do usuário em dicionário
lista_usuario = usuario[1].split(',')

# adicionando as informações do usuário num dicionário
info_usuario = dict()
info_usuario[lista_usuario[0]] = [lista_usuario[1],lista_usuario[2],lista_usuario[3],lista_usuario[4],lista_usuario[5]]
