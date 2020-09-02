def num_bridges(N,M):
    temp = [[-1 for col in range(M+1)] for row in range(N+1)]
    
    for i in range(N+1):
        for j in range(M+1):
            if i>j:
                temp[i][j]=0
            elif i==j or i==0 :
                temp[i][j]=1
                
    for i in range(N+1):
        for j in range(M+1):
            if (temp[i][j]==-1):
                temp[i][j]=temp[i][j-1]+temp[i-1][j-1]            
                

    print(temp[N][M])
    
num_input=int(input())

for i in range(num_input):
    case=input().split(" ")
    num_bridges(int(case[0]),int(case[1]))