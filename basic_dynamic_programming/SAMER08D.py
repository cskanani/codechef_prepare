min_sub_seq_len = int(input())
while min_sub_seq_len != 0:
    string1 = ' '+input()
    string2 = ' '+input()
    len_string1 = len(string1)
    len_string2 = len(string2)
    mem = [[0]*len_string1 for i in range(len_string2)]
    for i in range(min_sub_seq_len, len_string2):
        for j in range(min_sub_seq_len, len_string1):
            if string2[i] == string1[j]:
                limit = min(i, j)
                k = 0
                while k < limit and string2[i-k] == string1[j-k]:
                    if k + 1 >= min_sub_seq_len:
                        mem[i][j] = max(mem[i][j], mem[i-k-1][j-k-1] + k + 1)
                    k += 1
            mem[i][j] = max(mem[i][j], mem[i-1][j], mem[i][j-1])
    print(mem[-1][-1])
    min_sub_seq_len = int(input())
