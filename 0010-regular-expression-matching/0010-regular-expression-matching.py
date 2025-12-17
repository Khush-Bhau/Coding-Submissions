class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # dp[i][j] will store if s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Base case: empty string matches empty pattern
        dp[0][0] = True

        # Initialize first row for patterns like a*, a*b*, .* which match empty string
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # The character before '*' can occur 0 times, effectively removing 
                # the char and the '*' from the pattern consideration
                dp[0][j] = dp[0][j - 2]

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    # Current characters match or pattern has '.', inherit from diagonal
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # Case 1: '*' counts as zero of the preceding element
                    # We check the status excluding the character and the '*'
                    dp[i][j] = dp[i][j - 2]
                    
                    # Case 2: '*' counts as one or more of the preceding element
                    # We check if the preceding element matches the current char in s
                    # If so, we check if the string matched before this char (dp[i-1][j])
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[m][n]