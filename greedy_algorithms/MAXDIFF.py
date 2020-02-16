for _ in range(int(input())):
    num_itemes, split_size = map(int, input().split())
    weights = list(map(int, input().split()))
    weights.sort()
    max_weight_diff = max(
        abs(sum(weights[:split_size]) - sum(weights[split_size:])),
        abs(sum(weights[-split_size:]) - sum(weights[:-split_size]))
    )
    print(max_weight_diff)
