for _ in range(int(input())):
    num_tables, num_orders = map(int, input().split())
    orders = list(map(int, input().split()))
    
    prev_occurance = {}
    next_occurance = [float('inf')]*num_orders
    for i in range(num_orders-1, -1, -1):
        if orders[i] in prev_occurance:
            next_occurance[i] = prev_occurance[orders[i]]
        prev_occurance[orders[i]] = i
    
    sitting = {}
    cleaning_count = 0
    for i in range(num_orders):
        if orders[i] not in sitting:
            if len(sitting) == num_tables:
                remove_customer = -1
                customer_next_occrance = -1
                for customer in sitting:
                    if sitting[customer] > customer_next_occrance:
                        customer_next_occrance = sitting[customer]
                        remove_customer = customer
                del sitting[remove_customer]
            cleaning_count += 1
        sitting[orders[i]] = next_occurance[i]
    
    print(cleaning_count)
