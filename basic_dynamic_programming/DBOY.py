from sys import stdin
for _ in range(int(input())):
    num_stations = int(input())
    house_distances = list(map(int,stdin.readline().split()))
    fuel_capacity = list(map(int,stdin.readline().split()))
    fuel_capacity.sort()
    min_fill_required = [10**9]*(1001) # gives better performance than float('inf')
    for x in fuel_capacity:
        min_fill_required[x] = 1
    for i in range(1,1001):
        j = 0
        while j < num_stations and fuel_capacity[j] < i: 
            min_fill_required[i] = min(
                min_fill_required[i],
                min_fill_required[i-fuel_capacity[j]]+1
                )
            j += 1
    required_fills = 0
    for house_distance in house_distances:
        required_fills += min_fill_required[2*house_distance]
    print(required_fills)
