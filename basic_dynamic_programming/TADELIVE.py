# DP Solution can only pass tasks 1 and 2
# This is the Greedy approach to solve the problem
total_orders, andy_capacity, bob_capacity = map(int, input().split())
andy_tips = list(map(int, input().split()))
bob_tips = list(map(int, input().split()))
tips = list(zip(andy_tips, bob_tips))
tips.sort(key=lambda x: abs(x[0]-x[1]), reverse=True)
tips_received = 0
for andy_tip, bob_tip in tips:
    if andy_capacity and andy_tip >= bob_tip:
        tips_received += andy_tip
        andy_capacity -= 1
    elif bob_capacity and bob_tip >= andy_tip:
        tips_received += bob_tip
        bob_capacity -= 1
    elif andy_capacity:
        tips_received += andy_tip
        andy_capacity -= 1
    else:
        tips_received += bob_tip
        bob_capacity -= 1
print(tips_received)
