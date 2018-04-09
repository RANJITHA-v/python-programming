n,a,d=raw_input().split(' ')
n1=int(n)
a1=int(a)
d1=int(d)
c=0
for  i in range (1,n1+1):
  s=a1+(i-1)*d1
  c=c+s
print c
