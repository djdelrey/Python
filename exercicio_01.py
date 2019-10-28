"""
# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.x
# criando lista x = []
# criando tupla x = ()
# criando dicionario x={}
x = [1,2,3,4,5,6,7,8,9,10]
for  y in x:
	print(y)
"""

"""	
# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
x = ['futebol','voley','basquete']
#print(x)
for y in x:
	print(y)
"""
	
"""
# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
str1 = 'Manoel'
str2 = 'Pereira'
str3 = str1 + ' ' + str2
print(str3)
"""

"""
# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
#                objeto tupla para verificar quantas vezes o número 4 aparece na tupla
tlp = (1, 2, 2, 3, 4, 4, 4, 5)
print(tlp.count(4))
"""


"""
# Exercício 5 - Crie um dicionário vazio e imprima na tela
dct = {}
print(dct)
"""

"""
# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dct = {1:'Marcelo',2:'Manoel',3:'Luis'}
#print(dct)

for k,v in dct.items():
	print(k,v)
"""	

"""	
# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dct = {1:'Marcelo',2:'Manoel',3:'Luis'}
dct[4]='Claudio'
print (dct)

"""
"""
# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
#                Imprima o dicionário na tela.

dct = {1:[1,2,3],2:1000,3:3000}
for k,v in dct.items():
	print(k,v)
"""

"""
# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
#                o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
#                o quarto elemento um valor do tipo float.Imprima a lista na tela.
lst = ['Aula 01',(1,2),{1:'aaa',2:'bbb'},float(4)]
for x in lst:
	print(x)
"""

"""
# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18 
frase = 'Cientista de Dados é o profissional mais valorizado do momento !!!'
print(frase[1:18])
"""                 

"""
x = [1,2,3,4,5,6,7,8,9,10,]
for  y in x:
	print(y)
	
while y 
     if x % 2 == 0:
         print(x)
     x = x + 1


x = [1,2,3,4,5,6,7,8,9,10,]  
for  y in x:  

if resultado == 0:
    print(y)
else:
    print('O número {} é IMPAR'.format(numero)) 
    
 """
 
 cont = 0
while cont<100:
 cont = cont + 2
 print "%d" % (cont)
