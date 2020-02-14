from itertools import permutations

class PrimeAnagrams:
    def is_prime(self,n):
        if n < 2:
            return False 
        for i in range(2,int(n**0.5)+1):
            if not n%i:
                return False
        return True

    def primes(self, chars):
        chars_len = len(chars)
        primes_list = []
        for permutation in permutations(chars):
            for i in range(1, chars_len-1):
                for j in range(i+1, chars_len):
                    if permutation[0] == '0' or permutation[i] == '0' or permutation[j] == '0':
                        continue
                    num1 = int(''.join(permutation[:i]))
                    num2 = int(''.join(permutation[i:j]))
                    num3 = int(''.join(permutation[j:]))
                    if self.is_prime(num1) and self.is_prime(num2) and self.is_prime(num3):
                        if primes_list:
                            if primes_list[0]*primes_list[1]*primes_list[2] > num1*num2*num3:
                                primes_list = [num1, num2, num3]
                        else:
                            primes_list = [num1, num2, num3]
        primes_list.sort()
        return primes_list
