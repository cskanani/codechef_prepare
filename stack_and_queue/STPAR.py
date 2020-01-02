num_of_trucks = int(input())
while num_of_trucks:
    stack = []
    truck_order = list(map(int, input().split()))
    current_req_truck = 1
    i = 0
    while i < num_of_trucks:
        if truck_order[i] != current_req_truck:
            if stack and stack[-1] == current_req_truck:
                stack.pop()
                current_req_truck += 1
                i -= 1
            else:
                stack.append(truck_order[i])
        else:
            current_req_truck += 1
        i += 1
    while stack and stack[-1] == current_req_truck:
        current_req_truck += 1
        stack.pop()
    if stack:
        print('no')
    else:
        print('yes')
    num_of_trucks = int(input())
