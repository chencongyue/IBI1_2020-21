a=010202
b=190784
c=100321
d=abs(a-c)
print("d="+str(d))
e=abs(a-b)
print("e="+str(e))
if d<e:
	print("d<e")
elif d>e:
	print("d>e")
else:
	print("d=e")
