def searchDomain(lista,domain):
    domainSearch = '@' + domain
    print('Dominio buscado: ', domainSearch)
    count = 0
    for row in lista:
        if (row.getDominio() == domainSearch): 
            count+=1
    print('Cantidad de correos que tienen el mismo dominio: ', count)