M,N=map(int,input().split())
numbers=list(map(int,input().split()))
queue=list(range(1,M+1))

count=0

for number in numbers:
    p=queue.index(number);
    
    if (p==0):
        queue.remove(number)
        continue;

    temp=queue[:p]
    queue=queue[p+1:]
    queue.extend(temp)
     
    if(p<=len(queue)/2):
        count+=p
    elif(p>len(queue)/2):
        count+=(len(queue))-p+1
        

print(count)
