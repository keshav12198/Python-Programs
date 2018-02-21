def roots(a,b,c):
	if (b**2)>=(4*a*c):
		r1 = (-b+(((b**2)-(4*a*c))**(0.5)))/(2*a)
		r2 = (-b-(((b**2)-(4*a*c))**(0.5)))/(2*a)
		print ("Roots are %d and %d ", int(r1), int(r2))
	else:
		print "Roots are complex "


print ("Enter the value of a, b and c ")
a = input()
b = input()
c = input()
roots(a,b,c)