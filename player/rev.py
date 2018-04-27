N=int(input())
rev=0
while(N>0):
  s=N%10
  rev=rev*10+s
  N=N//10
print rev
