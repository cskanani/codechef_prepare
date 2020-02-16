for _ in range(int(input())):
    input()
    num_teams = int(input())
    preferred_ranks = []
    for i in range(num_teams):
        team_name, preferred_rank = input().split()
        preferred_ranks.append(int(preferred_rank))
    preferred_ranks.sort()
    badness = 0
    for i in range(len(preferred_ranks)):
        badness += abs(i + 1 - preferred_ranks[i])
    print(badness)
