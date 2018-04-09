a1=[]
b1=int(raw_input())
for i in range(1,b1+1):
	d=int(raw_input(" "))
	a1.append(d)
a1.sort()
print max(a1)
