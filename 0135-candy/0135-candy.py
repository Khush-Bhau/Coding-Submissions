class Solution(object):
    def candy(self, ratings):
        n = len(ratings)
        if n == 0:
            return 0

        # Step 1: everyone gets at least one candy
        candies = [1] * n

        # Step 2: left-to-right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Step 3: right-to-left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)
