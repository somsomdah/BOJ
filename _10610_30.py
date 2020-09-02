import sys

inpt=sys.stdin.readline()
inpt_num=list(map(int,[n for n in inpt if n!='\n']))
inpt_num.sort(reverse=True)

num=""
for i in inpt_num:
     num+=str(i)
num=int(num)
#print(num)

if sum(inpt_num)%3==0 and num%10==0:
     print(num)
else:
     print(-1)
