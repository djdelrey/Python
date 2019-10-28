#Definindo uma fun��o
def primeiraFunc():
    print('Hello World')

print(primeiraFunc())

"""

# Definindo uma fun��o com par�metro
def primeiraFunc(nome):
    print('Hello %s' %(nome))

primeiraFunc('Aluno')

def funcLeitura():
    for i in range(0, 5):
        print("N�mero " + str(i))

funcLeitura()

# Fun��o para somar n�meros
def addNum(firstnum, secondnum):
    print("Primeiro n�mero: " + str(firstnum))
    print("Segundo n�mero: " + str(secondnum))
    print("Soma: ", firstnum + secondnum)

# Chamando a fun��o e passando par�metros
addNum(45, 3)

Vari�veis locais e globais
# Vari�vel Global
var_global = 10  # Esta � uma vari�vel global

def multiply(num1, num2):
    var_global = num1 * num2  # Esta � uma vari�vel local
    print(var_global)

multiply(5, 25)

print(var_global)

# Vari�vel Local
var_global = 10  # Esta � uma vari�vel global
def multiply(num1, num2):
    var_local = num1 * num2   # Esta � uma vari�vel local
    print(var_local)

multiply(5, 25)

print(var_local)

#Fun��es Built-in
abs(-56)
abs(23)

#Fun��es str, int, float
idade = input("Digite sua idade: ")
if idade > 13:
  print("Voc� pode acessar o Facebook")
Digite sua idade: 14

# Usando a fun��o int para converter o valor digitado
idade = int(input("Digite sua idade: "))
if idade > 13:
  print("Voc� pode acessar o Facebook")


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
Criando fun��es usando outras fun��es
In [34]:
import math

def numPrimo(num):
    '''
    Verificando se um n�mero 
    � primo. 
    '''
    if (num % 2) == 0 and num > 2: 
        return "Este n�mero n�o � primo"
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if (num % i) == 0:
            return "Este n�mero n�o � primo"
    return "Este n�mero � primo"
In [35]:
numPrimo(541)
Out[35]:
'Este n�mero � primo'
Fazendo split dos dados
In [36]:
# Fazendo split dos dados
def split_string(text):
    return text.split(" ")
In [37]:
texto = "Esta fun��o ser� bastante �til para separar grandes volumes de dados."
In [38]:
# Isso divide a string em uma lista.
print(split_string(texto))
['Esta', 'fun��o', 'ser�', 'bastante', '�til', 'para', 'separar', 'grandes', 'volumes', 'de', 'dados.']
In [39]:
# Podemos atribuir o output de uma fun��o, para uma vari�vel
token = split_string(texto)
In [40]:
token
Out[40]:
['Esta',
 'fun��o',
 'ser�',
 'bastante',
 '�til',
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
# Fun��es com n�mero vari�vel de argumentos
def printVarInfo( arg1, *vartuple ):
   # Imprimindo o valor do primeiro argumento
    print ("O par�metro passado foi: ", arg1)
   
   # Imprimindo o valor do segundo argumento 
    for item in vartuple:
        print ("O par�metro passado foi: ", item)
    return;
In [46]:
# Fazendo chamada � fun��o usando apenas 1 argumento
printVarInfo(10)
O par�metro passado foi:  10
In [47]:
printVarInfo('Chocolate', 'Morango', 'Banana')
O par�metro passado foi:  Chocolate
O par�metro passado foi:  Morango
O par�metro passado foi:  Banana
"""
