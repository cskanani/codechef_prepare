from collections import defaultdict
for _ in range(int(input())):
    num_customers, num_compartments = map(int, input().split())
    customer_list = []
    for i in range(num_customers):
        customer_list.append(list(map(int, input().split())))
    customer_list.sort(key=lambda x: x[1])
    allowed_count = 0
    compartments = defaultdict(int)
    for customer in customer_list:
        if compartments[customer[2]] <= customer[0]:
            compartments[customer[2]] = customer[1]
            allowed_count += 1
    print(allowed_count)
