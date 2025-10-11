class Solution:
    def sumOfDigits(self, n):
        # code here
        sum = 0
        for i in range(0,n):
            
            sum = sum+ n%10
            n = n // 10
        return sum
        # return n%10 + self.sumOfDigits(n//10)
        