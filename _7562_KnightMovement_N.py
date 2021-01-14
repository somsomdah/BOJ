dx=[1,1,-1,-1,2,2,-2,-2]
dy=[2,-2,2,-2,1,-1,1,-1]


def dfs(x,y):
     global count
     checklist[x][y]=1
     count+=1
     
     if x==dest_x and y==dest_y:
          return
     else:
          for i in range(8):
               xx=x+dx[i]
               yy=y+dy[i]

               if 0<=xx<l and 0<=yy<l and checklist[xx][yy]==0:
                    dfs(xx,yy)

               
     

t=int(input())

for _ in range(t):
     l=int(input())
     start_x,start_y=map(int,input().split())
     dest_x,dest_y=map(int,input().split())
     checklist=[[0]*l for _ in range(l)]
     count=0

     dfs(start_x,start_y)

     print(count)
