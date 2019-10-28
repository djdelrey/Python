#Definindo uma função
def primeiraFunc():
    print('Hello World')

print(primeiraFunc())

"""

# Definindo uma função com parâmetro
def primeiraFunc(nome):
    print('Hello %s' %(nome))

primeiraFunc('Aluno')

def funcLeitura():
    for i in range(0, 5):
        print("Número " + str(i))

funcLeitura()

# Função para somar números
def addNum(firstnum, secondnum):
    print("Primeiro número: " + str(firstnum))
    print("Segundo número: " + str(secondnum))
    print("Soma: ", firstnum + secondnum)

# Chamando a função e passando parâmetros
addNum(45, 3)

Variáveis locais e globais
# Variável Global
var_global = 10  # Esta é uma variável global

def multiply(num1, num2):
    var_global = num1 * num2  # Esta é uma variável local
    print(var_global)

multiply(5, 25)

print(var_global)

# Variável Local
var_global = 10  # Esta é uma variável global
def multiply(num1, num2):
    var_local = num1 * num2   # Esta é uma variável local
    print(var_local)

multiply(5, 25)

print(var_local)

#Funções Built-in
abs(-56)
abs(23)

#Funções str, int, float
idade = input("Digite sua idade: ")
if idade > 13:
  print("Você pode acessar o Facebook")
Digite sua idade: 14

# Usando a função int para converter o valor digitado
idade = int(input("Digite sua idade: "))
if idade > 13:
  print("Você pode acessar o Facebook")


print(int("26"))
print(float("123.345"))
print(str(14))
Out[23]:

print(len([23,34,45,46]))

array = ['a', 'b', 'c']

print(max(array))
print(min(array))

array = ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']

print(array)

print(max(array))
print(min(array))
list1 = [23, 23, 34, 45]
In [33]:
sum(list1)
Out[33]:
125
Criando funções usando outras funções
In [34]:
import math

def numPrimo(num):
    '''
    Verificando se um número 
    é primo. 
    '''
    if (num % 2) == 0 and num > 2: 
        return "Este número não é primo"
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if (num % i) == 0:
            return "Este número não é primo"
    return "Este número é primo"
In [35]:
numPrimo(541)
Out[35]:
'Este número é primo'
Fazendo split dos dados
In [36]:
# Fazendo split dos dados
def split_string(text):
    return text.split(" ")
In [37]:
texto = "Esta função será bastante útil para separar grandes volumes de dados."
In [38]:
# Isso divide a string em uma lista.
print(split_string(texto))
['Esta', 'função', 'será', 'bastante', 'útil', 'para', 'separar', 'grandes', 'volumes', 'de', 'dados.']
In [39]:
# Podemos atribuir o output de uma função, para uma variável
token = split_string(texto)
In [40]:
token
Out[40]:
['Esta',
 'função',
 'será',
 'bastante',
 'útil',
 'para',
 'separar',
 'grandes',
 'volumes',
 'de',
 'dados.']
In [41]:
caixa_baixa = "Este Texto Deveria Estar Todo Em LowerCase"
In [42]:
def lowercase(text):
    return text.lower()
In [43]:
lowercased_string = lowercase(caixa_baixa)
In [44]:
lowercased_string
Out[44]:
'este texto deveria estar todo em lowercase'
In [45]:
# Funções com número variável de argumentos
def printVarInfo( arg1, *vartuple ):
   # Imprimindo o valor do primeiro argumento
    print ("O parâmetro passado foi: ", arg1)
   
   # Imprimindo o valor do segundo argumento 
    for item in vartuple:
        print ("O parâmetro passado foi: ", item)
    return;
In [46]:
# Fazendo chamada à função usando apenas 1 argumento
printVarInfo(10)
O parâmetro passado foi:  10
In [47]:
printVarInfo('Chocolate', 'Morango', 'Banana')
O parâmetro passado foi:  Chocolate
O parâmetro passado foi:  Morango
O parâmetro passado foi:  Banana
"""
