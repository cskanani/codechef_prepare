import sys
sys.setrecursionlimit(10**6)

def check_seq(thread_elements, thread_indexes, output_seq, output_seq_index):
    if output_seq_index == len(output_seq):
        return True
    for i_thread in range(len(thread_elements)):
        if (
            (len(thread_elements[i_thread]) > thread_indexes[i_thread])
            and (thread_elements[i_thread][thread_indexes[i_thread]] == output_seq[output_seq_index])
        ):
            thread_indexes[i_thread] += 1
            output_seq_index += 1
            if check_seq(thread_elements, thread_indexes, output_seq, output_seq_index):
                return True
            thread_indexes[i_thread] -= 1
            output_seq_index -= 1
    return False
    
for _ in range(int(input())):
    num_threads = int(input())
    thread_elements = []
    for i_thread in range(num_threads):
        thread_elements.append(list(map(int, input().split()))[1:])
    output_seq = list(map(int, input().split()))[::-1]
    if check_seq(thread_elements, [0]*len(thread_elements), output_seq, 0):
        print('Yes')
    else:
        print('No')
