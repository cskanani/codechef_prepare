#include<bits/stdc++.h>
using namespace std;

int lcs(string str1, string str2) {
    str1 = str1;
    str2 = str2;
    int len_str1 = str1.length();
    int len_str2 = str2.length();
    int i, j, mem[2][len_str2+1];
    memset(mem, 0, sizeof(mem[0][0])*2*(len_str2+1));
    for (i = 0; i <= len_str1; i++) {
        for (j = 0; j <= len_str2; j++) {
            if (i == 0 || j == 0) {
                mem[i%2][j] = 0;
            } else if (str1[i-1] == str2[j-1]) {
                mem[i%2][j] = mem[(i-1)%2][j-1] + 1;
            } else {
                mem[i%2][j] = max(mem[(i-1)%2][j], mem[i%2][j-1]);
            }
        }
    }
    if (len_str1 % 2) {
        return mem[1][len_str2];
    } else {
        return mem[0][len_str2];
    }
    
}

int main() {
    int t;
    string str, rev_str;
    cin >> t;
    while (t--) {
        cin >> str;
        rev_str = str;
        reverse(rev_str.begin(), rev_str.end());
        cout << str.length() - lcs(str, rev_str) << endl;
    }
}
