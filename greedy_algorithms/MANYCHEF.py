def possible_chef(signboard, i):
    if (
        (signboard[i] == '?' or signboard[i] == 'C')
        and (signboard[i+1] == '?' or signboard[i+1] == 'H')
        and (signboard[i+2] == '?' or signboard[i+2] == 'E')
        and (signboard[i+3] == '?' or signboard[i+3] == 'F')
    ):
        return True
    return False

for _ in range(int(input())):
    signboard = list(input())
    for i in range(len(signboard)-4, -1, -1):
        if possible_chef(signboard, i):
            signboard[i] = 'C'
            signboard[i+1] = 'H'
            signboard[i+2] = 'E'
            signboard[i+3] = 'F'
    for i in range(len(signboard)):
        if signboard[i] == '?':
            signboard[i] = 'A'
    print(''.join(signboard))
