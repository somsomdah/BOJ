# 틀림

import sys

n=int(sys.stdin.readline())
k=int(sys.stdin.readline())

m=0
res=-1
for s in range(1,2*n+1):
     for i in range (1,s//2+1):
          j=s-i
          if i==j:
               m+=1
               if m==k:
                    print(i*j)
                    sys.exit(0)
               
          else:
               m+=1
               if m==k:
                    print(i*j)
                    sys.exit(0)
               m+=1
               if m==k:
                    print(i*j)
                    sys.exit(0)
          
