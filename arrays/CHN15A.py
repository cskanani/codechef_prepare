for _ in range(int(input())):
    total_minions, addition_value = map(int, input().split())
    minion_characteristic = list(map(int, input().split()))
    wolverin_minions = 0
    for i in range(total_minions):
        if (minion_characteristic[i] + addition_value) % 7 == 0:
            wolverin_minions += 1
    print(wolverin_minions)
