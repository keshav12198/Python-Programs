import random
def rand_divis_3():
	a = random.randint(1,1001)
	print "The random number is",a
	if a%3==0:
		return True
	else:
		return False

print rand_divis_3()