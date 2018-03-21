n=int(raw_input())
temp=n
count=0
val=0
if(n<=100000):
  while(n!=0):
    n=n/10
    count=count+1
n=temp
while(n!=0):
  r=n%10
  val+=r**count
  n=n/10
if(temp==val):
  print("Yes")
else:
  print("No")
  
