for _ in range(int(input())):
    total_elephants, available_candies = map(int, input().split())
    required_candies = sum(map(int, input().split()))
    if available_candies >= required_candies:
        print('Yes')
    else:
        print('No')
