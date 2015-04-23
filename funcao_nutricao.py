# -*- coding: utf-8 -*-

'''
Calculará o IMC segundo uma massa e altura
'''

def IMC(massa,altura):                                                         # Calcula o IMC do usuario a partir de sua massa e altura
    ''' 
    >>> IMC(90,1.88)
    25.46
    >>> IMC(65,1.68)
    23.03
    >>> IMC(80,1.78)
    25.25
    '''
    
    return float('{0:.2f}'.format(massa/altura**2))


'''
Calculará o a quantidade de calorias que o usuário deveria ingerir
'''    
def calcula_harris(idade,massa,sexo,altura,exercicio):                         # Define a função que calculará a quantidade de calorias que o usuario deveria consumir por dia, através da equação de Harris Benedict
    '''
    >>> calcula_harris(18,65,'M',1.55,'baixo')
    2201.05
    >>> calcula_harris(18,70,'M',1.70,'médio')
    2696.63
    >>> calcula_harris(18,80,'M',1.85,'muito ativo')
    3696.94
    >>> calcula_harris(60,65,'M',1.55,'mínimo')
    1633.63
    >>> calcula_harris(60,70,'M',1.70,'médio')
    2325.56
    >>> calcula_harris(60,80,'M',1.85,'alto')
    2943.47
    >>> calcula_harris(26,65,'M',1.55,'baixo')
    2138.35
    >>> calcula_harris(26,70,'M',1.70,'médio')
    2625.95
    >>> calcula_harris(26,80,'M',1.85,'alto')
    3277.78
    >>> calcula_harris(18,60,'F',1.55,'baixo')
    1928.71
    >>> calcula_harris(18,70,'F',1.70,'muito ativo')
    2928.28
    >>> calcula_harris(18,75,'F',1.80,'médio')
    2508.21
    >>> calcula_harris(60,60,'F',1.55,'alto')
    2108.12
    >>> calcula_harris(60,70,'F',1.70,'mínimo')
    1632.72
    >>> calcula_harris(60,75,'F',1.80,'baixo')
    1976.7
    >>> calcula_harris(26,60,'F',1.55,'alto')
    2360.32
    >>> calcula_harris(26,70,'F',1.70,'médio')
    2335.54
    >>> calcula_harris(26,75,'F',1.80,'muito ativo')
    3009.22
    '''
    
    altura = altura*100   
    
    if sexo == 'F':
        if exercicio == 'mínimo':
            return float('{0:.2f}'.format((447.6+(9.2*massa)+(3.1*altura)-(4.3*idade))*1.2))
        elif exercicio == 'baixo':
            return float('{0:.2f}'.format((447.6+(9.2*massa)+(3.1*altura)-(4.3*idade))*1.375))
        elif exercicio == 'alto':
            return float('{0:.2f}'.format((447.6+(9.2*massa)+(3.1*altura)-(4.3*idade))*1.725))
        elif exercicio == 'muito ativo':
            return float('{0:.2f}'.format((447.6+(9.2*massa)+(3.1*altura)-(4.3*idade))*1.9))
        else:
            return float('{0:.2f}'.format((447.6+(9.2*massa)+(3.1*altura)-(4.3*idade))*1.55))
    if sexo == 'M':
        if exercicio == 'mínimo':
            return float('{0:.2f}'.format((88.36+(13.4*massa)+(4.8*altura)-(5.7*idade))*1.2))
        elif exercicio == 'baixo':
            return float('{0:.2f}'.format((88.36+(13.4*massa)+(4.8*altura)-(5.7*idade))*1.375))
        elif exercicio == 'alto':
            return float('{0:.2f}'.format((88.36+(13.4*massa)+(4.8*altura)-(5.7*idade))*1.725))
        elif exercicio == 'muito ativo':
            return float('{0:.2f}'.format((88.36+(13.4*massa)+(4.8*altura)-(5.7*idade))*1.9))
        else:
            return float('{0:.2f}'.format((88.36+(13.4*massa)+(4.8*altura)-(5.7*idade))*1.55))
    else:
        print('Este programa não se aplica a você, seja lá o que você for')
         