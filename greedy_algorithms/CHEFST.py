for _ in range(int(input())):
    stack1_count, stack2_count, maximum_removal = map(int, input().split())
    maximum_possible_removal = min(
        stack1_count,
        stack2_count,
        maximum_removal * (maximum_removal + 1) // 2
    )
    stack1_count -= maximum_possible_removal
    stack2_count -= maximum_possible_removal
    print(max(0, stack1_count + stack2_count))
