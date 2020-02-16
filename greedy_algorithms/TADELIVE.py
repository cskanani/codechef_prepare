total_delivery, andy_capacity, bob_capacity = map(int, input().split())
andy_tips = list(map(int, input().split()))
bob_tips = list(map(int, input().split()))
tips_diff = [(abs(andy_tip - bob_tip), andy_tip, bob_tip)
             for (andy_tip, bob_tip) in zip(andy_tips, bob_tips)]
tips_diff.sort(reverse=True)

tips_received = 0
for i in range(total_delivery):
    if tips_diff[i][1] > tips_diff[i][2] and andy_capacity:
        tips_received += tips_diff[i][1]
        andy_capacity -= 1
    else:
        tips_received += tips_diff[i][2]
        bob_capacity -= 1   
print(tips_received)
