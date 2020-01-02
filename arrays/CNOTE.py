for _ in range(int(input())):
    total_required_pages, available_pages, available_money, total_books = map(int, input().split())
    required_pages = total_required_pages - available_pages
    ans = 'UnluckyChef'
    for i in range(total_books):
        pages, cost = map(int, input().split())
        if pages >= required_pages and cost <= available_money:
            ans = 'LuckyChef'
    print(ans)
