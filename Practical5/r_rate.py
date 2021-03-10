n=84
r=1.2
c=1
#c is the number of rounds
for c in range (1,6):
	n=n*r
	c=c+1
	a=str(n)
	b="The number of infected individuals ater 5 rounds of infection is "+a
	if c==5:
		print (b)
