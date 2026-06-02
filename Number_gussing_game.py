import random

n = random.randint(1,10)

for i in range(6) :
    num = int(input("Guess the number : "))

    if(num==n) :
        print("Correct!!! You Won ")
        break
    elif(num<n) :
        print("Too Low ")
    elif(num>n) :
        print("Too High ")

else :
	print("You Cross the limit , for continue plyaing restart the game again!!! ")
