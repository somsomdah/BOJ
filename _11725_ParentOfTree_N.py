import sys

n=int(sys.stdin.readline())

adj_mat=[[0]*(n+1) for _ in range(n+1)]

for _ in range(n-1):
     i,j=map(int,sys.stdin.readline().split())
     adj_mat[i][j]=1
     adj_mat[j][i]=1

     

adj_list=[[] for _ in range(n+1)]


Q=[1]

while Q:
     v=Q.pop(0)

     for i in range(1,n+1):
          if adj_mat[v][i]==1:
               adj_list[v].append(i)
               adj_mat[v][i],adj_mat[i][v]=0,0
               Q.append(i)



parent=[0]*(n+1)

for i in range(1,n+1):
     childs=adj_list[i]
     for c in childs:
          parent[c]=i

for i in range(2,n+1):
     print(parent[i])
