class Solution:
    def __init__(self):
        self.memo = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        # Check memoization table
        if (s1, s2) in self.memo:
            return self.memo[(s1, s2)]
        
        # Base Case 1: Strings are identical
        if s1 == s2:
            return True
        
        # Pruning: If they aren't anagrams, they can't be scrambled versions
        # This significantly speeds up the solution
        if sorted(s1) != sorted(s2):
            self.memo[(s1, s2)] = False
            return False
        
        n = len(s1)
        
        # Try every possible split position i (from 1 to n-1)
        for i in range(1, n):
            # Option 1: No Swap
            # Compare s1's left with s2's left AND s1's right with s2's right
            if (self.isScramble(s1[:i], s2[:i]) and 
                self.isScramble(s1[i:], s2[i:])):
                self.memo[(s1, s2)] = True
                return True
            
            # Option 2: Swap
            # Compare s1's left with s2's right AND s1's right with s2's left
            if (self.isScramble(s1[:i], s2[n-i:]) and 
                self.isScramble(s1[i:], s2[:n-i])):
                self.memo[(s1, s2)] = True
                return True
        
        # If no split works
        self.memo[(s1, s2)] = False
        return False