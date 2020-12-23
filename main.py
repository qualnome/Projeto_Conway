#Sitio para escrevermos o codigo
def cria_mundo (linhas,colunas):
    l= []
    l2 = []
    for x in range (colunas):      
        l += [0,]    
    for x in range (linhas):       
        l2.append(l)
    return(l2)
 
l2=cria_mundo(5,5)
def tamanho_mundo (l2):
    tuplo=(len(l2),)
    tuplo +=(len(l2),)
    return(tuplo)
print(tamanho_mundo(l2))
 
