class PrimePolynom {
    public:
        bool isPrime(int n) {
            if (n < 2) {
                return false;
            } else {
                for (int j = 2; j*j <= n; j++) {
                    if (n % j == 0) {
                        return false;
                    }
                }
                return true;
            }
        }
        int reveal(int A, int B, int C) {
            for (int m = 0; true; m++) {
                if (!isPrime(A*m*m + B*m + C)) {
                    return m;
                }
            }
        }
};
