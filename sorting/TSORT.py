#import sys
#sys.setrecursionlimit(10**5)
#from sys import stdin
#from random import shuffle

#def partition(nums_list, start, end):
    #small_ind = (start - 1)
    #pivot = nums_list[end]
    #for nums_list_i in range(start, end):
        #if nums_list[nums_list_i] < pivot:
            #small_ind += 1
            #nums_list[nums_list_i], nums_list[small_ind] = nums_list[small_ind], nums_list[nums_list_i]
    #nums_list[end], nums_list[small_ind+1] = nums_list[small_ind+1], nums_list[end]
    #return small_ind+1

#def quick_sort(nums_list, start, end):
    #if start >= end:
        #return
    #pivot_i = partition(nums_list, start, end)
    #quick_sort(nums_list, start, pivot_i - 1)
    #quick_sort(nums_list, pivot_i + 1, end)
    
#nums_count = int(stdin.readline())
#nums_list = []
#for nums_list_i in range(nums_count):
    #nums_list.append(int(stdin.readline()))
#shuffle(nums_list)
#quick_sort(nums_list, 0, nums_count-1)
#print('\n'.join(map(str, nums_list)))

from sys import stdin
nums_count = int(stdin.readline())
nums_list = []
for nums_list_i in range(nums_count):
    nums_list.append(int(stdin.readline()))
nums_list.sort()
print('\n'.join(map(str, nums_list)))
