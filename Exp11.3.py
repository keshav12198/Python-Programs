import random
def roll_dice(n,t):
	while t:
		a = random.randint(1,n+1)
		print a
		t-=1
	return "That's All!"

a = input("Enter no. of sides of dice ")
b = input("Enter no. of times dice is rolled")
print roll_dice(a,b)