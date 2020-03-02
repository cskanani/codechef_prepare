while True:
    try:
        num_mixtures = int(input())
    except:
        break
    mixture_colors = list(map(int, input().split()))
    mem = [[10**9]*(num_mixtures+1) for i in range(num_mixtures+1)]
    for i in range(len(mem)):
        mem[i][i] = 0
    for l in range(1, num_mixtures+1):
        for i in range(num_mixtures-l+2):
            j = i+l-1
            for k in range(i, j):
                mem[i][j] = min(mem[i][j], mem[i][k] + mem[k+1][j] + (sum(mixture_colors[i-1:k])%100)*(sum(mixture_colors[k:j])%100))
    print(mem[1][num_mixtures])
