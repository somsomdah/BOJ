import sys
import math

N=int(sys.stdin.readline())
divisor_list=list(map(int,sys.stdin.readline().split()))
divisor_list.sort()

print(divisor_list[0]*divisor_list[-1])
