import sys

p,q=map(int,sys.stdin.readline().split())

adj_list=[[] for _ in range(p+1)]


for _ in range(q):
     v1,v2,w=map(int,sys.stdin.readline().split())
     adj_list[v1].append((v2,w))
     adj_list[v2].append((v1,w))


for i in range(1,p+1):
     adj_list[p].sort(key=lambda x:x[1]) # weight가 작은 순으로 정렬


S=[1] #selected
U=[i for i in range(2,p+1)] #unselected
total=0

while U:
     v,w=0,sys.maxsize
     v_s=0
     
     for v1 in S:
          if adj_list[v1]:
               v2,w2=adj_list[v1][0]
               if w2<w:
                    v,w=v2,w2
                    v_s=v1

     if v not in S and v in U:
          S.append(v)
          U.remove(v)

          adj_list[v_s].remove((v,w))
          adj_list[v].remove((v_s,w))

          total+=w


print(total)
      
          
          
     

               
          
               
     
