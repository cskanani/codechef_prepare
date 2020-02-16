for _ in range(int(input())):
    num_days, num_white_buttons, num_black_buttons = map(int, input().split())
    planned_tasks = list(map(int, input().split()))
    completed_tasks = list(map(int, input().split()))
    white_buttons = list(map(int, input().split()))
    black_buttons = list(map(int, input().split()))
    remaining_tasks = [
        (i_planned_tasks - i_completed_tasks)
        for (i_planned_tasks, i_completed_tasks)
        in zip(planned_tasks, completed_tasks)
    ]
    button_powers = white_buttons + black_buttons
    remaining_tasks.sort(reverse=True)
    button_powers.sort(reverse=True)
    remaining_tasks_index = 0
    button_powers_index = 0
    while (
        (remaining_tasks_index < len(remaining_tasks))
        and (button_powers_index < len(button_powers))
    ):
        if remaining_tasks[remaining_tasks_index] >= button_powers[button_powers_index]:
            remaining_tasks[remaining_tasks_index] -= button_powers[button_powers_index]
            remaining_tasks_index += 1
        button_powers_index += 1
    print(sum(remaining_tasks))
