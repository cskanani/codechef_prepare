#include <bits/stdc++.h>
class DivisorInc {
public:
  int countOperations (int n, int m) {
        int vis[m+1];
        memset( vis, 0, (m+1)*sizeof(int) );
        vis[n] = 1;
        for (int i = n; i <= m; i++) {
            if (vis[i]) {
                for (int j = 2; j*j <= i; j++) {
                    if (i % j == 0 && i + j <= m) {
                        if (vis[i + j]) {
                            vis[i + j] = std::min(vis[i] + 1, vis[i + j]);
                        } else {
                            vis[i + j] = vis[i] + 1;
                        }
                        if (i + i / j <= m) {
                            if (vis[i + i / j]) {
                                vis[i + i / j] = std::min(vis[i] + 1, vis[i + i / j]);
                            } else {
                                vis[i + i / j] = vis[i] + 1;
                            }
                        }
                    }
                }
            }
        }
        return vis[m] - 1;
    }
};
