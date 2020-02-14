# Recursion - 6.39
import sys
sys.setrecursionlimit(10**6)

def mat_multi(a, b, mod):
    c = [[0, 0], [0, 0]]
    c[0][0] = (a[0][0]*b[0][0] + a[0][1]*b[1][0]) % mod
    c[0][1] = (a[0][0]*b[1][0] + a[0][1]*b[1][1]) % mod
    c[1][0] = (a[1][0]*b[0][0] + a[1][1]*b[1][0]) % mod
    c[1][1] = (a[1][0]*b[1][0] + a[1][1]*b[1][1]) % mod
    return c

def get_fibonacci_num(mat, n, mod):
    if n <= 1:
        output_mat = mat
    elif n%2:
        output_mat = get_fibonacci_num(mat, n//2, mod)
        output_mat = mat_multi(output_mat, output_mat, mod)
        output_mat = mat_multi(mat, output_mat, mod)
    else:
        output_mat = get_fibonacci_num(mat, n//2, mod)
        output_mat = mat_multi(output_mat, output_mat, mod)
    return output_mat

for _ in range(int(input())):
    num_people, mod = map(int, input().split())
    fibonacci_mat = get_fibonacci_num([[1, 1], [1, 0]], num_people + 1, mod)
    print(fibonacci_mat)
    print(fibonacci_mat[1][1] * 2 % mod)
