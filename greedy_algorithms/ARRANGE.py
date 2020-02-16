for _ in range(int(input())):
    num_amplifiers = int(input())
    amplifier_powers = list(map(int, input().split()))
    amplifier_powers.sort(reverse=True)
    if num_amplifiers > 1 and amplifier_powers[0] == 3 and amplifier_powers[1] == 2:
        amplifier_powers[0] = 2
        amplifier_powers[1] = 3
    i = num_amplifiers - 1
    while i > -1 and amplifier_powers[i] == 1:
        i -= 1
    amplifier_powers = amplifier_powers[i+1:] + amplifier_powers[:i+1]
    print(' '.join(map(str, amplifier_powers)))
