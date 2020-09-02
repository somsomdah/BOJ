import sys

q=[]

N=int(sys.stdin.readline()) # input 보다 빠름

for i in range(N):
    c=list(map(int,sys.stdin.readline().split()))
    q.append(c)
q.sort(key=lambda c:(c[0],c[1])) # 다중키 sort

for c in q:
    print(c[0],c[1]);