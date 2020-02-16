for _ in range(int(input())):
    num_participants = int(input())
    men_hotness = list(map(int, input().split()))
    women_hotness = list(map(int, input().split()))
    men_hotness.sort()
    women_hotness.sort()
    total_hotnesss = 0
    for men, women in zip(men_hotness, women_hotness):
        total_hotnesss += men * women
    print(total_hotnesss)
