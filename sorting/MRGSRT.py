from math import ceil
def print_merge_calls(start, end, req_ind, depth):
    if start == req_ind and end == req_ind:
        return depth
    num_ele = end - start + 1
    mid = start + ceil(num_ele / 2) - 1
    if start <= req_ind <= mid:
        print(start, mid)
        return print_merge_calls(start, mid, req_ind, depth+1)
    else:
        print(mid+1, end)
        return print_merge_calls(mid+1, end, req_ind, depth+1)
    
for _ in range(int(input())):
    start, end, req_ind = map(int, input().split())
    depth_count = False
    if req_ind < start or req_ind > end:
        print(-1)
    else:
        print(start, end)
        print(print_merge_calls(start, end, req_ind, 1))
