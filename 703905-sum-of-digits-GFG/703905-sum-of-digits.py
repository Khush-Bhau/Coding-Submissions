class Solution:
    def sumOfDigits(self, n):
        # code here
        sum = 0
        for i in range(0,n):
            
            r = n % 10
            n = n // 10
            sum = sum+r
        return sum