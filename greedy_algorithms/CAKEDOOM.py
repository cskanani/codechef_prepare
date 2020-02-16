for _ in range(int(input())):
    available_colors = int(input())
    arrangement = list(input())
    if available_colors == 2:
        for i in range(len(arrangement)):
            if arrangement[i] != '?':
                arrangement[i%2] = arrangement[i]
                break
    possible = True
    for i in range(len(arrangement)):
        next_color = arrangement[(i+1)%len(arrangement)]
        if arrangement[i] != '?' and arrangement[i] == next_color:
            possible = False
            break
    if not possible and len(arrangement) > 1:
        ans = 'NO'
    else:
        for i in range(len(arrangement)):
            if arrangement[i] == '?':
                previous_color = arrangement[i-1]
                next_color = arrangement[(i+1)%len(arrangement)]
                for j in range(available_colors):
                    if str(j) != previous_color and str(j) != next_color:
                        arrangement[i] = str(j)
                        break
            if arrangement[i] == '?':
                possible = False
                break
        if not possible and len(arrangement) > 1:
            ans = 'NO'
        else:
            ans = ''.join(arrangement)
    print(ans)
