import random
import time

chance = 40



print ("Vamos lá, vamos ver quem ganha!!")
print ("Qual o nome do primeiro participante?")
user01 = input()

print ("Qual o nome do segundo participante?")
user02 = input()

print ("OK, já temos os nomes dos participantes... vamos ver quem vai ganhar", user01, "ou", user02)

print ('Insira seu numero', user01, ':', end='')
choice01 = int(input())

print ('Insira seu numero', user02, ':', end='')
choice02 = int(input())

for tried in range(1,chance+1):
    num = random.randint(1, 20)  

    if choice01 == num:
        print("Temos um ganhador!! =D")
        print("...")
        time.sleep(2)
        print("Voces estao anciosas?")
        time.sleep(2)
        print("E o ganhador é...")
        time.sleep(1)
        print("vamos para a contagem regressiva... 5")
        time.sleep(1)
        print("4, muita calma...")
        time.sleep(1)
        print("3, respirem...")
        time.sleep(1)
        print("2, ta chegando a hora...")
        time.sleep(1)
        print("1... e o ganhador é...")
        time.sleep(2)
        print("A", user01, "o numero sorteado foi o", num)
        break
    elif choice02 == num:
        print("Temos um ganhador!! =D")
        print("...")
        time.sleep(2)
        print("Voces estao anciosas?")
        time.sleep(2)
        print("E o ganhador é...")
        time.sleep(3)
        print("vamos para a contagem regressiva... 5")
        time.sleep(2)
        print("4, muita calma...")
        time.sleep(2)
        print("3, respirem...")
        time.sleep(2)
        print("2, ta chegando a hora...")
        time.sleep(2)
        print("1... e o ganhador é...")
        time.sleep(3)
        print("A", user02, "o numero sorteado foi o", num)
        break
    else:
        print ("Erraram o numero sorteado foi ",num)
        input("Pressione <ENTER> para sortear o proximo numero...")        


