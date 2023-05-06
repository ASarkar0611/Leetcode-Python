class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1: return True
        i = 1; p = 1; flag = 0
        while p <= n:
            p = p * 2
            print("p =", p)
            #i += 1
            if p == n:
                flag = 1
                break
            elif p > n:
                flag = 0
        if flag == 1: return True
        else: return False