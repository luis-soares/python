print ('Divide 10 by ?')
divideBy = input()
try:
    if int(divideBy) <= 10:
        value = 10 / int(divideBy)
        print(value)      
except ValueError:
    print('Error: Numero invalido')  
except ZeroDivisionError:
    print('Error: Nao pode dividir por 0')


