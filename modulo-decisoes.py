#IF
a = 9
if (a==10):
    print ("O valor de a é igual a 10")
else:
    print ("O valor de A não é 10, é ",a)

#IF 2

acao = int(input ("Digite '1' para sim e '2' para nao:"))
if (acao==1):
    print ("Você disse que sim")
else:
    if(acao==2):
        print ("Voce disse que não")
    else:
        print ("Selecao invalida, voce digitou ",acao)


#IF 3
idade = int(input("Informe sua idade:"))
if (idade<=0):
    print ("Sua idade nao pode ser menor que 0")
elif(idade >150):
    print ("A sua idade não pode ser maior que 150 anos!")
elif (idade<18):
    print ("Voce precisa ter mais que 18 anos")

#IF 4 #COMPARATIVOS
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite o 2o numero: "))

if (num1==num2): #operador de igualdade
    print ("O numero %d é igual ao %d." %(num1,num2))
if (num1!=num2): #operador de diferença
    print ("O numero %d é diferente de %d." %(num1,num2))
if (num1<num2): #menor que 
    print ("O numero %d é menor que o numero %d" %(num1,num2))
if (num1>num2): #maior que
    print ("O numero %d é maior que o numero %d" %(num1,num2))
if (num1<=num2): #menor ou igual
    print ("O numero %d é menor ou igual ao numer %d" %(num1,num2))
if (num1>=num2): #maior ou igual
    print ("O numero %d é maior ou igual ao numero %d" %(num1,num2))