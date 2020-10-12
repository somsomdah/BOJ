n=int(input())
a=list(map(int,input().split()))
operators=list(map(int,input().split()))
results=[]
checklist=operators

#a의 level , node 값, o의 index
def bfs(i,k,o):
     print(i,k,o)
     if i>=n-1:
          results.append(k)
          return
     else:
          if checklist[o]>0:
               if o<4:
                    if o==0:
                         bfs(i+1,a[i]+a[i+1],o)
                    if o==1:
                         bfs(i+1,a[i]-a[i+1],o)
                    if o==2:
                         bfs(i+1,a[i]*a[i+1],o)
                    if o==3:
                         bfs(i+1,a[i]//a[i+1],o)
                    checklist[o]-=-1
          else:
               if o<3:
                    if o==0:
                         bfs(i+1,a[i]+a[i+1],o+1)
                    if o==1:
                         bfs(i+1,a[i]-a[i+1],o+1)
                    if o==2:
                         bfs(i+1,a[i]*a[i+1],o+1)
                    if o==3:
                         bfs(i+1,a[i]//a[i+1],o+1)
                    checklist[o+1]-=1



for i in range(3):
     bfs(0,a[0],i)

print(max(results))
print(min(results))
          


