for _ in range(int(input())):
    target_num = int(input())
    purchased_items = 0
    if target_num > 4095:
        purchased_items += (target_num // 2048)
        target_num %= 2048
    purchased_items += bin(target_num).count('1')
    print(purchased_items)
