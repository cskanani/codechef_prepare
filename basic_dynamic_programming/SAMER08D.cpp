#include<bits/stdc++.h>
using namespace std;

int main() {
    int min_sub_seq_len, i, j, k, limit;
    cin >> min_sub_seq_len;
    while (min_sub_seq_len != 0) {
        string str1, str2;
        cin >> str1;
        cin >> str2;
        str1 = " " + str1;
        str2 = " " + str2;
        int len_str1 = str1.length();
        int len_str2 = str2.length();
        int mem[len_str1][len_str2];
        memset(mem, 0, sizeof(mem[0][0]) * len_str1 * len_str2);
        for (i = 1; i < len_str1; i++) {
            for (j = 1; j < len_str2; j++) {
                if (str1[i] == str2[j]) {
                    limit = min(i, j);
                    k = 0;
                    while (k < limit && str1[i-k] == str2[j-k]) {
                        if (k + 1 >= min_sub_seq_len) {
                            mem[i][j] = max(mem[i][j], mem[i-k-1][j-k-1] + k + 1);
                        }
                        k++;
                    }
                }
                mem[i][j] = max(mem[i][j], max(mem[i-1][j], mem[i][j-1]));
            }
        }
        cout << mem[len_str1-1][len_str2-1] << endl;
        cin >> min_sub_seq_len;
    }
}
