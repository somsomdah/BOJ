


# !!!!!!!!!!!!!!!!!!!!시간 초과!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
n=int(input())

a=[]

for i in range(1,n+1):
     a.append((i,int(input())))


max_res=-1
res=[]

def dfs(L,arr):

     global max_res
     global res
     
     if L==n:
          set1=set([el[0] for el in arr])
          set2=set([el[1] for el in arr])

          if set1==set2:

               if len(arr)>max_res:
                    max_res=len(arr)
                    res=sorted(list(set1))

     
     else:
          dfs(L+1,arr)
          arr.append(a[L])
          dfs(L+1,arr)
          arr.remove(a[L])


dfs(0,[])

print(max_res)
for r in res:
     print(r)

                    
