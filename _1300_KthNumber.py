import sys

n=int(sys.stdin.readline())
b=[i*j for i in range(1,n+1) for j in range(1,n+1)]
b.sort()

k=int(sys.stdin.readline())
s,e=0,n*n-1

while s<=e:
     m=(s+e)//2

     if b[k]==m:
          print(m)
          break
     if m<b[k]:
          s=m+1
     else:
          e=m-1
# 메모리 초과로 실패
