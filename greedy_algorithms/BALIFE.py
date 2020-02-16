num_processors = int(input())
while num_processors != -1:
    num_process = []
    while len(num_process) != num_processors:
        num_process += list(map(int, input().split()))
        
    total_process = sum(num_process)
    if total_process % num_processors:
        print(-1)
    else:
        required_process = total_process // num_processors
        num_process[0] -= required_process
        time_required = abs(num_process[0])
        for i in range(1, num_processors):
            num_process[i] += num_process[i-1]
            num_process[i] -= required_process
            time_required = max(time_required, abs(num_process[i]))
        print(time_required)
    input()
    num_processors = int(input())
