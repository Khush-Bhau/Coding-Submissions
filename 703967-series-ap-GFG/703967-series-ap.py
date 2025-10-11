
class Solution:
    def nthTermOfAP(self, a1 : int, a2 : int, n : int) -> int:
        # code here
        
# Where:
# an = nth term,
# a = first term,
# d = common difference,
# n = term number.

# Substitute the values of a, d, and n into the formula to calculate an.

        d = a2-a1
        # an = a1 + (n - 1)d
        return a1 + (n - 1)*d