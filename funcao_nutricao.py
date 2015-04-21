# -*- coding: utf-8 -*-

'''
Calculará o IMC segundo uma massa e altura
'''

def IMC(massa,altura):
    return massa/altura**2

'''
Calculará o a quantidade de calorias que o usuário deveria ingerir
'''    
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
Plotará os gráficos das calorias
'''

def grafico_calorias(dias,cal_ingerida,cal_recomendada):
    import matplotlib.pyplot as plt
    import numpy as np
    
    calorias_consumidas = []
    for a in dias:
        calorias_consumidas.append(cal_ingerida)
     
    todos_elementos = calorias_consumidas + cal_recomendada
     
    ax = plt.subplot(111)
    ax.bar(np.arange(0,len(dias))+0.8, calorias_consumidas,width=0.2,color='b')
    ax.bar(np.arange(0,len(dias))+1.0, cal_recomendada,width=0.2,color='r')
    ax.set_xticks(np.arange(len(dias))+1)
    ax.set_xticklabels(dias)
    plt.axis([0,len(dias)+1,0,max(todos_elementos)+200])
    legenda="Calorias ingeridas(Kcal)","Calorias recomendadas(Kcal)"
    plt.legend(legenda,bbox_to_anchor=(1.0, -0.15),ncol=2,fancybox=True, shadow=True)
    plt.show()   

''' 
Plotará os gráficos do consumo dos outros nutrientes
'''
def grafico_nutricional(dias,prot_ingerida,carb_ingerido,gord_ingerida):
    import matplotlib.pyplot as plt
    import numpy as np
    
    proteinas = list()
    carboidratos = list()
    gorduras = list()
    for a in dias:
        proteinas.append(prot_ingerida)
        carboidratos.append(carb_ingerido)
        gorduras.append(gord_ingerida)        

    todos_elementos = proteinas+carboidratos+gorduras    
    
    y = proteinas
    z = carboidratos
    k = gorduras
    
    ax = plt.subplot(111)
    ax.bar(np.arange(0,len(dias))+0.7, y,width=0.2,color='b')
    ax.bar(np.arange(0,len(dias))+0.9, z,width=0.2,color='g')
    ax.bar(np.arange(0,len(dias))+1.1, k,width=0.2,color='r')
    ax.set_xticks(np.arange(len(dias))+1)
    ax.set_xticklabels(dias)
    plt.axis([0,len(dias)+1,0,max(todos_elementos)+5])
    legendas="Proteínas","Carboidratos","Gorduras"
    plt.legend(legendas,bbox_to_anchor=(1.0, -0.15),ncol=2,fancybox=True, shadow=True)
    plt.show()