# -*- coding: utf-8 -*-

'''
Calculará o IMC segundo uma massa e altura
'''

def IMC(massa,altura):
  
    return float('{0:.2f}'.format(massa/altura**2))


'''
Calculará o a quantidade de calorias que o usuário deveria ingerir
'''    
def calcula_harris(idade,massa,sexo,altura,exercicio):                         # Define a função que calculará o TMB e o grau de atividade
    '''
    >>> calcula_harris(18,65,'M',1.55,'baixo')
    1188.28 
    >>> calcula_harris(18,70,'M',1.70,'intermediario')
    144.48 
    >>> calcula_harris(18,80,'M',1.85,'muito alto')
    2026.62 
    >>> calcula_harris(60,65,'M',1.55,'minimo')
    749.76 
    >>> calcula_harris(60,70,'M',1.70,'intermediario')
    1073.41 
    >>> calcula_harris(60,80,'M',1.85,'alto')
    1426.99 
    >>> calcula_harris(26,65,'M',1.55,'baixo')
    1125.58 
    >>> calcula_harris(26,70,'M',1.70,'intermediario')
    1373.80 
    >>> calcula_harris(26,80,'M',1.85,'alto')
    1761.29 
    >>> calcula_harris(18,60,'F',1.55,'baixo')
    1487.48 
    >>> calcula_harris(18,70,'F',1.70,'muito alto')
    2231.11 
    >>> calcula_harris(18,75,'F',1.80,'intermediario')
    1891.90 
    >>> calcula_harris(60,60,'F',1.55,'alto')
    2177.65 
    >>> calcula_harris(60,70,'F',1.70,'minimo')
    1862.95 
    >>> calcula_harris(60,75,'F',1.80,'baixo')
    1926.62 
    >>> calculla_harris(26,60,'F',1.55,'alto')
    1925.45 
    >>> calculla_harris(26,70,'F',1.70,'intermediario')
    1873.44 
    >>> calculla_harris(26,75,'F',1.80,'muito alto')
    2384.46 
    '''    
    if sexo == 'F':
        if exercicio == 'minimo':
            return float('{0:.2f}'.format((447.6+(9.2*massa)+(3.1*altura)-(4.3*idade))*1.2))
        elif exercicio == 'baixo':
            return float('{0:.2f}'.format((447.6+(9.2*massa)+(3.1*altura)-(4.3*idade))*1.375))
        elif exercicio == 'alto':
            return float('{0:.2f}'.format((447.6+(9.2*massa)+(3.1*altura)-(4.3*idade))*1.725))
        elif exercicio == 'muito alto':
            return float('{0:.2f}'.format((447.6+(9.2*massa)+(3.1*altura)-(4.3*idade))*1.9))
        else:
            return float('{0:.2f}'.format((447.6+(9.2*massa)+(3.1*altura)-(4.3*idade))*1.55))
    if sexo == 'M':
        if exercicio == 'minimo':
            return float('{0:.2f}'.format((88.36+(13.4*massa)+(4.8*altura)-(5.7*idade))*1.2))
        elif exercicio == 'baixo':
            return float('{0:.2f}'.format((88.36+(13.4*massa)+(4.8*altura)-(5.7*idade))*1.375))
        elif exercicio == 'alto':
            return float('{0:.2f}'.format((88.36+(13.4*massa)+(4.8*altura)-(5.7*idade))*1.725))
        elif exercicio == 'muito alto':
            return float('{0:.2f}'.format((88.36+(13.4*massa)+(4.8*altura)-(5.7*idade))*1.9))
        else:
            return float('{0:.2f}'.format((88.36+(13.4*massa)+(4.8*altura)-(5.7*idade))*1.55))
    else:
        print('Este programa não se aplica a você, seja lá o que você for')
           