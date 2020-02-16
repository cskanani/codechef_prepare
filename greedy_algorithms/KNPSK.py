num_items = int(input())
costs_weight1 = []
costs_weight2 = []
total_weight = 0
for i in range(num_items):
    weight, cost = map(int, input().split())
    total_weight += weight
    if weight == 1:
        costs_weight1.append(cost)
    else:
        costs_weight2.append(cost)
costs_weight1.sort(reverse=True)
costs_weight2.sort(reverse=True)
max_costs = [0]*(total_weight + 1)
weight1_index, weight2_index = 0, 0

# Filling even weights
for i in range(2, len(max_costs), 2):
    cost1 = 0
    cost2 = 0
    if weight1_index < len(costs_weight1):
        cost1 += costs_weight1[weight1_index]
    if weight1_index+1 < len(costs_weight1):
        cost1 += costs_weight1[weight1_index+1]
    
    if weight2_index < len(costs_weight2):
        cost2 += costs_weight2[weight2_index]
    
    if cost1 > cost2:
        max_costs[i] = max_costs[i-2] + cost1
        weight1_index += 2
    else:
        max_costs[i] = max_costs[i-2] + cost2
        weight2_index += 1
        
# Filling odd weights

if len(costs_weight1) != 0:
    max_costs[1] = costs_weight1[0]

weight1_index, weight2_index = 1, 0

for i in range(3, len(max_costs), 2):
    cost1 = 0
    cost2 = 0
    if weight1_index < len(costs_weight1):
        cost1 += costs_weight1[weight1_index]
    if weight1_index+1 < len(costs_weight1):
        cost1 += costs_weight1[weight1_index+1]
    
    if weight2_index < len(costs_weight2):
        cost2 += costs_weight2[weight2_index]
    
    if cost1 > cost2:
        max_costs[i] = max_costs[i-2] + cost1
        weight1_index += 2
    else:
        max_costs[i] = max_costs[i-2] + cost2
        weight2_index += 1
    

print(' '.join(map(str, max_costs[1:])))
