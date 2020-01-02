bar_heights = list(map(int, input().split()))
while bar_heights[0]:
    bar_heights = bar_heights[1:] + [-1] # added -1 for computing area of elements in stack when all bars are processed
    stack = []
    max_area = 0
    for i in range(len(bar_heights)):
        cur_right_index = i
        while stack and bar_heights[stack[-1]] >= bar_heights[i]:
            cur_height = bar_heights[stack.pop()]
            if stack:
                cur_left_index = stack[-1]
            else:
                cur_left_index = -1
            cur_area = cur_height * (cur_right_index - cur_left_index - 1)
            max_area = max(max_area, cur_area)
        stack.append(i)
    print(max_area)
    bar_heights = list(map(int, input().split()))
