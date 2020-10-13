import random

num = random.randint(1, 10)
chance = 5

print ('Who are challenging?')
name = input()

print ("OK ", name , ", can you discovery the number that I'm thinking between 1 and 10? How many chances do you need to answer? You will have" ,chance,  "chances to Win")

for tried in range(1,chance+1):
    leftchoice = chance - tried
    print ("This is your chance number",tried,"to win, has left", leftchoice ,"chance(s)")
    print ('insert your number:', end='')
    choice = int(input())

    if choice < num:
        print("You need to try again, because your number is too low")
    elif choice > num:
        print("Ops, not at this time... your number is highter than my number")
    else:
        break

if choice == num:
    print ("Thats correct!! Wowwww, You beat me in", tried, "attempts" )
else:
    print('Not at this time =D, I won!! My number was', num )
