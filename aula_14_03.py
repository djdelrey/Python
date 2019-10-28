
lista1 = [1,2,3,4,5,6]
lista2 = [9,10,11,12]

lista1.append(7)

lista2.append(8)

juntalist = [lista1]+[lista2]

for listajunta in juntalist:
    if listajunta:
        print(listajunta)


#lista1 = [1,2,3,4,5,6]
#lista2 = [9,10,11,12]

#lista1.append(7)

#lista2.append(8)

#for lista in lista1:
#    if lista:
#        print('Lista NÂ°1 com',lista1)

#for lista in lista2:
#    if lista:
#        print('Lista NÂ°2 com',lista2)