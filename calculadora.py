num1 =int( input('digite primeiro numero: '))
num2 =int( input('digite segundo numero: '))

operador = input('qual operação')

if operador == '+':
     print(num1 + num2)

elif operador == '-':
      print(num1 - num2)

elif operador == '*':
    print(num1 * num2)

elif operador == '/':
      print(num1 / num2)

else:
    print('bye')
