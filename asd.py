list = [1,2,3,4,5,9]
valida = 0
y = input('digite um numero ???')

#list.append(7)

for x in list:
    if(x == int(y)):
        print('numero encontrado =>' + str(x))
        valida = 1
        break

if (valida == 0):
    print('valor não encontrado !!!')
