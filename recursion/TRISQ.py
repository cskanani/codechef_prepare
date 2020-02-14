## Recursive Solution - 0.82
#import sys
#sys.setrecursionlimit(10**5)

#def get_count(base_len):
    #if base_len <= 3:
        #return 0
    #return get_count(base_len - 2) + (base_len - 2) // 2

#for _ in range(int(input())):
    #base_len = int(input())
    #print(get_count(base_len))
    
# DP Solution - 0.02
triange_count = [0]*(10**4+1)
for base_len in range(4, 10**4+1):
    triange_count[base_len] += triange_count[base_len - 2] + (base_len - 2) // 2
for _ in range(int(input())):
    base_len = int(input())
    print(triange_count[base_len])
