for _ in range(int(input())):
    num_workers = int(input())
    worker_salary = list(map(int, input().split()))
    min_salary = min(worker_salary)
    
    # we are selecting a worker and decreasing its salary by 1
    # the minimum moves will be achieved if we make salaries of all worker equal to minimum salary
    required_moves = 0
    for i in range(num_workers):
        required_moves += worker_salary[i] - min_salary
    print(required_moves)
