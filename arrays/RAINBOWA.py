for _ in range(int(input())):
    array_size = int(input())
    array = list(map(int, input().split()))
    start_pointer, end_pointer = 0, array_size - 1
    current_req_element = 1
    current_element_count = 0
    ans = 'yes'
    while start_pointer <= end_pointer:
        if array[start_pointer] != array[end_pointer]:
            ans = 'no'
            break
        elif array[start_pointer] == current_req_element:
            start_pointer += 1
            end_pointer -= 1
            current_element_count += 1
        elif current_element_count:
            current_req_element += 1
            current_element_count = 0
            if current_req_element > 7:
                ans = 'no'
                break
        else:
            ans = 'no'
            break
    if current_req_element != 7 or current_element_count == 0:
        ans = 'no'
    print(ans)            
