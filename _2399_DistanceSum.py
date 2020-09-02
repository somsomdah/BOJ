N = int(input())
X=list(map(int,input().split()))
X.sort();

result=0;
for i in range(N):
    result+=(i-(N-(i+1)))*X[i]
    
result*=2;

print(result)