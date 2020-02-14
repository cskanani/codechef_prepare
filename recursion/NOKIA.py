def get_min_required_wire(length):
    if length < 2:
        return 0
    elif length == 2:
        return 2
    elif length % 2:
        return length + get_min_required_wire(length//2) + get_min_required_wire(length//2 + 1)
    else:
        return length + 2*get_min_required_wire(length//2)
    
for _ in range(int(input())):
    num_posts, wire_available = map(int, input().split())
    min_wire_required = get_min_required_wire(num_posts+1)
    if min_wire_required > wire_available:
        print(-1)
    else:
        max_wire_required = num_posts * (num_posts + 1) // 2 + num_posts
        print(max(0, wire_available - max_wire_required)) 
