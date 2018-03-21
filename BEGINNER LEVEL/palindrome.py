n=int(raw_input())
temp=n
num=0
while(n>0):
  k=n%10
  num=num*10+k
 n=n//10
if(n==num):
  print("yes")
else:
  print("no")  
  
