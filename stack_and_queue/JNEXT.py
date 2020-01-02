for _ in range(int(input())):
    num_of_digits = int(input())
    digits = list(map(int, input().split()))
    small_digit_loc = -1
    for i in range(num_of_digits - 2, -1, -1):
        if digits[i] < digits[i+1]:
            small_digit_loc = i
            break
    if small_digit_loc == -1:
        print(-1)
    else:
        just_greater_num_loc = small_digit_loc + 1
        for i in range(small_digit_loc + 1, num_of_digits):
            if digits[i] > digits[small_digit_loc] and digits[just_greater_num_loc] >= digits[i]:
                just_greater_num_loc = i
        digits[small_digit_loc], digits[just_greater_num_loc] = digits[just_greater_num_loc], digits[small_digit_loc]
        digits[small_digit_loc + 1:] = digits[small_digit_loc + 1:][::-1]
        print(''.join(map(str, digits)))
