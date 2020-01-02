for _ in range(int(input())):
    total_cops, houses_per_min, search_time = map(int, input().split())
    houses_by_cop = houses_per_min * search_time
    cop_location = [location - 1 for location in map(int, input().split())]
    cop_location.sort()
    safe_house_count = 0
    next_candidate_house = 0
    for i in range(total_cops):
        safe_house_count += max(0, cop_location[i] - houses_by_cop - next_candidate_house)
        next_candidate_house = cop_location[i] + houses_by_cop + 1
    safe_house_count += max(0, 100 - next_candidate_house)
    print(safe_house_count)
