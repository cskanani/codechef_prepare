def get_max_xor(num_list):
    stack = []
    max_xor = num_list[0] ^ num_list[1]
    for i in range(len(num_list)):
        while stack and stack[-1] < num_list[i]:
            stack.pop()
        stack.append(num_list[i])
        if len(stack) > 1:
            max_xor = max(max_xor, stack[-1] ^ stack[-2])
    return max_xor

list_len = int(input())
num_list = list(map(int, input().split()))
print(max(get_max_xor(num_list), get_max_xor(num_list[::-1])))
