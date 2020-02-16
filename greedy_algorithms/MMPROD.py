P = 10**9 + 7
for _ in range(int(input())):
    total_num, k = map(int, input().split())
    num_list = list(map(int, input().split()))
    num_list.sort()
    if num_list[-1] <= 0 and k % 2:
        product = 1
        for i in range(total_num-k, total_num):
            product = product * num_list[i] % P
    else:
        start_ind, end_ind, product = 0, total_num-1, 1
        if k % 2:
            k -= 1
            product = num_list[-1] % P
            end_ind -= 1
        for i in range(k//2):
            if (
                num_list[start_ind]*num_list[start_ind+1]
                > num_list[end_ind]*num_list[end_ind-1]
            ):
                product = product * num_list[start_ind] * num_list[start_ind+1] % P
                start_ind += 2
            else:
                product = product * num_list[end_ind] * num_list[end_ind-1] % P
                end_ind -= 2
    print(product)
