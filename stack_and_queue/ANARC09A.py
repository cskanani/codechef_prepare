parantheses_string = input().strip()
ans_number = 0
while '-' not in parantheses_string:
    ans_number += 1
    operations_required = 0
    bracket_count = 0 # to simmulate stack
    for i in range(len(parantheses_string)):
        if parantheses_string[i] == '{':
            bracket_count += 1
        elif bracket_count > 0 and parantheses_string[i] == '}':
            bracket_count -= 1
        elif parantheses_string[i] == '}':
            operations_required += 1
            bracket_count = 1
    print('{}. {}'.format(ans_number, operations_required + bracket_count//2))
    parantheses_string = input().strip()
