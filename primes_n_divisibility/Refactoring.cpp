class Refactoring {
    public:
        int rec_count(int n, int min_factor) {
            int count = 0;
            for (int j = min_factor; j*j <= n; j++) {
                if (n%j == 0) {
                    count += rec_count(n/j, j) + 1;
                }
            }
            return count;
        }
        int refactor(int n) {
            return rec_count(n, 2);
        }
};
